// Include the global header
#include "globals.h"

// define the IOstreams
FILE * source = NULL;
ostream * dest = NULL;

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
		source = fopen(argv[1], "r");
	else
		source = stdin;
	if (argc > 2)
		dest = new fstream(argv[2], fstream::in | fstream::out);
	else
		dest = &cout;
	
    result = getTokenList();


    // Handle the tokens
    temp = result;
    while (temp)
    {
//		cerr << "handling token " << temp->getValue()->data() << endl;
        if (temp->getType() == CANDIDATE)
            checkForBoundary(temp);

        temp = temp->getNext();
    }

	//result->outputList(dummy);

	// clean up
    delete result;
    delete dummy;
	if (source) fclose(source);
}

bool checkForBoundary(Token * candidate)
{
    Context * context = new Context(candidate);
	string * delimiter = new string (" ");
	
    context->output(dest, delimiter);

	*dest << endl;	

	delete delimiter;	

    return false;
}
