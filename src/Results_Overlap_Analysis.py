import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

#returns top 5% of the output photos
def get_top_5_percent(cb_df, gb_df):
    cb_urls = cb_df.values
    gb_urls = gb_df.values
    size = int(math.floor(max(len(cb_urls), len(gb_urls)) * 0.05))
    s = slice(0, size)
    return (cb_urls[s], gb_urls[s])


#returns fraction of overlap
def findOverlap(cs_urls, hp_urls):
    overlap = 0
    if len(cs_urls) == 0 or len(hp_urls) == 0: return overlap
    for url in cs_urls:
        print(url)
        if url in hp_urls:
            overlap += 1
    return (float(overlap) / float(len(cs_urls)))

#plots bar graph of country vs. overlap
def plot_graph(series):
    ax = series.plot(kind="bar", rot=0)
    t2 = ax.set_title("Percentage of overlap between Crowdsourced and Hand-selected Best Photos")
    plt.tight_layout()
    plt.show()


def main():
    photosets = ["Budapest", "Singapore", "Greece", "California", "CostaRica", "SouthAfrica"]
    data = {}
    for set in photosets:
        checkbox_output = './data/Subset_Results/' + set + '_Checkbox.csv'
        good_bad_output = './data/Subset_Results/' + set + '_GoodBad.csv'
        handpicked = './data/our_best_photos/' + set + '_our_best.csv'
        cb_df = pd.read_csv(checkbox_output)
        gb_df = pd.read_csv(good_bad_output)
        hp_df = pd.read_csv(handpicked)
        (cb_df, gb_df) = get_top_5_percent(cb_df, gb_df)
        checkbox_overlap =  findOverlap(cb_df, hp_df)
        good_bad_overlap = findOverlap(gb_df, hp_df)
        data[set] = {"checkbox": checkbox_overlap, "good_bad": good_bad_overlap}
    series = pd.Series(data)
    print(series.mean())
    print(series.std())
    plot_graph(series)


if __name__ == '__main__':
    main()
