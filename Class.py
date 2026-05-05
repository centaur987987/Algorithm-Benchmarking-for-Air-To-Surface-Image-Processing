## Objective:  Generates a class that is used to pull various information 
# for a chosen image

## Variables:
# r = entropy radius
# s = theshold scale
# w = number of white pixels

from pathlib import Path
import cv2
from skimage.filters.rank import entropy
from matplotlib import pyplot as plt
from skimage.morphology import disk

# Create a class "Image" which can complete various actions for said image
class Image:

    # Initialize variables for convenient reference in other classes
    def __init__(self, name: str):
        self.name = name
        self.path = None
        self.label = None
        self.img = None
        self.entropy = None
        self.threshold = None
        self.white = None
        self.all = None

    # print the name of the image
    def get_name(self):
        print(self.name)

    # print the path of the image based on whether or not the name includes "BAD". This requires all bad files to be labeled as such
    def get_path(self):
        if "BAD" in self.name:
            self.path = Path("Photos/Train_Set/Bad")
            self.label = 0
        else:
            self.path = Path("Photos/Train_Set/Good")
            self.label = 1 
        print(self.path / self.name)
        return self.path

    # Create a label for each image. 0 for bad. 1 for good.
    def get_label(self):
        if "BAD" in self.name:
            self.label = 0
        else:
            self.label = 1
        
        return self.label

    # Display the image
    def display(self):
        if "BAD" in self.name:
            self.path = Path("Photos/Train_Set/Bad")
            self.label = 0
        else:
            self.path = Path("Photos/Train_Set/Good")
            self.label = 1 
        print(self.path / self.name)
        full_path = (self.path / self.name).resolve()

        if not full_path.exists():
            print(f"ERROR: File not found at {full_path}")
            return None
        
        self.img = cv2.imread(str(full_path), cv2.IMREAD_GRAYSCALE)
        print(self.img)
        print("pixel count is ", self.img.size)
        #self.img = cv2.medianBlur(self.img, 5)
        plt.figure(1)
        plt.imshow(self.img, cmap = 'gray')
        plt.title('Image')
        plt.show()
        cv2.waitKey(0)
        return self.img

    # Display the entropy of the image
    def get_entropy(self, r):
        self.entropy = entropy(self.img, disk(r))
        plt.figure(1)
        plt.imshow(self.entropy, cmap='magma')
        plt.title('Entropy Image')
        plt.show()
        cv2.waitKey(0)
        return self.entropy
    
    #Display threshold of image
    def get_threshold(self, r, s):
        scaled_entropy = self.img / self.img.max()
        entropy_image = entropy(scaled_entropy, disk(r))
        scaled_entropy = entropy_image / entropy_image.max()
        self.threshold = scaled_entropy < s
        
        plt.imshow(self.threshold, cmap='grey')
        plt.title('Threshold Image')
        plt.show()
        
        self.threshold = self.threshold.flatten()
        
        return self.threshold

    def get_white(self):
        total_white = self.threshold.sum()
        print("The amount of white pixels =", total_white)

        return self.white

    def get_all(self, r, s):
        
        # get path
        if "BAD" in self.name:
            self.path = Path("Photos/Train_Set/Bad")
            self.label = 0
        else:
            self.path = Path("Photos/Train_Set/Good")
            self.label = 1    

        # import image
        self.img = cv2.imread(self.path / self.name, cv2.IMREAD_GRAYSCALE)
        self.img = cv2.medianBlur(self.img, 5)

        # entropy
        scaled_entropy = self.img / self.img.max()
        entropy_image = entropy(scaled_entropy, disk(r))
        scaled_entropy = entropy_image / entropy_image.max()

        # threshold
        self.threshold = scaled_entropy < s

        # determine white pixel count
        total_white = self.threshold.sum()

        return total_white, self.label
    
    def get_all_test(self, r, s):
        # get path
        if "BAD" in self.name:
            self.path = Path("Photos/Test_Set/Bad")
            self.label = 0
        else:
            self.path = Path("Photos/Test_Set/Good")
            self.label = 1    

        # import image
        self.img = cv2.imread(self.path / self.name, cv2.IMREAD_GRAYSCALE)
        self.img = cv2.medianBlur(self.img, 5)

        # entropy
        scaled_entropy = self.img / self.img.max()
        entropy_image = entropy(scaled_entropy, disk(r))
        scaled_entropy = entropy_image / entropy_image.max()

        # threshold
        self.threshold = scaled_entropy < s

        # determine white pixel count
        total_white = self.threshold.sum()

        return total_white, self.label

    def print_images(self, r, s):
        # get path
        if "BAD" in self.name:
            self.path = Path("Photos/Test_Set/Bad")
            self.label = 0
        else:
            self.path = Path("Photos/Test_Set/Good")
            self.label = 1    

        # import image
        self.img = cv2.imread(self.path / self.name, cv2.IMREAD_GRAYSCALE)
        
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
        self.img = clahe.apply(self.img)

        self.img = cv2.medianBlur(self.img, 5)
     
        # entropy
        scaled_entropy = self.img / self.img.max()
        entropy_image = entropy(scaled_entropy, disk(r))
        plt.figure(4)
        plt.imshow(entropy_image, cmap = 'magma')
        plt.title('entropy')
        plt.show()
        cv2.waitKey(0)
        scaled_entropy = entropy_image / entropy_image.max()

        # threshold
        self.threshold = scaled_entropy < s
        plt.figure(5)
        plt.imshow(self.threshold, cmap = 'gray')
        plt.title('threshold')
        plt.show()
        cv2.waitKey(0)
        # determine white pixel count
        total_white = self.threshold.sum()

        return total_white, self.label
