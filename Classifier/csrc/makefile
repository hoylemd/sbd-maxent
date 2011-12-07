CFLAGS=-Wall -pedantic
COMPILE=g++ -c -g
LINK=g++

all : Contextualizer GetSample SplitSample stopwatch Replacer newlineStripper

lex.yy.cpp : tokenizer.l
	flex -o lex.yy.cpp tokenizer.l

newlineStripper : newlineStripper.cpp
	$(COMPILE) newlineStripper.cpp -o newlineStripper.o $(CFLAGS)
	$(LINK) newlineStripper.o -o newlineStripper $(CFLAGS)

Contextualizer : lex.o main.o token.o context.o globals.h token.h
	$(LINK) lex.o main.o token.o context.o -o Contextualizer $(CFLAGS)

GetSample: getSample.cpp
	${COMPILE} getSample.cpp -o getSample.o ${CFLAGS}
	$(LINK) getSample.o -o GetSample ${CFLAGS}

SplitSample: splitSample.cpp
	${COMPILE} splitSample.cpp -o splitSample.o ${CFLAGS}
	$(LINK) splitSample.o -o SplitSample ${CFLAGS}

stopwatch: stopwatch.c
	${COMPILE} stopwatch.c -o stopwatch.o ${CFLAGS}
	${LINK} stopwatch.o -o stopwatch ${CFLAGS}

Replacer: lex.o replacer.o token.o globals.h token.h
	$(LINK) lex.o replacer.o token.o -o Replacer $(CFLAGS)

main.o : main.cpp globals.h
	${COMPILE} main.cpp -o main.o $(CFLAGS)

lex.o : lex.yy.cpp globals.h
	$(COMPILE) lex.yy.cpp -o lex.o $(CFLAGS)

token.o : token.cpp globals.h token.h
	$(COMPILE) token.cpp -o token.o $(CFLAGS)

classification.o : classification.cpp globals.h classification.h
	$(COMPILE) classification.cpp -o classification.o $(CFLAGS)

context.o : context.cpp context.h
	$(COMPILE) context.cpp -o context.o $(CFLAGS)

test : Contextualizer
	cat testFile.txt | ./Contextualizer > testFile.context

clean :
	rm -f *.o lex.yy.cpp *~ Contextualizer GetSample SplitSample newlineStripper stopwatch Replacer
