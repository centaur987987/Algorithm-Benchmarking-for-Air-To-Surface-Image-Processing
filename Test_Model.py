## Objective: Using r, s, and w from 
# a model, test the the variables with the test data set

## Variables:
# r = entropy radius
# s = theshold scale
# w = number of white pixels

from Class import Image
from Test_Data import BAD_TEST, GOOD_TEST

# Variable Inputs
r = 6
s = .026634723264151408
w = 38927

#Generate Calibrate List
calibrate_list = BAD_TEST + GOOD_TEST

accuracy_list = []
for img in calibrate_list:
    test = Image(img) # load in Image class for the chosen photo
    [total_white, label] = test.get_all_test(r, s)
    print("label =", label)

    # Generate the match report
    if total_white > w:
        match = 0
    elif total_white < w:
        match = 1
    print("match =", match)

    if match == label:
        accuracy_list.append(1)
    else:
        print(img)
    print(" ")
print("Accuracy = ", len(accuracy_list) / len(calibrate_list) * 100, "%")
  