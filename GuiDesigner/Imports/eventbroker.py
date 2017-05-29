import sys
def output(param):
    sys.stdout.write(param+'\n')


class EventBroker():
    def __init__(self):
        self._dictionary_ = {}
 
    def subscribe(self,message_id,callback):
        if message_id in self._dictionary_:
            output('EventBroker: callback already defined for message id: {}\nThe callback before will be overwritten'.format(message_id))

        self._dictionary_[message_id] = callback
 
    def publish(self,message_id,*args,**kwargs):
        if message_id not in self._dictionary_:
            output('EventBroker: no callback defined for message: {},{},{}'.format(message_id,args,kwargs))
        else:
            self._dictionary_[message_id](*args,**kwargs)
     
