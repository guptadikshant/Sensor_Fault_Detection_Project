import logging
import os
from datetime import datetime
import sys
from from_root import from_root

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(from_root(), "Project-1_Sensor_Fault_Detection", "sensor", "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    format="[ %(asctime)s ] %(lineno)d  %(module)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    # To print the logs at console. To not print in console remove handlers
    handlers=[logging.StreamHandler(sys.stdout),
              logging.FileHandler(LOG_FILE_PATH)]
)
