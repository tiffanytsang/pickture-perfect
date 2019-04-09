# pickture-perfect

**Part 2: Deliverable 1**

Milestone 1: Develop methods to aggregate Mechanical Turker response data (6 points total)
* Develop method to identify bad workers (2 points)
* Develop method to identify the best photo(s) in a set of similar photos (2 points)
* Develop method to use metadata (time stamps, geolocation) to group photos (2 points)

Milestone 2: Set up the HIT (7 points total)
* Allow users to upload photos (1 point)
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

Total: 20 points

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
