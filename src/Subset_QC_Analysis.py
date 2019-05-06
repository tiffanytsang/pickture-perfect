#!/usr/bin/env python

import pandas as pd
import re

def make_url_map(df):
	url_map = {}
	for row in df.iterrows():
		row = row[1]
		label = row[0]
		url = row[2]
		url_map[label] = url
	return url_map

def get_votes(row, url_map):
	votes = row['Q3']
	votes_list = re.findall(r'img\d+', votes)
	return [url_map[vote] for vote in votes_list]

def find_unqualified_workers(df, url_map):
	unqualified_workers = set()
	for row in df.iterrows():
		row = row[1]
		worker_id = row['Q1']
		votes = get_votes(row, url_map)
		if any(['neg' in vote for vote in votes]):
			unqualified_workers.add(worker_id)
	print('total workers: ' + str(len(df.Q1.unique())))
	print('# bad workers: ' + str(len(unqualified_workers)))
	return unqualified_workers

def sorted_urls(urls):
	l = [{'img_url': k, 'count': v} for (k, v) in urls.items()]
	l.sort(key=lambda rec: rec['count'], reverse=True)
	return l

def rank_images(df, url_map):
	unqual = find_unqualified_workers(df, url_map)
	out = {}
	for row in df.iterrows():
		row = row[1]
		worker_id = row['Q1']
		if (worker_id not in unqual):
			votes = get_votes(row, url_map)
			for vote in votes:
				if vote in out:
					out[vote] = out[vote] + 1
				else:
					out[vote] = 1
	return sorted_urls(out)

def get_ranked_images(input_csv, output_csv):
	input_df = pd.read_csv(input_csv, header=None)
	url_map = make_url_map(input_df)
	df = pd.read_csv(output_csv, skiprows=[1,2])
	return rank_images(df, url_map)

def write_results(url_list, filepath):
	out_df = pd.DataFrame(url_list, columns=['img_url'])
	out_df.to_csv(filepath, index=False)

def make_csv_list():
	places = ['Budapest', 'Singapore', 'California', 'Greece', 'CostaRica', 'SouthAfrica']
	gb_in = [('../data/Subset_Data/Qualtrics_Input/' + place + '_GOOD_BAD.csv') for place in places]
	cb_in = [('../data/Subset_Data/Qualtrics_Input/' + place + '_CHECKBOX.csv') for place in places]
	gb_out = [('../data/Subset_Data/Qualtrics_Output/' + place + '_GoodBad.csv') for place in places]
	cb_out = [('../data/Subset_Data/Qualtrics_Output/' + place + '_Checkbox.csv') for place in places]
	gb_res = [('../data/Subset_Results/' + place + '_GoodBad.csv') for place in places]
	cb_res = [('../data/Subset_Results/' + place + '_Checkbox.csv') for place in places]
	gb_list = list(zip(gb_in, gb_out, gb_res))
	cb_list = list(zip(cb_in, cb_out, cb_res))
	return gb_list + cb_list    

def main():
	csv_list = make_csv_list()
	for (in_csv, out_csv, res_csv) in csv_list:
		print(res_csv)
		urls = get_ranked_images(in_csv, out_csv)

if __name__ == '__main__':
	main()