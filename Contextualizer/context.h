#include "token.h"

// debug macros. comment out to disable debug messages
// #define DEBUGCONTEXT 1

using namespace std;

class Context
{
    Token * tokens[7];
	int isEOS;
	
public:
    Context(Token *);
    ~Context();

    Token * getList();
	int isEndOfSentence();
	void setEndOfSentence(int);
	void output(ostream *, string * delimiter);
};
