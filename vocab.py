#!/usr/bin/python2.7

def getSentiwordnet():
	file = open("./Datasets/SentiWordNet_3.0.0_20130122.txt", "r")

	posScore = []
	negScore = []
	vocab = []

	for i, line in enumerate(file):
		if line[0]=="a":
			tokens = line.split("\t")

			for j, token in enumerate(tokens):
				if "#" in token and j>3:
					imWords = token.split(" ")
					
					for imWord in imWords:
						word = imWord.split("#")[0]
						vocab.append(word)
						posScore.append(tokens[2])
						negScore.append(tokens[3])

