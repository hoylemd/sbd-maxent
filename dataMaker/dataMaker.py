import string
import sys

honourific_list = [
	"mr.",
	"mrs.",
	"dr.",
	"ms.",
	"prof.",
	"pvt.",
	"cpl.",
	"mcpl.",
	"sgt.",
	"wo.",
	"cdt.",
	"lt.",
	"cpt.",
	"mjr.",
	"col.",
	"gen."
]

def isHonourific(context, response):
	candidate = context[3]
	for honourific in honourific_list:
		if candidate.lower == honourific.lower:
			return true

	return false

if len(sys.argv) == 2:
	f = open(sys.argv[1], 'r')

	lines = f.readlines()
	
	contexts = []

	for line in lines:
		words = (string.split(line))
		for word in words:
			print word + " ",
		print
		contexts.append(words)

	

else:
	print "Usage: python dataMaker <filename>"
	print "    where <filename> is the path to a contexts file"
