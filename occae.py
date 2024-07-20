from apscheduler.schedulers.background import BackgroundScheduler
import time

def check_system_status():
    print("Checking system status...")

scheduler = BackgroundScheduler()
scheduler.add_job(check_system_status, 'interval', seconds=60)
scheduler.start()

try:
    # Keep the script running to allow scheduled jobs to execute
    while True:
        time.sleep(2)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
