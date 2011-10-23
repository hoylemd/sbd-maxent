// Include the global header
#include "globals.h"

// define the IOstreams
FILE * source = NULL;

bool checkForBoundary(Token *);

// main routine
int main(int argc, char* argv[])
{
	// Local variables
	string * dummy = new string("");
	Token * result;
    Token * temp;

	// open source file if any.
	if (argc > 1)
	{
		source = fopen(argv[1], "r");
	}

    result = getTokenList();

    // Handle the tokens
    // test the conext construction first
    temp = result;
    checkForBoundary(temp);
    temp = temp->getNext();
    checkForBoundary(temp);
    temp = temp->getNext();
    checkForBoundary(temp);
    temp = temp->getNext();
    checkForBoundary(temp);

    while (temp->getNext())
        temp = temp->getNext();

    checkForBoundary(temp);
    temp = temp->getPrev();
    checkForBoundary(temp);
    temp = temp->getPrev();
    checkForBoundary(temp);
    temp = temp->getPrev();
    checkForBoundary(temp);

	//result->outputList(dummy);

	// clean up
    delete result;
    delete dummy;
	if (source) fclose(source);
}

bool checkForBoundary(Token * candidate)
{
    Context * context = new Context(candidate);

    context->getList()->outputList(new string("|"));
    cout << endl;


    return false;
}