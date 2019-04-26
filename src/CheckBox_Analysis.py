import sys
import pandas as pd

# usage: python CheckBox_Analysis.py

#returns set of bad worker Ids
def select_unqualified_workers(df):
    worker_set = set()
    for row in df.iterrows():
        row = row[1]
        worker_id = row['WorkerId']
        url = row['Input.img_url']
        score, count = get_score(row)
        neg = 'neg' in url
        if ((neg and score > 0) or count > 4):
            worker_set.add(worker_id)
        no_people = row['Answer.radios.noPeople']
        people_checked = row['Answer.checkboxes.7'] or row['Answer.checkboxes.8']
        if (no_people and people_checked):
            worker_set.add(worker_id)
    return worker_set

#returns an (int, int) of score, number of Trues
def get_score(row):
    score = 0
    count = 0
    for i in range(1, 9):
        vote = row['Answer.checkboxes.' + str(i)]
        if (vote):
            if (i % 2 == 1):
                score += 1
            else:
                score -= 1
            count += 1
    return score, count

#gets average score for each image, excluding bad workers
def get_scores(df, unqual):
    urls = {}
    for row in df.iterrows():
        row = row[1]
        worker_id = row['Input.WorkerId']
        if worker_id in unqual:
            continue
        url = row['Input.img_url']
        score = get_score(row)
        if url in urls:
            urls[url] += score
        else:
            urls[url] = score
    return urls

def main():
    filename = '../data/checkbox/' + sys.argv[1]
    df = pd.read_csv(filename)
    print(select_unqualified_workers(df))
    return

if __name__ == '__main__':
    main()