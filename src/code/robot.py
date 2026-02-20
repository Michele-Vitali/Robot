import logging
import threading
from typing import Dict
from dashboard import Dashboard
from componentIF import Component

class Robot:
    # Components is a dict having [Component_name: Component_instance]
    def __init__(self, components: Dict[str, Component]):
        self.components = components
        # We declare a dict where we have name and health status for each component, initialized
        # to UNKOWN.
        self.health_status: Dict[str, str] = {comp_name: "UNKNOWN" for comp_name in components}
        self.dashboard = None

    # Health check for single component (the instance is passed as argument)
    def _check_component(self, comp_instance: Component):
        # We check the health of the component and update the health_status dict accordingly
        current_comp_status = "OK" if comp_instance.check_health() else "FAIL"
        self.health_status[comp_instance.get_name()] = current_comp_status
        self.dashboard.update_health_status(self.health_status)


    # Health check for all components
    def health_check(self) -> bool:
        threads = []
        # We use threads to speed up things and work in parallel without blocking any execution.
        for comp_instance in self.components.values():
            t = threading.Thread(target=self._check_component, args=(comp_instance,))
            t.start()
            threads.append(t)
        
        for t in threads:
            t.join()
        
        return all(status == "OK" for status in self.health_status.values())

    def initialize(self):
        self.dashboard = Dashboard(self.components, self.health_status)
        self.dashboard.start_dashboard()
        logging.info("Starting robot initialization...")
        
        # We initialize each component...
        failed_components = []
        for name, comp_instance in self.components.items():
            try:
                logging.info(f"Initializing {name}...")
                comp_instance.initialize()
            except Exception as e:
                logging.error(f"Failed to initialize {name}: {e}")
                failed_components.append(name)
        
        # If any component failed to initialize...
        if failed_components:
            logging.critical(f"Components failed to initialize: {failed_components}")
            return False
        
        # Now that we have initialized all components, we perform a health check
        # testing each component for their functioning.
        logging.info("Checking component health...")
        if not self.health_check():
            logging.critical("Health check failed after initialization!")
            return False
        
        logging.info("Robot initialized successfully!")
        return True
    
    def stop(self):
        self.dashboard.stop_dashboard()