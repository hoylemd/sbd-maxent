import string
import sys

# list of honourifics to check against
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
	"gen.",
	"hrm."
]

# feature function for honourifics
def isHonourific(context, response):
	# grab the relevant token
	candidate = context[3].lower()

	# check it against the list
	for honourific in honourific_list:	
		if candidate == honourific:
			return 1

	# fall-through
	return 0

# main script==========================================

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

	contextFeatures = []	
	for context in contexts:
		features = dict(
			honourificTest= isHonourific(context, True))
		contextFeatures.append(features)

	print contextFeatures
	

else:
	print "Usage: python dataMaker <filename>"
	print "    where <filename> is the path to a contexts file"
