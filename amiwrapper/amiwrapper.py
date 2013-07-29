from termprint import *
from starpy import manager
from twisted.internet import reactor
import sys, logging
import settings

i, e, w = "INFO", "ERROR", "WARNING"

class AMIWrapper(object):
    """ Base class wrapper file for call originating with starpy """

    user = getattr(settings, "AMI_USER")
    pwd = getattr(settings, "AMI_PASS")
    host = getattr(settings, "PBX")
    command_txt = None
    response = None

    allowed_keys = ['user', 'pwd', 'host', 'command_txt', 'response']
    def __init__(self, **kwargs):
        """ Set the credentials or stop the reactor """
        if not self.host or not self.user or not self.pwd:
            raise Exception("No credentials found")
            self.__stop_reactor()
            sys.exit()

        for k, v in kwargs.items():
            if k in self.allowed_keys:
                setattr(self, k, v)
    
    # privates
    def __stop_reactor(self):
        """ Attempt to stop the reactor so the
        application can terminate.
        """
        try:
            reactor.stop()
        except:
            termprint(e, "Failed to stop reactor")
            pass

    def __run_reactor(self, method):
        """ Start and run the reactor """
        reactor.callWhenRunning(method)
        reactor.run()

    def __exception(self, msg, exit=True):
        """ Print any errors and exit """
        termprint(e, msg)
        self.__stop_reactor()
        sys.exit()

    def __set_session(self):
        self.session = manager.AMIFactory(self.user, self.pwd)
        return self.__get_session()

    def __get_session(self):
        """ Get the session from self.session safely """
        return getattr(self, "session", None)



if __name__ == '__main__':
    #manager.log.setLevel(logging.DEBUG)

    # send a command
    cl = AMIWrapper(command="dialplan show from-internal")
    reactor.callWhenRunning(cl.command)
    reactor.run()


