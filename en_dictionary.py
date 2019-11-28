'''
Program for searching an explanation of entered word in the dictionary
Input: a word in english
Output: an explenation of the entered word in english
'''

import json
from difflib import get_close_matches

dt = json.load(open('data.json'))

def translate(w):
	'''
	Function looks for a word in the database. First looks for the exact name.
	If func can't find the entered word than function 'get_close_matches' from the module: 'difflib'
	is applied and will try to find closest mach. If the ratio rate between entered word and similarity
	with a word in the database is lower than 0.6 than no results will be provided.
	'''
	w =  w.lower()
	if w in dt:
		return dt[w]
	elif w.capitalize() in dt:
		return dt[w.capitalize()]
	elif w.upper() in dt:
		return dt[w.upper()]

	elif len(get_close_matches(w,dt.keys())) > 0:
		ask = input (f"Did you mean:{get_close_matches(w,dt.keys())[0]} ?. If yes, enter Y if no enter N ").lower()
		if ask[0] == 'y':
			return dt[get_close_matches(w,dt.keys())[0]]
		elif ask[0] == 'n':
			return "Sorry. Try again."
		else:
			return "Sorry we didn't recognize your entry"


	else:
		return "Word doesn't exist. Please check spelling"

def question():
	'''
	Function which asks for a new search
	'''
	
	x = input("Do you want to translate another word? If yes, enter 'Y' if no, enter 'N': ").lower()
	if x == 'y':
		return True

	elif x == 'n':
		print('Program finished')
	else:
		print('Unrecognize answer. Program ended')
		return False


def code():
	'''
	Simple function which asks for a word that you wants to translate and 
	then function 'translate' will run. 
	If there is more values for the selected key in the database, function will print all of them.
	'''
	word = input("Enter the word you want to translate: ").lower()
	output = translate(word)

	if type(output) == list:
		for item in output:
				print(item)

	else:
		print (output)


#Functions for running the program
code()	
while question():
	code()
