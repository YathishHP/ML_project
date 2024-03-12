import logging
import os 
from datetime import datetime


LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"# log file name
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)# logpath in current working directory
os.makedirs(logs_path,exist_ok=True)# append the changes

LOG_FILE_path = os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_path,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

