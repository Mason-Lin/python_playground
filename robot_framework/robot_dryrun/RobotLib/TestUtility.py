import base64
import cv2
from robot.api import logger


def log_snapshot_by_base64(screenshot_path):
    img = cv2.imread(screenshot_path, cv2.IMREAD_UNCHANGED)
    if img is None:
        raise Exception("Image is empty")
    buffer = cv2.imencode('.jpg', img)[1]
    imgdata = base64.b64encode(buffer).decode('ascii')
    logger.info(f'<img src="data:image/jpg;base64,{imgdata}">', html=True)
