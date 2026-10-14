"""
Launcher script for JobPulse AI Web Interface.
Starts uvicorn and opens http://127.0.0.1:8000 in your default browser.
"""
import webbrowser
import threading
import time
import sys
import uvicorn

def open_browser():
    time.sleep(1.2)
    print("\n[JobPulse AI] Opening web interface in browser: http://127.0.0.1:8000 ...")
    webbrowser.open("http://127.0.0.1:8000")

if __name__ == "__main__":
    print("=" * 65)
    print("  JobPulse AI — Venu's Job Search & ATS Matcher Web Application")
    print("  Host: http://127.0.0.1:8000")
    print("=" * 65)
    
    # Auto-open browser in background thread
    threading.Thread(target=open_browser, daemon=True).start()
    
    try:
        uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True, log_level="info")
    except KeyboardInterrupt:
        print("\n[JobPulse AI] Server stopped.")
        sys.exit(0)
