// Include the global header
#include "globals.h"

// define the IOstreams
FILE * source = NULL;

// main routine
int main(int argc, char* argv[])
{
	// Local variables
	string * dummy = new string("");
	Token * result;

	// open source file if any.
	if (argc > 1)
	{
		source = fopen(argv[1], "r");
	}

    result = getTokenList();

	result->outputList(dummy);

	// clean up
    delete result;
    delete dummy;
	if (source) fclose(source);
}