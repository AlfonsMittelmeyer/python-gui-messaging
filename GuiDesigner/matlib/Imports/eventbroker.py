import sys
def output(param):
    sys.stdout.write(param+'\n')

class EventBroker():
    def __init__(self):
        self._dictionary_ = {}
 
    def subscribe(self,message_id,callback_or_alias):

        is_string = True

        try: # python2
            is_string = isinstance(callback_or_alias,basestring)
        except NameError: #python 3
            is_string = isinstance(callback_or_alias,str)
            
        if is_string:
            if message_id not in self._dictionary_:
                self._dictionary_[message_id] = set()
            self._dictionary_[message_id].add(callback_or_alias)
            
        else:
            if message_id in self._dictionary_:

                callback = self._dictionary_[message_id]
                if isinstance(callback ,set):
                    output("EventBroker: message '{}' is a broadcast message. It's not allowed to overwrite it by a callback.".format(message_id))
                else:                
                    output('EventBroker: callback already defined for message id: {}\nThe callback before will be overwritten'.format(message_id))
                    self._dictionary_[message_id] = callback_or_alias
            else:
                self._dictionary_[message_id] = callback_or_alias
 

    def publish(self,message_id,*args,**kwargs):
        if message_id not in self._dictionary_:
            output('EventBroker: no callback defined for message: {},*{},**{}'.format(message_id,args,kwargs))
        else:
            callback = self._dictionary_[message_id]
            if not isinstance(callback ,set):
                return callback(*args,**kwargs)
            for element in callback:
                if element in self._dictionary_:
                    callback = self._dictionary_[element]
                    if isinstance(callback,set):
                        output("EventBroker: for message id '{}' is alias '{}' allowed, but no furter aliases for this alias".format(message_id,element))
                    else:
                        callback(*args,**kwargs)


eventbroker = EventBroker()
publish = eventbroker.publish
subscribe = eventbroker.subscribe


if __name__ == '__main__':

# =========================== Test ==============================
# for aliases are only strings allowed

    def receiver_A():

        def got(info):
            output('receiver_A got info: ' + info)

        subscribe('BROADCAST','BROADCAST_A')
        subscribe('BROADCAST_A',got)

    def receiver_B():

        def got(info):
            output('receiver_B got info: ' + info)

        subscribe('BROADCAST','BROADCAST_B')
        subscribe('BROADCAST_B',got)

    receiver_A()
    receiver_B()

    publish('BROADCAST','NEWS')
    
