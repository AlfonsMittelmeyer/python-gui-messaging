import threading
import queue

class Proxy:
 
    def __init__(self,extern_proxy=None):

        # if there is an extern proxy, multiple threads may communicate
        # via this extern proxy without knowing each other
        if extern_proxy == None: self.extern_proxy = self
        else: self.extern_proxy = extern_proxy
 
        self.reset()

    def __del__(self):
        # unregister extern registered callbacks
        if self.extern_proxy != self: self.extern_proxy.undo_receiveAll_extern(self)

    # extern trigger for communication between threads
    # extern trigger before start of event loop
    # - before there is an event loop, extern triggers by events will not have an effect
    # - for tkinter the extern trigger may be used or polling
    def _noop(self): pass

    def reset(self):

        # Configuration for triggers at start, which may be changed by the user
        self.trigger = self.do_work # intern trigger at start is direct call of 'do_work'.
        self.extern_trigger = self._noop # extern trigger at start is set to do nothing. feel free to change this in your application

        self._Dictionary = {} # contains registered message ids and registered callback functions for these message ids
        self._owners = {} # contains owners and their callback functions:
                         # callback functions may be registerd for an owner (or for None in case of existence of the callbacks until end)
                         # if the owner becomes deleted it should unregister all it's callback functions
                         # because of this dictionary this may be done at once for all callback functions via undo_receiveAll or undo_receiveAll_extern

        self._Queue = queue.Queue() # Queue for sending messages
        self._Queue_HighPrio = queue.Queue() # Queue for register and unregister callback functions
        self._register("execute_function",lambda msg: msg()) # very useful callback function: executes messages, which are lambda expressions
        self._running = False # regulates calls of method 'do_work' - start value False enables call of method 'work'
        self._looping = False # regulates ending event loop. After 'loop' is called, the loop may be ended by calling 'exit_loop'

    # process a message in a queue ==========
    def work(self,*args):

        # get message from Queue
        if not self._Queue_HighPrio.empty(): data = self._Queue_HighPrio.get()
        elif not self._Queue.empty(): data = self._Queue.get()
        else: return False

        # look up message id and registered callbacks for it and call callback
        msgid = data[0]
        msgdata = data[1]
        if msgid in self._Dictionary:
            receivers = self._Dictionary[msgid].items() # items contain callback function and optional_parameter
            for callback,optional_parameter in receivers:
                if type(optional_parameter) is bool:
                    if optional_parameter: callback((msgid,msgdata))
                    else: callback(msgdata)
                else: callback((optional_parameter,(msgid,msgdata)))
        return True

    # process all messages in the queues ========
    def do_work(self,*args):
        if self._running: return
        self._running = True
        while self.work(): pass
        self._running = False

    # set both triggers at once, if it's the same ========
    def set_trigger(self,trigger):
        self.trigger = trigger
        self.extern_trigger = trigger

    # loop for event driven threads - don't use this in a GUI event loop (mainloop) - it will block the GUI
    def loop(self,do_with_loop = None):
        self.event = threading.Event()
        self.set_trigger(self.event.set)
        self.event.set()
        self._looping = True
        if do_with_loop != None: do_with_loop()
        while self._looping:
            self.event.wait()
            self.event.clear()
            self.do_work()

    # exit event loop 
    def exit_loop(self,*args):
        self._looping = False
        self.trigger()

    # send functions invoke registered callbacks for the message id =======

    # send function within same thread
    def send(self,msgid,msgdata=None):
        self._Queue.put((msgid,msgdata))
        self.trigger()

    # send function called by another thread - use it, if you directly want to access the proxy of another thread
    def send_extern(self,msgid,msgdata=None):
        self._Queue.put((msgid,msgdata))
        self.extern_trigger()

    # send function called by another thread - you may use it also use it, if you directly want to access the proxy of another thread
    # this send function is used also in connection with communication via external proxy
    def receive_extern(self,message):
        self._Queue.put(message)
        self.extern_trigger()

    # high prio should only be used for registrations ==
    def send_highprio(self,msgid,msgdata=None):
        self._Queue_HighPrio.put((msgid,msgdata))
        self.trigger()

    # high prio should only be used for registrations ==
    def send_extern_highprio(self,msgid,msgdata=None):
        self._Queue_HighPrio.put((msgid,msgdata))
        self.extern_trigger()

    # extern send and receive callbacks connected with the external proxy =======

    # registering a list of message ids, which shall be received via the external proxy
    def do_receive_extern(self,message_ids,owner=None):
        if owner == None: owner = self
        for mid in message_ids: self.extern_proxy.do_receive_extern_one(owner,mid,self.receive_extern,True)

    # registering a list of message ids, which shall be sent to other tasks via the external proxy
    def do_send_extern(self,message_ids,owner=None):
        if owner == None: owner = self
        for mid in message_ids: self.do_receive(owner,mid,self.send_intern_extern,True)

    # callback for do_send_extern
    def send_intern_extern(self,message): self.extern_proxy.receive_extern(message)

    # register callbacks ================================================

    # normal case - we use the queue - different reasons
    def do_receive(self,owner,msgid,callback,optional_parameter=False):
        self._Queue_HighPrio.put(("execute_function",lambda: self._do_receive(owner,msgid,callback,optional_parameter)))
        self.trigger()

    # normally not used - if you want to receive messages from another thread without using the external proxy
    # or if another thread wants to receive messages from this thread without the external proxy
    def do_receive_extern_one(self,owner,msgid,callback,optional_parameter=False):
        self._Queue_HighPrio.put(("execute_function",lambda: self._do_receive(owner,msgid,callback,optional_parameter)))
        self.extern_trigger()

    # register callback for the owner, so that it may be unregistered by undo_receive_All
    # and call register callback
    def _do_receive(self,owner,msgid,callback,optional_parameter):
        if owner != None:
            if not owner in self._owners: self._owners[owner] = {}
            self._owners[owner][callback]=msgid
        self._register(msgid,callback,optional_parameter)

    # register message id, callback and optional_parameter in the message id dictionary
    def _register(self,msgid,callback,optional_parameter=False):
        if msgid not in self._Dictionary: self._Dictionary[msgid] = {}
        self._Dictionary[msgid][callback] = optional_parameter


    # normal case - we use the queue - different reasons
    def do_receive_option(self,owner,msgid,callback,optional_parameter=False):
        self._Queue_HighPrio.put(("execute_function",lambda: self._do_receive_option(owner,msgid,callback,optional_parameter)))
        self.trigger()

    # register callback for the owner, so that it may be unregistered by undo_receive_All
    # and call register callback
    def _do_receive_option(self,owner,msgid,callback,optional_parameter):
        if owner != None:
            if not owner in self._owners: self._owners[owner] = {}
            self._owners[owner][callback]=msgid
        self._register_option(msgid,callback,optional_parameter)
        
    # register message id, callback and optional_parameter in the message id dictionary
    def _register_option(self,msgid,callback,optional_parameter=False):
        if msgid not in self._Dictionary: self._Dictionary[msgid] = {}
        if callback not in self._Dictionary[msgid]: self._Dictionary[msgid][callback] = {}
        self._Dictionary[msgid][callback][optional_parameter] = None

    # unregister callback ================================================

    # normal case - we use the queue - different reasons
    def undo_receive(self,owner,msgid,callback):
        self._Queue_HighPrio.put(("execute_function",lambda: self._undo_receive(owner,msgid,callback)))
        self.trigger()
 
    # normally not used - only interesting for callbacks in connection with other threads without using the external proxy
    def undo_receive_extern(self,owner,msgid,callback):
        self._Queue_HighPrio.put(("execute_function",lambda: self._undo_receive(owner,msgid,callback)))
        self.extern_trigger()

    # unregister callback for the owner
    # and call unregister register callback
    def _undo_receive(self,owner,msgid,callback):
        if owner != None:
            if owner in self._owners:
                if callback in self._owners[owner]: del self._owners[owner][callback]
        self._unregister1(msgid,callback)

    # unregister message id, callback (and optional_parameter) by removing the entry from the dictionary
    def _unregister1(self,msgid,callback):
        if msgid in self._Dictionary:
            receivers = self._Dictionary[msgid]
            if callback in receivers:
                del receivers[callback]
                if len(receivers) == 0: del self._Dictionary[msgid]


    # normal case - we use the queue - different reasons
    def undo_receive_option(self,owner_and_option,msgid,callback):
        self._Queue_HighPrio.put(("execute_function",lambda: self._undo_receive_option(owner_and_option,msgid,callback)))
        self.trigger()


    # unregister callback for the owner
    # and call unregister register callback
    def _undo_receive_option(self,owner_and_option,msgid,callback):
        if owner_and_option != None:
            if owner_and_option in self._owners:
                if callback in self._owners[owner_and_option]: del self._owners[owner_and_option][callback]
        self._unregister1_option(msgid,owner_and_option,callback)

    # unregister message id, callback (and optional_parameter) by removing the entry from the dictionary
    def _unregister1_option(self,owner_and_option,msgid,callback):
        if msgid in self._Dictionary:
            receivers = self._Dictionary[msgid]
            if callback in receivers:
                if owner_and_option in receivers[callback]:
                    del receivers[callback][owner_and_option]
                    if len(receivers[callback]) == 0:
                        del receivers[callback]
                        if len(receivers) == 0: del self._Dictionary[msgid]

    # unregister Owner ================================================

    # unregister all callbacks of an owner
    def undo_receiveAll(self,owner):
        self._Queue_HighPrio.put(("execute_function",lambda: self._undo_receiveAll(owner)))
        self.trigger()

    # unregister all callbacks of an owner, which are registered by the proxy of another thread
    def undo_receiveAll_extern(self,owner):
        self._Queue_HighPrio.put(("execute_function",lambda: self._undo_receiveAll(owner)))
        self.extern_trigger()

    # remove owner_and_option from the owners dictionary and unregister its callbacks ============
    # undo_receiveAll_option should be called, if an owner_and_option is destroyed and the callbacks would become not valid after this
    def _undo_receiveAll(self,owner):
        if owner in self._owners:
            messages = self._owners[owner]
            del self._owners[owner]
            for callback,msgid in messages.items(): self._unregister1(msgid,callback)

    # unregister all callbacks of an owner_and_option
    def undo_receiveAll_option(self,owner_and_option):
        print("UndoAll")
        self._Queue_HighPrio.put(("execute_function",lambda: self._undo_receiveAll_option(owner_and_option)))
        self.trigger()

    # remove owner_and_option_and_option from the owners dictionary and unregister its options maybe the callbacks ============
    def _undo_receiveAll_option(self,owner_and_option):
        if owner_and_otion in self._owners:
            messages = self._owners[owner_and_option]
            del self._owners[owner_and_option]
            for callback,msgid in messages.items():
                print("unregister",msgid)
                self._unregister1_option(owner_and_option,msgid,callback)
            
    def wait_unroute(self,unroute):
        self.extern_proxy.do_receive_extern_one(self,"UNROUTED",self.exit_loop)
        self.loop(unroute)
