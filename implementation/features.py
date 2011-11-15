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

# feature function for surrounding quotes
def inQuote(context, response):

	# initialize the quote level
	quoteLevel = 0

	# calculate the quote level of the prefix
	for candidate in context[:3]:
		# print "candidate: '" + candidate + "' 0:'" + candidate[0] + "' -1:'" + candidate[-1] + "'"
		if candidate[0] == '"':
			quoteLevel += 1
		if candidate[-1] == '"':
			quoteLevel -= 1

	# if we have unbalanced open quotes, we are in a quote
	if quoteLevel > 0:
		return 1

	# calculate the quote level of the suffix
	for candidate in context[4:]:
		if candidate[0] == '"':
			quoteLevel += 1
		if candidate[-1] == '"':
			quoteLevel -= 1

	# if we have unbalanced closed quotes, we are in a quote
	if quoteLevel < 0:
		return 1

	# no quotey stuff count. 
	return 0

def testFeatures(context):
	features = dict(
		honourificTest = isHonourific(context, True),
		quoteTest = inQuote(context, True)
		)
	return features

