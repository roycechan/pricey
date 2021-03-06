import schedule
import time
import logging
import os


# Enable logging
logging.basicConfig(
                    filename="logs",
                    filemode='a',
                    format='%(asctime)s - %(module)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    )
logging.getLogger().addHandler(logging.StreamHandler())
logger = logging.getLogger(__name__)


def job():
    logger.info("Scheduled task starting...")
    os.system('python daily_shopee.py')
    os.system('python daily_bot.py')
    logger.info("Scheduled task ended.")


schedule.every().day.at("06:00").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)