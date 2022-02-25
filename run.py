from website import run
from FlightTracker import FlightTracker
import threading
import config

if __name__ == "__main__":
    tracker = FlightTracker(config.ICAO)

    website = threading.Thread(target=run)
    tracker = threading.Thread(target=tracker.locate)

    website.start()
    tracker.start()
