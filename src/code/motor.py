import logging
import time

from componentIF import Component


class Motor(Component):
    def __init__(self, name: str):
        self.name = name
        self._initialized = False
        self.current_pwm = 0

    def initialize(self) -> bool:
        self._initialized = True
        self.current_pwm = 0
    
    def check_health(self) -> bool:
        try:
            if not self._initialized:
                raise RuntimeError("Motor not initialized")
            
            time.sleep(0.5) # Simulate initialization time
            return True
        except Exception as e:
            logging.error(f"Motor {self.name} failed to initialize: {e}")
            return False
        
    def get_name(self) -> str:
        return self.name

    def get_status_info(self) -> str:
        return f"PWM: {self.current_pwm}%"
    
    def set_pwm(self, pwm: int):
        self.current_pwm = pwm