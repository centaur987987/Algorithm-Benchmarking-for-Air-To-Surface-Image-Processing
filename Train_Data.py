## Loads the pre-selected and manually labeled training images used to train the models

import os
from pathlib import Path

IMAGES_DIR_GOOD = Path("Photos/Train_Set/Good")
IMAGES_DIR_BAD = Path("Photos/Train_Set/Bad")

GOOD_TRAIN = os.listdir(IMAGES_DIR_GOOD)
BAD_TRAIN = os.listdir(IMAGES_DIR_BAD)