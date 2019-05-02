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


def reasons_for_rejection(df, dict):

    for row in df.iterrows():
        row = row[1]
        url = row['Input.img_url']
        good, bad = get_score(row)
        tot_votes = good + bad
        neg = 'neg' in url
        if (neg and good - bad > 0):
            dict["Negative as Good"] += 1
        if tot_votes > 4:
            dict["More Than 4 Checked"] += 1
        no_people = row['Answer.radios.noPeople']
        people_checked = row['Answer.checkboxes.7'] or row['Answer.checkboxes.8']
        if (no_people and people_checked):
            dict["People Discrepancy"] += 1;


def main():
    files = ["Budapest_Checkbox.csv", "California_Checkbox.csv",
    "CostaRica_Checkbox.csv", "Greece_Checkbox.csv",
    "Singapore_Checkbox.csv", "SouthAfrica_Checkbox.csv"]
    d = {}
    reasons_dict = {}
    reasons_dict["More Than 4 Checked"] = 0
    reasons_dict["Negative as Good"] = 0
    reasons_dict["People Discrepancy"] = 0

    for file in files:
        input = '../data/checkbox_input/' + file
        df = pd.read_csv(input)
        pct = get_unqualified_pct(df)
        d[file] = pct
        reasons_for_rejection(df, reasons_dict)

    print(d)
    sizes = [50, 220, 360, 220, 50, 440]
    #print(d.values())
    dqdf = pd.DataFrame(list(zip(d.values(), sizes)),
        columns=['percentages','sizes'])
    print(dqdf.corr())
    #print(reasons_dict)

    total_dq = sum(reasons_dict.values())
    reasons_dict2 = {k:v/total_dq for k,v in reasons_dict.items()}
    print(reasons_dict2)
    reasons_series = pd.Series(reasons_dict2)
    reasons_ax = reasons_series.plot.pie(label="",autopct='%1.1f%%')
    t1 = reasons_ax.set_title("Breakdown of Reasons for Disqualification for Checkbox HIT")

    # Uncomment to graph percentages of workers disqualified
    # d1 = {k[:-13]:v for k,v in d.items()}
    # series = pd.Series(d1)
    # mean = series.mean()
    # std = series.std()
    # print("Mean: " + str(mean))
    # print("Standard Deviation: " + str(std))
    #
    #
    # ax = series.plot(kind="bar")
    # t2 = ax.set_title("Percentage of Workers Disqualified in CheckBox HIT")
    plt.tight_layout()
    plt.show()





if __name__ == '__main__':
    main()
