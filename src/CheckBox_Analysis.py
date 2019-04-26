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
        good, bad = get_score(row)
        tot_votes = good + bad
        neg = 'neg' in url
        if ((neg and good - bad > 0) or tot_votes > 4):
            worker_set.add(worker_id)
        no_people = row['Answer.radios.noPeople']
        people_checked = row['Answer.checkboxes.7'] or row['Answer.checkboxes.8']
        if (no_people and people_checked):
            worker_set.add(worker_id)
    return worker_set

#returns an (int, int) of good votes, bad votes
def get_score(row):
    good = 0
    bad = 0
    for i in range(1, 9):
        vote = row['Answer.checkboxes.' + str(i)]
        if (vote):
            if (i % 2 == 1):
                good += 1
            else:
                bad += 1
    return good, bad

#gets average score for each image, excluding bad workers
def get_scores(df, unqual):
    urls = {}
    for row in df.iterrows():
        row = row[1]
        worker_id = row['WorkerId']
        if worker_id in unqual:
            continue
        url = row['Input.img_url']
        good, bad = get_score(row)
        if url in urls:
            urls[url][0] += good
            urls[url][1] += bad
        else:
            urls[url] = [good, bad]
    for (k, v) in urls.items():
        urls[k] = (v[0] - v[1] + 1) / (v[1] + 1)
    return urls

def sorted_urls(urls):
    return sorted(urls, key=lambda key: urls[key])

def main():
    filename = '../data/checkbox/' + sys.argv[1]
    df = pd.read_csv(filename)
    unqual = select_unqualified_workers(df)
    urls = get_scores(df, unqual)
    print(sorted_urls(urls))
    return

if __name__ == '__main__':
    main()