candidate_nicknames = {
	"ronaldo": [
				"cristiano",
				"c. ronaldo",
				"ronaldo",
				"penaldo",
				"cr7",
				"cr",
				"cristiano ronaldo",
				"@cristiano"
				],
	"messi": [
				"leo",
				"messi",
				"lionel",
				"pulga",
				"messidona",
				"lionel messi",
				"@teammessi"
				],
	"neymar": [
				"neymar",
				"neymar jr.",
				"neymar jr",
				"neymar da silva santos júnior",
				"@neymarjr",
				],
	"buffon": [
				"buffon",
				"gigi",
				"superman",
				"gianluigi",
				"gianluigi buffon",
				"@gianluigibuffon"
				],
	"ramos": [
				"ramos",
				"sergio",
				"sergio ramos",
				"cuqui",
				"garcía",
				"sergio ramos garcía",
				"@sergioramos"
				]
}

negative_dict = [
					"not",
					"dont",
					"don't",
					"doesnt",
					"doesn't",
					"cant",
					"can't",
					"isn't",
					"isnt",
					"aren't",
					"arent",
					"wont",
					"won't",
					"shouldnt",
					"shouldn't",
					"musn't",
					"musnt"
				]


sample_tweets = [
					("Barcelona Soccer Shirt Lionel Messi #10 Futbol Jersey Men's Hooded Sweatshirt #Messi #BallondOr #ElClasico &gt;\u2026 https://t.co/mTckH6GLsO",1),
					("Lionel Messi will win the Ballon d'Or 2017. @fundacionmessi #BallondOr https://t.co/UIhwASxhux",1),
					("Ramos holds uncertainty over Ronaldo´s future at Madrid ##Atleticomadrid ##BallonDor… https://t.co/zpI7Pvt3RQ https://t.co/gfgP3HWBeG",0),
					("RT @CRonaldoSource: @Cristiano @nikefootball The best player in the world ?? #CristianoRonaldo #BallondOr https://t.co/T7IZpsTY4i",1)
				]


candidate_scores = {
	"ronaldo": {
		"positif": 0,
		"negatif": 0
	},
	"messi": {
		"positif": 0,
		"negatif": 0
	},
	"neymar": {
		"positif": 0,
		"negatif": 0
	},
	"buffon": {
		"positif": 0,
		"negatif": 0
	},
	"ramos": {
		"positif": 0,
		"negatif": 0
	},
}

def getCandidate(tweet):
	tweet = tweet.lower()
	result = "none"
	for key, value in candidate_nicknames.items():
		for nickname in value:
			if nickname in tweet:
				result = key
				break

		if result != "none":
			break

	return result

def countScore(samples):
	for sample in samples:
		candidate = getCandidate(sample[0])
		if candidate != "none":
			if (sample[1] == 1):
				candidate_scores[candidate]["positif"] += 1
			else:
				candidate_scores[candidate]["negatif"] += 1				

countScore(sample_tweets)
print(candidate_scores)


# print(getCandidate("Barcelona Soccer Shirt Lionel Messi #10 Futbol Jersey Men's Hooded Sweatshirt #Messi #BallondOr #ElClasico &gt;\u2026 https://t.co/mTckH6GLsO"))
