pattern = [
	('is the best', 'positif'),
	('is the worst', 'negatif'),
	('is unstoppable', 'positif'),
	('deserves to win', 'positif'),
	('will win the trophy', 'positif'),
	('cant even score', 'negatif'),
	('always do blunder', 'negatif'),
	('too old', 'negatif'),
	('wins many trophies', 'positif'),
	('saves the day', 'positif'),
	('can only score by penalty', 'negatif'),
	('is master of football', 'positif'),
	('is overrated','negatif'),
	('is underrated', 'positif'),
	('is terrible','negatif'),
	('is maestro', 'positif'),
	('always carry the team', 'positif'),
	('is fifa favourite', 'positif'),
	('is loyal to the team', 'positif'),
	('is incredible', 'positif'),
	('confident of winning','positif'),
	('stats is better than oor ther candidate','positif'),
	('the GOAT will win this year','positif'),
	('is King of Football','positif'),
	('is a future','positif'),
	('is frustated to win' , 'negatif'),
	(' = POY', 'positif'),
	('for', 'positif'),
	('is not rated fairly', 'positif'),
	('is gonna made it this year', 'positif')
]

pattern_2 = [
	('This is year of','positif'),
	("Ballon d'or 2017 winner will be",'positif'),
	("My prediction for #Ballon d'or is",'positif'),
	("And the best player of this season is",'positif'),
	("I am his number 1 fan. go",'positif'),
	("I am not his fan but stats dont lie",'positif'),
	("Soon Ballon D'or will be",'positif')
]

pattern_3 = [
	("win. FIFA is rigged",'negatif'),
	("win. is because his teammate just good",'negatif'),
	("lose. i will stop watch football", 'positif')
]

candidate = [
	'lionel messi',
	'cristiano ronaldo',
	'neymar jr',
	'gianluigi buffon',
	'sergio ramos'
]

outline = ""
for pat in pattern:
	for can in candidate:
		outline += can+" "+pat[0]+" #Ballondor"+","+pat[1] + "\n"
for pat in pattern_2:
	for can in candidate:
		outline += pat[0]+" "+ can +" #Ballondor"+","+pat[1] + "\n"
for pat in pattern_3:
	for can in candidate:
		outline += "If " + can+" "+pat[0]+" #Ballondor"+","+pat[1] + "\n"		
print(outline, file=open("generate.csv","w"))