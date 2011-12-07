import sys
import enchant

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
	"capt.",
	"cpts.",
	"capts.",
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
	"sens.",
	"jr.",
	"sr."
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
	"figs.",
	"s.",
	"st.",
	"ave.",
	"pp.",
	"pg.",
	"no.",
	"gov.",
	"p.m.",
	"a.m.",
	"cc.",
	"inc.",
	"co.",
	"i.d.",
	"cf.",
	"ch.",
	"vs.",
	"h.m.s.",
	"lb.",
	"lbs.",
	"p.",
	"m.p.h.",
	"in.",
	"stat.",
	"dept.",
	"e.g."
]



country_list = [
	"u.s."
]

day_list = [
	"mon.",
	"tues.",
	"wed.",
	"thurs.",
	"fri.",
	"sat.",
	"sun."
]

state_list = [
	"ala.",
	"ariz.",
	"ark.",
	"calif.",
	"colo.",
	"conn.",
	"del.",
	"fla.",
	"ga.",
	"ill.",
	"ind.",
	"kans.",
	"ky.",
	"la.",
	"md.",
	"mass.",
	"mich.",
	"minn.",
	"miss.",
	"mo.",
	"mont.",
	"nebr.",
	"n.h.",
	"n.j.",
	"n.m.",
	"n.y.",
	"n.c.",
	"n.d.",
	"okla.",
	"ore.",
	"pa.",
	"r.i.",
	"s.c.",
	"s.d.",
	"tenn.",
	"tex.",
	"vt.",
	"va.",
	"wash.",
	"w.va.",
	"wis.",
	"wyo."
]

english = enchant.Dict("en_US")

mistakeLists = [
	honourific_list,
	month_list,
	abbreviation_list,
	day_list,
	country_list,
	state_list
]

# function to remove all occurances of come chars in a string
def stripChars(theString, chars):
	# grab a local copy of the string
	returner = theString

	# iterate through chars and remove each one
	for char in chars:	
		returner = returner.replace(char, "")

	# toss back the stripped string
	return returner

# function to normalize a strin minimally
def formatMinimal(candidate):
	return stripChars(candidate, "*")

# function to normalize a string for analysis
def formatStandard(candidate):
	return stripChars(formatMinimal(candidate), ",").lower()

# function to normalize a string with punctuation removed
def formatStripped(candidate):
	return stripChars(formatStandard(candidate), ".?!")

# function to check if a word is a number
def isNumber(word):
	#try to cast it to a float
	try:
		# success. it's a number
		float(word)
		return True
	except ValueError:
		# failure. not a number
		return False	

# function to check for dictionary words
def isWord(candidate):
	# check the candidate against the dictionary
	if (len(candidate) > 1 and not isNumber(candidate)): 
		if english.check(candidate):
			return True
	
	# fall-through
	return False

# function to check if a token has a punctuation char at the end
def punctuationAtEnd(token):
	# grab the relevant char
	candidate = token[-1]

	# check the char against punctuation
	if (candidate == "." or candidate == "?" or candidate == "!"):
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
	candidate = context[3].lower().replace(".","")
	
	#check if the candidate is numeric
	if (isNumber(candidate)):
		return 1
	else:
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

#feature function for common mistakes (generally abbreviations)
def isMistake(context, response):
	# grab the relevant token
	candidate = formatStandard(context[3])

	# check it against the lists
	for list in mistakeLists:
		for mistake in list:
			if candidate == mistake:
				return 1

	# fall-through
	return 0

#feature function for dictionary words
def candidateIsWord(context, response):
	# grab the relevant token
	candidate = formatStandard(context[3])

	# check if it's a dictionary word
	if isWord(candidate):
		return 1;

	# fall-through
	return 0;

#feature function for dictionary words
def followingIsWord(context, response):
	# grab the relevant token
	candidate = formatStandard(context[4])

	# check if it's a dictionary word
	if isWord(candidate):
		return 1;

	# fall-through
	return 0;

#feature function for initials
def isInitial(context, response):
	# grab the relevant token
	candidate = formatStripped(context[3])
	
	# if it's only one character left, it's probably an initial
	if len(candidate) == 1:
		return 1
	else:
		return 0

# feature function for if the punctuation is at the end of the word
def punctuationAtEndFeature(context, response):
	# grab the relevant char
	candidate = formatMinimal(context[3])

	# check the char against punctuation
	if punctuationAtEnd(candidate):
		return 1
	
	# fall-through
	return 0
	

# feature function to check if the proceeding word is a candidate
def precedingCandidate(context, response):
	# grab the relevant token
	candidate = formatMinimal(context[2])

	# check if it's a potential end of sentence
	if punctuationAtEnd(candidate):
		return 1

	# fall-through
	return 0

# function to run all feature tests
def testFeatures(context):
	features = dict(
		quoteTest = inQuote(context, True),
		candidateQuoteTest = candidateQuote(context, True),
		numericTest = isNumeric(context, True),
		exclaimationTest = isExclaimation(context, True),
		questionTest = isQuestion(context, True),
		uppercaseTest = allCaps(context, True),
		FollowingCapitalizationTest = followingCapitalized(context, True),
		mistakeList = isMistake(context, True),
		dictionaryTest = candidateIsWord(context, True),
		followingDictionary = followingIsWord(context, True),
		initialTest = isInitial(context, True),
		punctuationEndTest = punctuationAtEndFeature(context, True),
		precedingTest = precedingCandidate(context, True)
	)
	return features


