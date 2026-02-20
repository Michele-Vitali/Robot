import time
import threading
from typing import Dict
from componentIF import Component

class Dashboard:
    def __init__(self, components: Dict[str, Component], health_status: Dict[str, str]):
        self.components = components
        self.health_status = health_status
        self._stop_dashboard = False


    def start_dashboard(self, refresh_rate: float = 0.5):
        def dashboard_loop():
            while not self._stop_dashboard:
                self.print_dashboard()
                time.sleep(refresh_rate)

        self._dashboard_thread = threading.Thread(target=dashboard_loop, daemon=True)
        self._dashboard_thread.start()

    def stop_dashboard(self):
        self._stop_dashboard = True
        if hasattr(self, '_dashboard_thread'):
            self._dashboard_thread.join()
    
    def print_dashboard(self):
        print("\033[H\033[J", end="") # To clear the screen
        print("="*30 + " MiRobot Dashboard " + "="*30)
        for comp_name in self.components:
            status = self.health_status.get(comp_name, "UNKNOWN")
            symbol = "✅" if status == "OK" else "❌" if status == "FAIL" else "❓"
            info = self.components[comp_name].get_status_info()
            print(f"{comp_name:<15} | {status:<4} | {symbol} | {info}")
        print("="*75)

    def update_health_status(self, health_status: Dict[str, str]):
        self.health_status.update(health_status)

    def initialize(self):
        self.start_dashboard()