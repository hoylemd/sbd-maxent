#include "token.h"

using namespace std;

class Context
{
    Token * tokens[7];

public:
    Context(Token *);
    ~Context();

    Token * getList();
};