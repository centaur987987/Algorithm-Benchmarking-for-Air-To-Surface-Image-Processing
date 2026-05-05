## Objective: Generate the variable combinations required for Grid Search

import itertools

def Gen_Grid():
    val = [round(i * 1 + 1, 2) for i in range(0, 9)]
    scale = [round(i * 0.1 + 0.1, 2) for i in range(0, 9)]
    match_val = [round(i * 10000 + 10000, 2) for i in range(0, 9)]
    combinations = list(itertools.product(val, scale, match_val))

    return combinations
