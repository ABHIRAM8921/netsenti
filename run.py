import threading
import uvicorn
from core.log_monitor import start_monitor

def start_api():
    uvicorn.run("api.main:app", host="0.0.0.0", port=8000, reload=False)

if __name__ == "__main__":
    print("Starting NetSentinel...")

    # Start log monitor in separate thread
    monitor_thread = threading.Thread(target=start_monitor)
    monitor_thread.daemon = True
    monitor_thread.start()

    # Start FastAPI server
    start_api()
