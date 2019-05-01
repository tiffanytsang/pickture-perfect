import pandas as pd
from CheckBox_Aggregation import get_score
import matplotlib.pyplot as plt


def get_unqualified_pct(df):
    bad_set = set()
    total_workers = set()
    for row in df.iterrows():
        row = row[1]
        worker_id = row['WorkerId']
        total_workers.add(worker_id)
        url = row['Input.img_url']
        good, bad = get_score(row)
        tot_votes = good + bad
        neg = 'neg' in url
        if ((neg and good - bad > 0) or tot_votes > 4):
            bad_set.add(worker_id)
        no_people = row['Answer.radios.noPeople']
        people_checked = row['Answer.checkboxes.7'] or row['Answer.checkboxes.8']
        if (no_people and people_checked):
            bad_set.add(worker_id)
    return round(len(bad_set)/len(total_workers) * 100, 4)

def main():
    files = ["Budapest_Checkbox.csv", "California_Checkbox.csv",
    "CostaRica_Checkbox.csv", "Greece_Checkbox.csv",
    "Singapore_Checkbox.csv", "SouthAfrica_Checkbox.csv"]
    d = {}
    for file in files:
        input = '../data/checkbox_input/' + file
        df = pd.read_csv(input)
        pct = get_unqualified_pct(df)
        d[file] = pct
    print(d)



    d1 = {k[:-13]:v for k,v in d.items()}
    series = pd.Series(d1)
    mean = series.mean()
    std = series.std()
    print("Mean: " + str(mean))
    print("Standard Deviation: " + str(std))


    ax = series.plot(kind="bar")
    t2 = ax.set_title("Percentage of Workers Disqualified in CheckBox HIT")
    plt.tight_layout()
    plt.show()





if __name__ == '__main__':
    main()
