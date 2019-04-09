import pandas as pd
import csv

# returns a list 
def find_unqualified(df):
  unqualified = set()
  for row in df.iterrows():
    row = row[1]
    neg1 = row["NegImg1"]
    neg2 = row["NegImg2"]
    worker = row["WorkerID"]
    for i in range(1, 8):
      rank = row["Rank" + str(i)]
      if rank == neg1 or rank == neg2:
        unqualified.add(worker)

  # write bad workers to csv
  with open('../data/HIT3/hit3unqualifiedworkers.csv', 'w') as f:
    writer = csv.writer(f,delimiter=',')
    writer.writerow(['WorkerID'])
    for bad_worker in unqualified:
      writer.writerow([bad_worker])

  return bad_workers

def main():
  hit3_data = pd.read_csv('../data/HIT3/hit3dummy.csv')
  bad_workers = identify_bad_workers(hit3_data)

if __name__ == '__main__':
  main()

