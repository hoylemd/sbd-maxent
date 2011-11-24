import sys

# list of honourifics to check against
honourific_list = [
	"mr.",
	"mrs.",
	"dr.",
	"drs.",
	"ms.",
	"prof.",
	"profs.",
	"pvt.",
	"pvts.",
	"cpl.",
	"cpls.",
	"mcpl.",
	"mcpls.",
	"sgt.",
	"sgts.",
	"wo.",
	"wos.",
	"cdt.",
	"ctds.",
	"lt.",
	"lts.",
	"cpt.",
	"cpts.,"
	"mjr.",
	"mjrs.",
	"col.",
	"cols.",
	"gen.",
	"gens.",
	"hrm.",
	"hrms.",
	"rep.",
	"reps.",
	"rev.",
	"revs.",
	"sen.",
	"sens."
]

month_list = [
	"jan.",
	"feb.",
	"mar.",
	"apr.",
	"jun.",
	"jul.",
	"aug.",
	"sept.",
	"oct.",
	"nov.",
	"dec."
]

abbreviation_list = [
	"fig.",
	"s.",
	"av."
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
		try:
			if candidate[-1] == '"' or (candidate[-1] == ',' and candidate[-2] == '"'):
				quoteLevel -= 1
		except IndexError:
			# just continue, there was a standalone ,
			quoteLevel = quoteLevel	

	# if we have unbalanced open quotes, we are in a quote
	if quoteLevel > 0:
		return 1
	
	# calculate the quote level of the suffix
	for candidate in context[4:]:
		if candidate[0] == '"':
			quoteLevel += 1
		try:
			if candidate[-1] == '"' or (candidate[-1] == ',' and candidate[-2] == '"'):
				quoteLevel -= 1
		except IndexError:
			#just continue, there was a standaline ,
			quoteLevel = quoteLevel

	# if we have unbalanced closed quotes, we are in a quote
	if quoteLevel < 0:
		return 1

	# no quotey stuff count. 
	return 0


# feature function for quotes on candidate
def candidateQuote(context, response):
	#get the candidate
	candidate = context[3].lower()

	if candidate.find('"') == -1:
		return 0
	else:
		return 1

# feature function for number candidates
def isNumeric(context, response):
	#get the candidate	
	candidate = context[3].lower()
	
	#try to cast it to a float
	try:
		# success. it's a number
		float(candidate)
		return 1
	except ValueError:
		# failure. not a number
		return 0


#feature function for ! at the end of the candidate
def isExclaimation(context, response):
	#get the candidate
	candidate = context[3].lower()

	#check if it ends in a !
	if candidate[-1] == '!':
		return 1
	else:
		return 0

# feature function for ? at the end of the candidate
def isQuestion(context, response):
	#get the candidate
	candidate = context[3].lower()

	#check if it ends in a ?
	if candidate[-1] == '?':
		return 1
	else:
		return 0	

# feature function to check if all alpha chars are capitalized in candidate
def allCaps(context, response):
	# get the candidate
	candidate = context[3].replace("*", "")
	
	# test it for uppercase	
	if candidate.isupper():
		return 1
	else:
		return 0


# feature function to check if the following token is capitalized
def followingCapitalized(context, response):
	#get the following token
	following = context[4]

	# check for capitalization
	if following == following.capitalize():
		return 1
	else:
		return 0

# feature function to check if the candidate is a month abbreviation
def monthAbbreviation(context, response):
	# grab the relevant token
	candidate = context[3].lower()

	# check it against the list
	for month in month_list:	
		if candidate == month:
			return 1

	# fall-through
	return 0


testContext = ["a", "a", "a", "U.S.*a.", "a", "a", "a"]

# feature function for common abbreviations
def isAbbreviation(context, response):
	# grab the relevant token
	candidate = context[3].lower().replace("*", "")

	# check it against the list
	for abbreviation in abbreviation_list:	
		if candidate == abbreviation:
			return 1

	# fall-through
	return 0

# function to run all feature tests
def testFeatures(context):
	features = dict(
		honourificTest = isHonourific(context, True),
		quoteTest = inQuote(context, True),
		candidateQuoteTest = candidateQuote(context, True),
		numericTest = isNumeric(context, True),
		exclaimationTest = isExclaimation(context, True),
		questionTest = isQuestion(context, True),
		uppercaseTest = allCaps(context, True),
		capitalizationTest = followingCapitalized(context, True),
		monthTest = monthAbbreviation(context, True),
		abbreviationTest = isAbbreviation(context, True)
	)
	return features


