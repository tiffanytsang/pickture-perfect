import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

#returns top 25% of the output photos, which is top 5% of all photos
def get_top_5_percent(cb_df, gb_df):
    cb_urls = cb_df.values
    gb_urls = gb_df.values
    size = int(math.floor(max(len(cb_urls), len(gb_urls)) * 0.25))
    s = slice(0, size)
    return (cb_urls[s], gb_urls[s])


#returns fraction of overlap
def findOverlap(cb_urls, gb_urls):
    overlap = 0
    for url in cb_urls:
        if url in gb_urls:
            print(url)
            overlap += 1
    return (float(overlap) / float(len(cb_urls)))

#plots bar graph of country vs. overlap
def plot_graph(series):
    ax = series.plot(kind="bar", rot=0)
    t2 = ax.set_title("Percentage of overlap between final subsets from Checkbox and GoodBad HIT")
    plt.tight_layout()
    plt.show()


def main():
    photosets = ["Budapest", "Singapore", "Greece", "California", "CostaRica", "SouthAfrica"]
    data = {}
    for set in photosets:
        checkbox_output = './data/Subset_Results/' + set + "_Checkbox.csv"
        good_bad_output = './data/Subset_Results/' + set + "_GoodBad.csv"
        cb_df = pd.read_csv(checkbox_output)
        gb_df = pd.read_csv(good_bad_output)
        (cb_df, gb_df) = get_top_5_percent(cb_df, gb_df)
        data[set] = findOverlap(cb_df, gb_df)
    series = pd.Series(data)
    print(series.mean())
    print(series.std())
    plot_graph(series)


if __name__ == '__main__':
    main()
