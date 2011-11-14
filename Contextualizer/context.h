#include "token.h"

// debug macros. comment out to disable debug messages
// #define DEBUGCONTEXT 1

using namespace std;

class Context
{
    Token * tokens[7];

public:
    Context(Token *);
    ~Context();

    Token * getList();
	void output(ostream *, string * delimiter);
};
