import logging
import os
from datetime import datetime

LOG_LIFE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_LIFE)
os.makedirs(logs_path,exist_ok=True)

LOG_LIFE_PATH=os.path.join(logs_path,LOG_LIFE)

logging.basicConfig(
    filename=LOG_LIFE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s %(message)s ",
    level=logging.INFO,


)
