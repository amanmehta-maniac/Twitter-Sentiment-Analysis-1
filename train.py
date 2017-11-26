#!/usr/bin/python2.7


from getData import getTraindata, getTestdata
from vocab import SentiWords
from sklearn.mixture import GaussianMixture

def trainMP(data, labels, n_polarity = 4, n_epochs = 3):
	model = GaussianMixture(n_components=n_polarity, covariance_type="full", n_init=n_epochs)
	model.fit(data, labels)
	return model

def testMP(data, labels):
	predictions = model.predict_proba(data)
	
	lglikelihood = model.score(data, labels)
	print lglikelihood

	return predictions

def main():
	trainData = []
	trainLabels = []
	vocab = SentiWords()
	Data = getTraindata()

	#Data = getTestdata(search="<search_term>", count=<num_of_tweets>)

	for i, sample in enumerate(Data):
		trainData.append(Data.fvec)
		trainLabels.append(Data.label)
	
	model = trainMP(trainData, trainLabels, n_polarity = 4, n_epochs = 3)
	predictions = testMP(model, trainData, trainLabels)

if __name__ == "__main__":
	main()