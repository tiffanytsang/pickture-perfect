import sys
import pandas as pd
import numpy as np

def resize(cb_df, gb_df):
    if len(cb_df.index) != len(gb_df.index):
        if len(cb_df.index) > len(gb_df.index):
            cb_df = cb_df.drop(range(len(gb_df.index) + 1, len(cb_df.index)))
        else:
            gb_df = gb_df.drop(range(len(cb_df.index) + 1, len(gb_df.index)))
    return (cb_df, gb_df)

def findOverlap(cb_df, gb_df):
    cb_urls = cb_df.values
    gb_urls = gb_df.values
    print(cb_urls, gb_urls)
    overlap = 0
    for url in cb_urls:
        if url in gb_urls:
            print("cb", np.where(url == cb_urls))
            print("gb", np.where(url == gb_urls))
            overlap += 1
    print(overlap, len(cb_urls))


def main():
    filename = sys.argv[1]
    checkbox_output = '/Users/killenberge/pickture-perfect/data/checkbox_output/' + filename
    good_bad_output = '/Users/killenberge/pickture-perfect/data/good_bad_output/' + filename
    cb_df = pd.read_csv(checkbox_output)
    gb_df = pd.read_csv(good_bad_output)
    (cb_df, gb_df) = resize(cb_df, gb_df)
    findOverlap(cb_df, gb_df)

if __name__ == '__main__':
    main()
