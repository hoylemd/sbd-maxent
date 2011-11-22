from features import *


# Test them!

testsFailed = []
numTestsPassed = 0
numTestsFailed = 0
testsRun = 0

def assertVal(testName, condition, result):
	# get globals
	global testsFailed
	global numTestsPassed
	global numTestsFailed
	global testsRun
	
	testsRun += 1
	if condition == result:
		numTestsPassed += 1;
		print testName + " test passed."
	else :
		numTestsFailed += 1;
		testsFailed.append(testName);
		print testName + " test FAILED!"

# test Honourific

# regular, negative
testName = "honourific negative"
context = ["this", "is", "not", "an", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isHonourific(context, True), 0);
print

# regular, positive
testName = "honourific positive"
context = ["this", "is", "not", "Mr.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isHonourific(context, True), 1);
print

# test inQuote

# regular, negative
testName = "in quote negative"
context = ["this", "is", "not", "an", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, inQuote(context, True), 0);
print

# regular, positive, prefix
testName = "in quote positive prefix"
context = ["this", "is", "\"not", "Mr.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, inQuote(context, True), 1);
print

# regular, positive, suffix
testName = "in quote positive suffix"
context = ["this", "is", "not", "Mr.", "honorific\"", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, inQuote(context, True), 1);
print

# regular, negative, prefix quoted word
testName = "in quote negative prefix quoted word"
context = ["this", "is", "\"not\"", "Mr.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, inQuote(context, True), 0);
print

# regular, negative, suffix quoted word
testName = "in quote negative suffix quoted word"
context = ["this", "is", "not", "Mr.", "\"honorific\"", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, inQuote(context, True), 0);
print

# regular, negative, closed quote preceeding
testName = "in quote closed preceeding quote"
context = ["\"Make", "Me.\"", "you", "say?", "OK,", "I", "Will!"]
print "Test case: ",
print context
assertVal(testName, inQuote(context, True), 0)
print

# test candidateQuote

# regular, positive, candidate quoted at start
testName = "candidate quote positive quoted at start"
context = ["this", "is", "not", "\"Mr.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, candidateQuote(context, True), 1);
print

# regular, positive, candidate quoted at end
testName = "candidate quote positive quoted at end"
context = ["this", "is", "not", "Mr.\"", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, candidateQuote(context, True), 1);
print

# regular, positive, candidate quoted in middle
testName = "candidate quote positive quoted in middle"
context = ["this", "is", "not", "M\"r.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, candidateQuote(context, True), 1);
print

# regular, negative, candidate not a quote
testName = "candidate quote positive quoted at end"
context = ["this", "is", "not", "Mr.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, candidateQuote(context, True), 0);
print

# test isNumeric

# regular, positive, candidate is a positive number
testName = "is numeric positive positive number"
context = ["this", "is", "not", "1.5", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isNumeric(context, True), 1);
print

# regular, positive, candidate is a negative number
testName = "is numeric positive negative number"
context = ["this", "is", "not", "-7.2", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isNumeric(context, True), 1);
print

# regular, negative, candidate is a word
testName = "is numeric negative word"
context = ["this", "is", "not", "pineapple.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isNumeric(context, True), 0);
print

# regular, positive, candidate is a positive number
testName = "is numeric negative mixed"
context = ["this", "is", "not", "1.5dudes", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isNumeric(context, True), 0);
print

# test isExclaimation

# regular, positive, candidate ends in an exclaimation
testName = "ends in exclaimation positive"
context = ["this", "is", "not", "totally!", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isExclaimation(context, True), 1);
print

# regular, negative, candidate has no exclaimation
testName = "no exclaimation negative"
context = ["this", "is", "not", "totally.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isExclaimation(context, True), 0);
print

# regular, negative, candidate has exclaimation, but not at the end
testName = "starts with exclaimation negative"
context = ["this", "is", "not", "!bile", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isExclaimation(context, True), 0);
print

# test isQuestion

# regular, positive, candidate ends in a question
testName = "ends in question positive"
context = ["this", "is", "not", "totally?", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isQuestion(context, True), 1);
print

# regular, negative, candidate has no question
testName = "no question negative"
context = ["this", "is", "not", "totally.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isQuestion(context, True), 0);
print

# regular, negative, candidate has question, but not at the end
testName = "starts with question negative"
context = ["this", "is", "not", "?bile", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, isQuestion(context, True), 0);
print

# test allCaps

# regular, positive, candidate is allcaps
testName = "allcaps positive punctuated"
context = ["this", "is", "not", "U.S.A.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, allCaps(context, True), 1);
print

# regular, positive, candidate is allcaps, no punctuation
testName = "allcaps positive not punctuated"
context = ["this", "is", "not", "USA.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, allCaps(context, True), 1);
print

# regular, positive, candidate is not allcaps
testName = "allcaps negative"
context = ["this", "is", "not", "U.S.a.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, allCaps(context, True), 0);
print

# test followingCapitalized

# regular, positive, following is capitalized
testName = "following capitalized positive"
context = ["this", "is", "not", "candidate.", "Honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, followingCapitalized(context, True), 1);
print

# regular, negative following is not capitalized
testName = "following capitalized negative"
context = ["this", "is", "not", "candidate.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, followingCapitalized(context, True), 0);
print

# test monthAbbrevitation

# regular, positive month abbreviation
testName = "month abbreviation positive"
context = ["this", "is", "not", "Feb.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, monthAbbreviation(context, True), 1);
print

# regular, negative month abbreviation
testName = "month abbreviation positive"
context = ["this", "is", "not", "an.", "honorific", "my", "friend"]
print "Test case: ",
print context
assertVal(testName, monthAbbreviation(context, True), 0);
print


print "Testing summary:"
print "Num run: %d Num passed: %d Num Failed: %d" % (testsRun, numTestsPassed, numTestsFailed)
print "Pass rate: %.3f Fail rate: %.3f" % (float(numTestsPassed) / float(testsRun), float(numTestsFailed) / float(testsRun))
print "Failed tests:"
for test in testsFailed:
	print test
