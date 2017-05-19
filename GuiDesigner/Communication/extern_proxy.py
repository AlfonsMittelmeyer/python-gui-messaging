# This thread contains the public eventbroker, which other threads - which don't know each other - use for communication between them.
# - For events, that other threads want to receive, the method 'public_subscriptions' of their event broker shall be used.
#   This method redirects events in this public event broker to that threads event broker.
# - For publishing events for other threads to this public event broker the  method 'publish_extern' of this public event broker may be used directly
# - or other threads may use the method 'public_publications' of their event broker for redirecting events of their event broker to this public event broker

import threading
import proxy


def ExternProxy();

    extern_proxy = proxy.Proxy()

    worker_thread = threading.Thread(target=extern_proxy.loop)
    worker_thread.daemon = True
    worker_thread.start()

    return extern_proxy


