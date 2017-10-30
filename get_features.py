import csv
from collections import defaultdict
filename = "tweets.csv"

allTweets = [];
fvec = defaultdict()
#f0: percentage of capitalized text
num_tweets = 10;
num_features = 2;
for i in range(num_tweets):
	fvec[i] = defaultdict()
	for j in range(num_features):
		fvec[i][j] = -1.0;

with open(filename, 'r') as csvfile:
	csvreader = csv.reader(csvfile)
	fields = csvreader.next()

	for row in csvreader:
		str1 = ''.join(row)
		# print str1
		allTweets.append(str1);


# print allTweets

for tweet in allTweets:

	line = tweet.split(' ')
	line_size = len(line)
	Cap = 0
	CAP = 0
	exc = 0
	for word in line:
		## for capitalised, f0 and f1
		uppers = [l for l in word if l.isupper()]
		print "1st:", word[0]
		if word[0].isupper():
			Cap+=1
		s1 = len(uppers)
		s2 = len(word);
		if s1==s2:
			print "CAP word: ", word
			CAP+=1


		## for exclamations and capitalised check
		last_char = line.strip()[-1]
		if last_char=='!':
			exc += 1

	fvec[i][0] = ((Cap*1.0)/line_size)
	fvec[i][1] = ((CAP*1.0)/line_size)
	if Cap==0:
		fvec[i][2] = 0
	else:
		fvec[i][2] = 1
	print "new:", tweet, fvec[i][0], fvec[i][1], fvec[i][2]
	


	# print 



		





