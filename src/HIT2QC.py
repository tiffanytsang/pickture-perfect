import pandas as pd
import csv

#output bad workers
def identify_bad_workers(hit2_data):

	bad_workers = []

	#identify bad workers
	for index, row in hit2_data.iterrows():
		if (row['Chosen1'] == 9 or row['Chosen1'] == 10
			or row['Chosen2'] == 9 or row['Chosen2'] == 10
			or row['Chosen3'] == 9 or row['Chosen2'] == 10):
			bad_workers.append(row['WorkerID'])

	#write bad workers to csv
	with open('../data/HIT2/hit2unqualifiedworkers.csv', 'w') as f:
		writer = csv.writer(f,delimiter=',')
		writer.writerow(['WorkerID'])
		for bad_worker in bad_workers:
			writer.writerow([bad_worker])

	return bad_workers

def main():
	hit2_data = pd.read_csv('../data/HIT2/hit2dummy.csv')
	bad_workers = identify_bad_workers(hit2_data)

if __name__ == '__main__':
	main()