#!/usr/bin/env python

import pandas as pd

cb_files = ["Budapest_Checkbox.csv", "California_Checkbox.csv",
    "CostaRica_Checkbox.csv", "Greece_Checkbox.csv",
    "Singapore_Checkbox.csv", "SouthAfrica_Checkbox.csv"]

gb_files = ["Budapest_GoodBad.csv", "California_GoodBad.csv",
    "CostaRica_GoodBad.csv", "Greece_GoodBad.csv",
    "Singapore_GoodBad.csv", "SouthAfrica_GoodBad.csv"]

def make_df (filenames, prefix):
    li = []
    for filename in filenames:
        df = pd.read_csv(prefix + filename)
        li.append(df)
    return pd.concat(li, axis=0)

cb_df = make_df(cb_files, '../data/checkbox_input/')
gb_df = make_df(gb_files, '../data/good_bad_input/')

cb_workers = list(cb_df.WorkerId.unique())
gb_workers = list(gb_df.WorkerId.unique())

worker_count = len(set(cb_workers + gb_workers))
print('total workers: ' + str(worker_count))