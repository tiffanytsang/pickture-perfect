# pickture-perfect

**Part 2: Deliverable 1**

Milestone 1: Develop methods to aggregate Mechanical Turker response data (4 points total)
* Develop method to identify bad workers (2 points)
* Develop method to identify the best photo(s) in a set of similar photos (2 points)

Milestone 2: Set up the HIT (6 points total)
* Create three different HITs (using our three comparison methods) based on the same photoset
  1. X vs Y - Turker sees two images and picks the better one until the Turker has compared every combination of two images from the photoset (2 points)
  2. Subsets - Turker continuously picks subsets of the best images from the photoset until the best image is identified (2 points)
  3. Rank - Turker ranks the images from 1 to 10, 1 = best and 10 = worst (1 point)
* Upload HITs to Mechanical Turk and allow Turkers to work and make the results accessible to the requester (1 point)

Milestone 3: Analyze the different comparison methods (4 points total)
* Determine the best images from the uploaded photoset in advance (1 point)
  * Selecting for not blurry, not overly saturated, not rotated pictures
  * People (if there are any) looking at camera, eyes open, no red-eye
* Compare the three Turker-produced photosets with our predetermined best images (2 points)
  * Calculate percentage correct for each comparison method (1 point)

Milestone 4: Analyze results and produce a video (3 points total)
* Compile results from Milestone 3 and produce a video as final deliverable (3 points)

Total: 17 points

---

**Part 2: Deliverable 2**

* Raw data
  * Stored in picture/ directory
  * Each set of 10 pictures is stored under a subdirectory
* Sample input/output for QC
  * All input/output is stored in data/HITx directory. x = 1, 2, or 3 depending on the HIT design
  * Input: dummy data is stored in filename hitxdummy.csv. The negative images are stored under the NegImg1 and NegImg2 column
  * Output: bad workers are output in file with name hitxunqualifiedworkers.csv
* Sample input/output for aggregation
  * All input/output stored in data/HITx directory.
  * Input: dummy data is stored in filename hitxdummy.csv. Each row in the CSV contains the HIT reponses from a unique MTurk worker, identified by numeric ID. The worker output is stored under appropriate columns.
  * Output: best photo is output in file with name hitxbestphoto.csv
* Code for QC
  * Stored in src/ directory: files with name HITxQC.py
  * one file is included for each HIT design
* Code for aggregation
  * Stored in src/ directory: files with name HITxAggregation.py
  * one file is included for each HIT design
  
---
  
  **Part 3**

How to contribute to project:

1. Navigate to the MTurk Worker sandbox at https://workersandbox.mturk.com. Search for “Pickture Perfect.” Alternatively, click on one of the three links below:
X vs. Y: https://workersandbox.mturk.com/projects/3U2H1DGWOQ8M0GCWN8ZNJ3WWAFP4FC/tasks?ref=w_pl_prvw
Subset: https://workersandbox.mturk.com/projects/35VN5BQM8W5K112SK39I3TU23I25JM/tasks?ref=w_pl_prvw
Ranking: https://workersandbox.mturk.com/projects/32WAV7G60Q44K0FWWOZELY15K2G3DI/tasks?ref=w_pl_prvw
2. Once you start the HIT, click on the link to be redirected to the Qualtrics survey.
3. Depending on the HIT design, follow the appropriate instructions.
  * X vs. Y: You will be presented with a set of questions. Each question will have 2 images. Select the image of better aesthetic quality.
  * Rating: You will be presented with a set of questions. Each question will have 10 images. Order the images from 1 to 10 so that 1 indicates the photo of best aesthetic quality 
  * Subset: You will be presented with a series of questions. Each question will have 10 images. Please select the 3 images of best aesthetic quality.
4. Once you submit the Qualtrics survey, we will provide a code that you enter on the Amazon MTurk site.
5. If that code is verified, you will earn money for your work.
6. If you have any questions, contact Pickture Perfect at picktureperfect0@gmail.com

Characteristics of Good (high aesthetic quality) images include but are not limited to:

* Sharp/focused
* Proper coloration and saturation
* People (if any) are looking at the camera with open eyes
* Composition: main objects are framed as the focus of the image

Characteristics of Bad (low aesthetic quality) images include but are not limited to:

* Blurry
* Over/undersaturated
* Discolored
* If there are people in the image, they:
  * Have their eyes closed
  * Have red-eye
  * Aren’t looking at the camera
  * Are difficult to see

---

As of now, we have implemented Milestone 1 and 2. For Milestone 1, we have already developed methods to aggregate Mechanical Turker response data and to identify bad workers. Documentation for our relevant code is included below. For Milestone 2, we have already set up HITs for our 3 designs. The tasks can be found on the MTurk Worker Sandbox. These are the links to the HITs:
* X vs. Y: https://workersandbox.mturk.com/projects/3U2H1DGWOQ8M0GCWN8ZNJ3WWAFP4FC/tasks?ref=w_pl_prvw
* Subset: https://workersandbox.mturk.com/projects/35VN5BQM8W5K112SK39I3TU23I25JM/tasks?ref=w_pl_prvw
* Ranking: https://workersandbox.mturk.com/projects/32WAV7G60Q44K0FWWOZELY15K2G3DI/tasks?ref=w_pl_prvw

How code runs:

We pass data from the Qualtrics survey to our quality control and aggregation code to identify the best photo in a set of similar photos. Documentation for our quality control and aggregation code is found below. Code to read data from the Qualtrics survey will be implemented as part of Milestone 3.

Documentation for Quality Control Code:

For each of the three HIT designs, we include two gold standard negative photos in every set of 8 images. If the worker ever chooses the gold standard negative photo as one of the best photos, we will label the worker as a bad worker and reject their work.
* X vs. Y - Workers are presented with two photos. If the worker chooses the gold standard negative photo as the better photo, that worker will be identified as a bad worker. If the two photos presented are both gold standard negative photos, choosing the bad photo will not affect the worker’s quality, as they only choice they had was to choose a bad photo.
* Subset - If the worker includes a gold standard negative photo in their chosen subset of the 3 best photos, the worker will be identified as a bad worker.
* Ranking - If the worker ranks a gold standard negative photo in the top 8 out of 10, the worker will be identified as a bad worker.

The ID of bad workers are output in a csv file.


Documentation for Aggregation Code:

For each of the three HIT designs, we write aggregation code to identify the best photo in a set of 10 similar images.
* X vs. Y -  We will use the Elo Rating System to generate ratings for all the images. The Elo system is a way of calculating the relative ratings of players (or images, in our case) in a zero-sum game. (This is the system used by the World Chess Federation.) Once we have ratings for all of the images in a set, we can then designate the image with the highest rating as the best image in the set.
* Subset - For each image, we will calculate the number of times that image is put in the Top-3 subset. The image with the highest number of times will be designated as the best image.
* Ranking - We will calculate the average ranking for each image and designate the one with the highest average ranking as the best image.

The best photo in a set will be output in a csv file.

For Milestone 3, we will compare the differences in the best images found between the 3 HIT designs. We will compare them to our notions of a best image. To do this, we will look through the photos and tag the photos that we think are the best image. The code will be a simple script that counts these differences.
