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

def testFeatures(context):
	features = dict(
		honourificTest = isHonourific(context, True)
		)
	return features
