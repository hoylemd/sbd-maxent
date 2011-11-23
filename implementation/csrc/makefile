CFLAGS=-Wall -pedantic
COMPILE=g++ -c -g
LINK=g++

all : Contextualizer GetSample stopwatch

lex.yy.cpp : tokenizer.l
	flex -o lex.yy.cpp tokenizer.l

Contextualizer : lex.o main.o token.o context.o globals.h token.h
	$(LINK) lex.o main.o token.o context.o -o Contextualizer $(CFLAGS)

GetSample: getSample.cpp
	${COMPILE} getSample.cpp -o getSample.o ${CFLAGS}
	$(LINK) getSample.o -o GetSample ${CFLAGS}

stopwatch: stopwatch.c
	${COMPILE} stopwatch.c -o stopwatch.o ${CFLAGS}
	${LINK} stopwatch.o -o stopwatch ${CFLAGS}

main.o : main.cpp globals.h
	${COMPILE} main.cpp -o main.o $(CFLAGS)

lex.o : lex.yy.cpp globals.h
	$(COMPILE) lex.yy.cpp -o lex.o $(CFLAGS)

token.o : token.cpp globals.h token.h
	$(COMPILE) token.cpp -o token.o $(CFLAGS)

context.o : context.cpp context.h
	$(COMPILE) context.cpp -o context.o $(CFLAGS)

test : Contextualizer
	cat testFile.txt | ./Contextualizer > testFile.context

clean :
	rm -f *.o lex.yy.cpp *~ Contextualizer GetSample
