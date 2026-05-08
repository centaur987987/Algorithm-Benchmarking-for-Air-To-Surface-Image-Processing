## Objective: Optimize r, s, and w, with a regression model.
#
## Variables:
# r = entropy radius
# s = theshold scale
# w = number of white pixels
# X = input feature
# y = target label

import time
from skopt import BayesSearchCV
from sklearn.base import BaseEstimator
from Class import Image
from Calibrate_Data import BAD_CALIBRATE, GOOD_CALIBRATE

import pandas as pd
import plotly.express as px

# Initial Setup
class AI_Regression(BaseEstimator):
    def __init__(self, r=3, s=0.1, w=50000):
        self.r = r
        self.s = s
        self.w = w
        
    def fit(self, X, y=None): # need to keep format with the "BayesSearchCV format"
        return self
    
    def score(self, X, y):
        # Objective Function
        match_report = []
        for img_path in X:
            test = Image(img_path)
            total_white, _ = test.get_all(self.r, self.s)
            if total_white > self.w:
                match_report.append(0)
            else:
                match_report.append(1)
        
        # Calculate accuracy
        return sum(1 for i, j in zip(match_report, y) if i == j) / len(y)

# Setup Data
calibrate_list = BAD_CALIBRATE + GOOD_CALIBRATE
Labels = [Image(img).get_label() for img in calibrate_list]

# Complete Regression
Range = {
    'r': (1, 9),        # Range for entropy radius
    's': (0.01, 1.0),    # Range for threshold scale
    'w': (10000, 90000) # Range for white pixels
}

# Start Time
start_time = time.perf_counter()

opt = BayesSearchCV(
    AI_Regression(),
    Range,
    n_iter = 15, # test 15 combinations based on 'Regression_Iteration_Test.py'
    random_state = 0
)

opt.fit(calibrate_list, Labels)

# end time
end_time = time.perf_counter()
run_time = end_time - start_time

# print results
print('Good Variables are:', opt.best_params_)
print(f"Runtime: {run_time:.2f} seconds")

### PLOT CODE
# 1. Extract results into a DataFrame
results = pd.DataFrame(opt.cv_results_)

# 2. Extract hyperparameters and mean test score
# BayesSearchCV prefixes param names with 'param_'
df_plot = pd.DataFrame({
    'r': results['param_r'],
    's': results['param_s'],
    'w': results['param_w'],
    'Accuracy': results['mean_test_score']
})

# 3. Create the interactive 3D Scatter Plot
MY_COLOR_SCALE = 'Viridis' # or 'RdYlGn'
MY_RANGE = [0, 1]          # Forces 0% to 100% accuracy scale
fig = px.scatter_3d(
    df_plot, 
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