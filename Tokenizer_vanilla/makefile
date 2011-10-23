$CFLAGS=-Wall -pedantic

all : Tokenizer

lex.yy.cpp : tokenizer.l
	flex -o lex.yy.cpp tokenizer.l

Parser : lex.o main.o token.o globals.h token.h
	g++ lex.o main.o token.o -o Parser $(CFLAGS)

main.o : main.cpp globals.h
	g++ -c -g main.cpp -o main.o $(CFLAGS)

lex.o : lex.yy.cpp globals.h
	g++ -c -g lex.yy.cpp -o lex.o $(CFLAGS)

token.o : token.cpp globals.h token.h
	g++ -c -g token.cpp -o token.o $(CFLAGS)

memtest : clean Tokenizer
	valgrind -v --leak-check=full --log-file=valgrind-results.txt ./Tokenizer testFile.txt

test : clean Tokenizer
	./Tokenizer testFile.txt

clean :
	rm -f *.o lex.yy.c *~ Parser valgrind-results.txt
