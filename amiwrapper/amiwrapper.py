from termprint import *
from starpy import manager
from twisted.internet import reactor
import sys, logging
try:
    import settings
    user = getattr(settings, "AMI_USER")
    pwd = getattr(settings, "AMI_PASS")
    host = getattr(settings, "PBX")
except ImportError:
    host, user, pwd = "", "", ""

i, e, w = "INFO", "ERROR", "WARNING"

class AMIWrapper(object):
    """ Base class wrapper file for call originating with starpy """
    host = host
    user = user
    pwd = pwd

    response = None

    def __init__(self, **kwargs):
        """ Set the credentials or stop the reactor """
        for k, v in kwargs.items():
            setattr(self, k, v)
    
        if not self.host or not self.user or not self.pwd:
            raise Exception("No credentials found")
            self.__stop_reactor()
            sys.exit()

    def stop_reactor(self):
        """ Attempt to stop the reactor so the
        application can terminate.
        """
        try:
            reactor.stop()
        except:
            termprint(e, "Failed to stop reactor")
            pass

    def run_reactor(self, method):
        """ Start and run the reactor """
        reactor.callWhenRunning(method)
        reactor.run()

    def exception(self, msg, exit=True):
        """ Print any errors and exit """
        termprint(e, msg)
        self.stop_reactor()
        sys.exit()

    def set_session(self):
        self.session = manager.AMIFactory(self.user, self.pwd)
        return self.get_session()

    def get_session(self):
        """ Get the session from self.session safely """
        return getattr(self, "session", None)



