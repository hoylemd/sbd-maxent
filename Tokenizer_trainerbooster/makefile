$CFLAGS=-Wall -pedantic

all : Tokenizer

lex.yy.cpp : tokenizer.l
	flex -o lex.yy.cpp tokenizer.l

Tokenizer : lex.o main.o token.o filename.o
	g++ lex.o main.o token.o filename.o -o Tokenizer $(CFLAGS)

main.o : main.cpp globals.h
	g++ -c -g main.cpp -o main.o $(CFLAGS)

lex.o : lex.yy.cpp globals.h
	g++ -c -g lex.yy.cpp -o lex.o $(CFLAGS)

token.o : token.cpp token.h
	g++ -c -g token.cpp -o token.o $(CFLAGS)

filename.o : filename.h filename.cpp
	g++ -c -g filename.cpp -o filename.o $(CFLAGS)

memtest : clean Tokenizer
	valgrind -v --leak-check=full --log-file=valgrind-results.txt ./Tokenizer testFile.txt

test : clean Tokenizer
	./Tokenizer testFile.txt outFile.txt

clean :
	rm -f *.o lex.yy.cpp *~ Tokenizer outFile*.txt valgrind-results.txt
