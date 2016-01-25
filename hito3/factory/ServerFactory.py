#!/usr/bin/python
# -*- coding: utf-8 -*-

import Ice
Ice.loadSlice('../my_interface.ice --all -I .')
import drobots, sys
from main import *

class ControllerFactoryI(drobots.ControllerFactory):
    def __init__(self, broker, adapter):
        self.broker=broker
        self.adapter=adapter

    def make(self, bot, name, current=None):
        if bot.ice_isA("::drobots::Attacker"):
            rc_servant = RobotControllerAttacker(bot)
        else:
            rc_servant = RobotControllerDefender(bot)
 
        rc_proxy = self.adapter.add(rc_servant, self.broker.stringToIdentity(name))
        return rc_proxy


class ServerFactory(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        adapter = broker.createObjectAdapter("FactoryAdapter")

        servant = ControllerFactoryI(broker, adapter)
        proxy = adapter.add(servant, broker.stringToIdentity("factory1"))

        print(proxy)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


factory = ServerFactory()
sys.exit(factory.main(sys.argv))
