# play_sound.py

import os
import threading
from playsound import playsound

def play_wrong_sound():
    """
    Play the wrong-answer MP3 in a fire-and-forget thread.
    No windows, no blocking.
    """
    sound_path = os.path.abspath("assets/sounds_heartbeat.mp3")
    if not os.path.isfile(sound_path):
        raise FileNotFoundError(f"Sound file not found: {sound_path}")

    # Thread target
    def _player():
        try:
            playsound(sound_path)
        except Exception as ex:
            # You can log or handle playback errors here
            print("Playback error:", ex)

    # Start daemon thread (won’t prevent your app from exiting)
    threading.Thread(target=_player, daemon=True).start()

if __name__ == "__main__":
    # Quick test: plays the sound, then waits so you can hear it.
    play_wrong_sound()
    #input("Press Enter to exit…")