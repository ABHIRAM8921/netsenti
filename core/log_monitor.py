from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from core.feature_engine import process_log

ZEEK_LOG_PATH = "/opt/zeek/logs/current/conn.log"

class ZeekHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("conn.log"):
            print("New traffic detected...")
            process_log(ZEEK_LOG_PATH)

def start_monitor():
    event_handler = ZeekHandler()
    observer = Observer()
    observer.schedule(event_handler, path="/opt/zeek/logs/current/")
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
