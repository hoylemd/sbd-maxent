// Include the global header
#include "globals.h"

// define the IOstreams
FILE * source = NULL;

// main routine
int main(int argc, char* argv[])
{
	// Local variables
	string * resultString;
	Token * result;

	// open source file if any.
	if (argc > 1)
	{
		source = fopen(argv[1], "r");
	}

	// parse the tokens
	while(result = getToken())
	{
		resultString = result->toString();
		cout << *resultString << '\n';
		delete resultString;
	}

	// clean up
	if (source) fclose(source);
}