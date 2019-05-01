import sys
import pandas as pd

# usage: python GoodBad_Analysis.py [filename.csv]

#returns set of bad worker Ids
def select_unqualified_workers(df):
    worker_set = set()
    for row in df.iterrows():
        row = row[1]
        worker_id = row['WorkerId']

        for i in range(1,11):
            input_img = row['Input.img'+str(i)]
            img_good_answer = row['Answer.img'+str(i)+'.good']
            if input_img.find('neg', input_img.rfind('/')) > -1 and img_good_answer:
                worker_set.add(worker_id)
    return worker_set

#gets score for each image, excluding bad workers
def get_scores(df, unqual):
    photo_score = dict()
    photo_total = dict()
    for row in df.iterrows():
        row = row[1]
        worker_id = row['WorkerId']
        if worker_id in unqual:
            continue

        for i in range(1,11):
            input_img = row['Input.img'+str(i)]
            img_good_answer = row['Answer.img'+str(i)+'.good']
            if img_good_answer:
                photo_score[input_img] = photo_score.setdefault(input_img,0) + 1
            else:
                photo_score[input_img] = photo_score.setdefault(input_img,0) + 0
            photo_total[input_img] = photo_total.setdefault(input_img,0) + 1
    for key, value in photo_score.items():
        photo_score[key] = (photo_score[key]+0.0)/photo_total[key]
    return photo_score

def sorted_urls(urls):
    l = sorted(urls, key=lambda key: urls[key])
    l.reverse()
    return l

def main():
    csv = sys.argv[1]
    filename = '../data/good_bad_input/' + csv
    df = pd.read_csv(filename)
    unqual = select_unqualified_workers(df)
    urls = get_scores(df, unqual)
    out_df = pd.DataFrame(sorted_urls(urls), columns=['img_url'])
    output = '../data/good_bad_output/' + csv.split('_')[0] + '_output.csv'
    out_df.to_csv(output, index=False)
    return

if __name__ == '__main__':
    main()