import logging
import os
from datetime import datetime

LOG_FILE = datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".log"
log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)
log_file_path =  os.path.join(log_path,LOG_FILE)



logging.basicConfig(
    filename= log_file_path,
    format="{asctime} - {levelname} - {message}",
    style="{",
    level = logging.INFO
)