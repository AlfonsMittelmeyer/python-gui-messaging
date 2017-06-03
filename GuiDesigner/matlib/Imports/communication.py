from Imports.eventbroker import EventBroker

_eventbroker = EventBroker()
publish = _eventbroker.publish
subscribe = _eventbroker.subscribe
