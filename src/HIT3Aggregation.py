import pandas as pd
import csv

# returns a list of image IDs/URLs sorted based on 
# average ranking amongst all qualified workers
# also writes top image to csv
def get_ranked_images(df, bad_workers):
  #create set of unqualified workers
  unqual = set()
  for row in bad_workers.iterrows():
    row = row[1]
    unqual.add(row['WorkerID'])

  #create dict of image URL to rating
  pictures = {}
  for row in df.iterrows():
    row = row[1]
    if row['WorkerID'] not in unqual:
      for i in range(1, 11):
        url = int(row['Rank' + str(i)])
        if url not in pictures:
          pictures[url] = [i, 1] # sum, count
        else:
          pictures[url][0] += i
          pictures[url][1] += 1
  for (url, v) in pictures.items():
    pictures[url] = v[0] / v[1]
  
  #get list of picturs sorted by average rank
  ranked_pictures = sorted(pictures, key=pictures.get)

  #write top picture to csv
  with open('../data/HIT3/hit3bestphoto.csv', 'w') as f:
    writer = csv.writer(f,delimiter=',')
    writer.writerow(['BestPhoto'])
    writer.writerow([ranked_pictures[0]])

  return ranked_pictures


def main():
  hit3_data = pd.read_csv('../data/HIT3/hit3dummy.csv')
  bad_workers = pd.read_csv('../data/HIT3/hit3unqualifiedworkers.csv')
  ranked_images = get_ranked_images(hit3_data, bad_workers)

if __name__ == '__main__':
  main()

