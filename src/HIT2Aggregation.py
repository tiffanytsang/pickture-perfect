import pandas as pd
import csv

#Choose the best photo
def aggregate_data(hit2_data, bd):

	bad_workers = set()

	for index, row in bd.iterrows():
		bad_workers.add(row['WorkerID'])
  
	photo_score = dict()

	for index, row in hit2_data.iterrows():
		photo_score[row['Chosen1']] = photo_score.setdefault(row['Chosen1'],0) + 1
		photo_score[row['Chosen2']] = photo_score.setdefault(row['Chosen2'],0) + 1
		photo_score[row['Chosen3']] = photo_score.setdefault(row['Chosen3'],0) + 1
	
	best_photo = -1
	max_score = 0

	for key, value in photo_score.items():
		if value > max_score:
			max_score = value
			best_photo = key

	#write best photo to csv
	with open('../data/HIT2/hit2bestphoto.csv', 'w') as f:
		writer = csv.writer(f,delimiter=',')
		writer.writerow(['BestPhoto'])
		writer.writerow([best_photo])

	return best_photo

def main():
	hit2_data = pd.read_csv('../data/HIT2/hit2dummy.csv')
	bad_workers = pd.read_csv('../data/HIT2/hit2unqualifiedworkers.csv')
	best_photo = aggregate_data(hit2_data, bad_workers)

if __name__ == '__main__':
	main()