CFLAGS=-Wall -pedantic
COMPILE=g++ -c -g
LINK=g++

all : Parser

lex.yy.cpp : tokenizer.l
	flex -o lex.yy.cpp tokenizer.l

Parser : lex.o main.o token.o context.o globals.h token.h
	$(LINK) lex.o main.o token.o context.o -o Parser $(CFLAGS)

main.o : main.cpp globals.h
	${COMPILE} main.cpp -o main.o $(CFLAGS)

lex.o : lex.yy.cpp globals.h
	$(COMPILE) lex.yy.cpp -o lex.o $(CFLAGS)

token.o : token.cpp globals.h token.h
	$(COMPILE) token.cpp -o token.o $(CFLAGS)

context.o : context.cpp context.h
	$(COMPILE) context.cpp -o context.o $(CFLAGS)

test : Parser
	./Parser testFile.txt

clean :
	rm -f *.o lex.yy.c *~ Parser valgrind-results.txt
