import pandas as pd
from CheckBox_Analysis import get_score


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
    return len(bad_set)/len(total_workers)

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

if __name__ == '__main__':
    main()
