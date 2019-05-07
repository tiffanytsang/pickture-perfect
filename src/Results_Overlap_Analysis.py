import sys
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

def resize(cs_urls, hp_urls):
    if len(hp_urls) < len(cs_urls):
        cs_urls = cs_urls[0: len(hp_urls)]
    else:
        hp_urls = hp_urls[0: len(cs_urls)]
    return (cs_urls, hp_urls)


#returns fraction of overlap
def findOverlap(cs_df, hp_df):
    (cs_df, hp_df) = resize(cs_df, hp_df)
    cs_urls = cs_df.to_dict()["img_url"].values()
    hp_urls = hp_df.to_dict()["img_url"].values()
    overlap = 0
    for url in cs_urls:
        if url in hp_urls:
            overlap += 1
    frac = (float(overlap) / float(len(cs_urls)))
    return frac

def plot_graph(checkbox_data, goodbad_data):
    fig, ax = plt.subplots()
    index = np.arange(6)
    bar_width = 0.35
    rects1 = ax.bar(index, checkbox_data, bar_width, label='Checkbox')
    rects2 = ax.bar(index + bar_width, goodbad_data, bar_width, label='GoodBad')
    t2 = ax.set_title("Percentage of overlap between our favorite photos and crowdworker selected photos")
    ax.set_xticklabels(("", "Budapest", "Singapore", "Greece", "California", "CostaRica", "SouthAfrica"))
    fig.tight_layout()
    ax.legend()
    plt.show()


def main():
    photosets = ["Budapest", "Singapore", "Greece", "California", "CostaRica", "SouthAfrica"]
    checkbox_data = []
    goodbad_data = []
    for set in photosets:
        checkbox_output = './data/Subset_Results/' + set + '_Checkbox.csv'
        good_bad_output = './data/Subset_Results/' + set + '_GoodBad.csv'
        handpicked = './data/our_best_photos/' + set + '_our_best.csv'
        cb_df = pd.read_csv(checkbox_output)
        gb_df = pd.read_csv(good_bad_output)
        hp_df = pd.read_csv(handpicked)
        checkbox_overlap =  findOverlap(cb_df, hp_df)
        goodbad_overlap = findOverlap(gb_df, hp_df)
        checkbox_data.append(checkbox_overlap)
        goodbad_data.append(goodbad_overlap)
    plot_graph(checkbox_data, goodbad_data)


if __name__ == '__main__':
    main()
