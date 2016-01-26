// -*- mode:c++ -*-
#include "drobots.ice"

module drobots {

    dictionary<string, Object*> ObjectPrxDict;
    
    interface Container {
        void link(string key, Object* proxy);
        void unlink(string key);
        ObjectPrxDict list();
    };   

    interface ControllerFactory {
        drobots::RobotController* make(drobots::Robot* bot, Container* container);
    };

    interface RobotControllerAttacker extends drobots::RobotController{ };
	interface RobotControllerDefender extends drobots::RobotController{ };
   
};
