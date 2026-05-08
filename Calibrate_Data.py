## Loads the pre-selected and manually labeled training images used to train the models

import os
from pathlib import Path

IMAGES_DIR_GOOD = Path("Photos/Calibrate_Set/Good")
IMAGES_DIR_BAD = Path("Photos/Calibrate_Set/Bad")

GOOD_CALIBRATE = os.listdir(IMAGES_DIR_GOOD)
BAD_CALIBRATE = os.listdir(IMAGES_DIR_BAD)