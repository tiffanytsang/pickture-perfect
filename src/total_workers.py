#!/usr/bin/env python

import pandas as pd

cb_files = ["Budapest_Checkbox.csv", "California_Checkbox.csv",
    "CostaRica_Checkbox.csv", "Greece_Checkbox.csv",
    "Singapore_Checkbox.csv", "SouthAfrica_Checkbox.csv"]

gb_files = ["Budapest_GoodBad.csv", "California_GoodBad.csv",
    "CostaRica_GoodBad.csv", "Greece_GoodBad.csv",
    "Singapore_GoodBad.csv", "SouthAfrica_GoodBad.csv"]

places = ['Budapest', 'Singapore', 'California', 'Greece', 'CostaRica', 'SouthAfrica']
gb_subset = [('../data/Subset_Data/Qualtrics_Output/' + place + '_GoodBad.csv') for place in places]
cb_subset = [('../data/Subset_Data/Qualtrics_Output/' + place + '_Checkbox.csv') for place in places]

def make_df (filenames, prefix):
    li = []
    for filename in filenames:
        df = pd.read_csv(prefix + filename)
        li.append(df)
    return pd.concat(li, axis=0)

cb_df = make_df(cb_files, '../data/checkbox_input/')
gb_df = make_df(gb_files, '../data/good_bad_input/')
subset_df = make_df(gb_subset + cb_subset, '')

cb_workers = list(cb_df.WorkerId.unique())
gb_workers = list(gb_df.WorkerId.unique())
subset_workers = list(subset_df.Q1.unique())

worker_count = len(set(cb_workers + gb_workers + subset_workers))
print('total workers: ' + str(worker_count))