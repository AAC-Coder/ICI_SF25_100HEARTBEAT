# countdown_with_heartbeat.py

import flet as ft
import asyncio
import subprocess
import sys
import os



class Countdown(ft.Text):
    def __init__(self, seconds: int, heartbeat_script: str = "heartbeat.py", style=None, ref=None):
        super().__init__(value=str(seconds), style=style, ref=ref)
        self.seconds = seconds
        self.heartbeat_script = heartbeat_script

    def did_mount(self):
        # start the async loop
        self.running = True
        self.page.run_task(self._update_timer)

    def will_unmount(self):
        self.running = False

    async def _update_timer(self):
        # locate your heartbeat.py next to this script
        script_path = os.path.join(os.path.dirname(__file__), self.heartbeat_script)

        while self.running and self.seconds > 0:
            await asyncio.sleep(1)
            # 1. Decrement and update UI
            self.seconds -= 1
            self.value = str(self.seconds)
            self.update()

            # 2. Fire off heartbeat.py in a non-blocking way
            if os.path.isfile(script_path):
                # Use the same Python interpreter
                subprocess.Popen(
                    [sys.executable, script_path],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                )
            else:
                print(f"heartbeat script not found at: {script_path}")

        # When countdown ends
        if self.running:
            self.value = "⏰ Time's up!"
            self.update()

def main(page: ft.Page):
    page.title = "Async Countdown + Heartbeat"
    # Pass your heartbeat filename here if it's different
    page.add(Countdown(seconds=100, heartbeat_script="heartbeat.py"))

if __name__ == "__main__":
    ft.app(target=main)