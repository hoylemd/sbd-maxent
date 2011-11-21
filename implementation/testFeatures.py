from features import *


# Test them!

def assertVal(testName, condition, result):
	if condition == result:
		print testName + " test passed."
	else :
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
