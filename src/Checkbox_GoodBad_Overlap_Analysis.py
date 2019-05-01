import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

#makes sure the output is the same size
def resize(cb_df, gb_df):
    if len(cb_df.index) != len(gb_df.index):
        if len(cb_df.index) > len(gb_df.index):
            cb_df = cb_df.drop(range(len(gb_df.index) + 1, len(cb_df.index)))
        else:
            gb_df = gb_df.drop(range(len(cb_df.index) + 1, len(gb_df.index)))
    return (cb_df, gb_df)

#returns top 20% of the output photos
def get_top_20_percent(cb_df, gb_df):
    cb_urls = cb_df.values
    gb_urls = gb_df.values
    size = int(math.floor(max(len(cb_urls), len(gb_urls)) * 0.2))

    s = slice(0, size)
    return (cb_urls[s], gb_urls[s])


def findOverlap(cb_urls, gb_urls):
    overlap = 0
    for url in cb_urls:
        if url in gb_urls:
            overlap += 1
    return (float(overlap) / float(len(cb_urls)))

def plot_graph(data):
    series = pd.Series(data)
    ax = series.plot(kind="bar")
    t2 = ax.set_title("Percentage of overlap between Checkbox and GoodBad HIT")
    plt.tight_layout()
    plt.show()


def main():
    photosets = ["Budapest", "California", "CostaRica", "Greece", "Singapore", "SouthAfrica"]
    data = {}
    for set in photosets:
        checkbox_output = '/Users/killenberge/pickture-perfect/data/checkbox_output/' + set + "_output.csv"
        good_bad_output = '/Users/killenberge/pickture-perfect/data/good_bad_output/' + set + "_output.csv"
        cb_df = pd.read_csv(checkbox_output)
        gb_df = pd.read_csv(good_bad_output)
        (cb_df, gb_df) = get_top_20_percent(cb_df, gb_df)
        data[set] = findOverlap(cb_df, gb_df)
    print(data)
    plot_graph(data)


if __name__ == '__main__':
    main()
