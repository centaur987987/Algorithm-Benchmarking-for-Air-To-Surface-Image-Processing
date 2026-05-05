## Objective: This is the code for Grid search which represents the 
# logic of the work completed for the work project

## Variables:
# r = entropy radius
# s = theshold scale
# w = number of white pixels

import time
from Class import Image
from Train_Data import BAD_TRAIN, GOOD_TRAIN
from Generate_Grid import Gen_Grid
import pandas as pd
import plotly.express as px

# Start Time
start_time = time.perf_counter()

# Generate Combinations from Gen_Grid
combinations = Gen_Grid()

# Print combinations for reference
print('\n There are', len(combinations), 'combinations to be tested \n')

# Choose training set
train_list = BAD_TRAIN + GOOD_TRAIN # just using 2 for now
Good_Match_Report = [] # placeholder, need to fill in with better way of finding this
test = train_list[0]

# Generate the correct match report
for img in train_list:
    label = Image(img)
    #label.display() # display the original images when wanted
    label = label.get_label()
    Good_Match_Report.append(label)
    
    
print("The ideal match report is: ", Good_Match_Report)
Good_Report_List = []
plot_data = []
for r, s, w in combinations:
    match_report = []
    for img in train_list:
        
        test = Image(img) # load in Image class for the chosen photo    
        total_white, _ = test.get_all(r, s)
        # Generate the match report
        if total_white > w:
            match_report.append(0)
        elif total_white < w:
            match_report.append(1)
        
    print("\nFor a combination of entropy radius =", r, ", scale =", s, "and match val =", w)
    print("Match Report:", match_report)
    
    # Compare Match Reports
    if Good_Match_Report == match_report:
        Good_Report_List.append([r, s, w])

    # Calculate accuracy for this specific r, s, w combo
    correct_guesses = sum(1 for i, j in zip(match_report, Good_Match_Report) if i == j)
    accuracy = correct_guesses / len(Good_Match_Report)
    
    # Store for the plot
    plot_data.append({'r': r, 's': s, 'w': w, 'Accuracy': accuracy})
end_time = time.perf_counter()
run_time = end_time - start_time
print('Good Variables are:', Good_Report_List)
print(f"Runtime: {run_time:.6f} seconds")

# 2. Convert to DataFrame and Plot
df = pd.DataFrame(plot_data)
# Shared color settings
MY_COLOR_SCALE = 'Viridis' # or 'RdYlGn'
MY_RANGE = [0, 1]          # Forces 0% to 100% accuracy scale
fig = px.scatter_3d(
    df, 
    x='r', y='s', z='w',
    color='Accuracy',
    # --- ADD THESE TWO LINES ---
    color_continuous_scale=MY_COLOR_SCALE,
    range_color=MY_RANGE, 
    # ---------------------------
    title='Hyperparameter Accuracy Map',
    labels={'r': 'Radius', 's': 'Scale', 'w': 'White Pixels'}
)

fig.show()