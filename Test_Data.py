## Loads the pre-selected and manually labeled test images used to train the models

import os
from pathlib import Path

IMAGES_DIR_GOOD = Path("Photos/Test_Set/Good")
IMAGES_DIR_BAD = Path("Photos/Test_Set/Bad")

GOOD_TEST = os.listdir(IMAGES_DIR_GOOD)
BAD_TEST = os.listdir(IMAGES_DIR_BAD)
