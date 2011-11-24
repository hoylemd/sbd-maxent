// Include the global header
#include "globals.h"

// define the IOstreams
FILE * source = NULL;
FILE * classificationFile = NULL;
ostream * dest = NULL;

bool checkForBoundary(Token *);

// main routine
int main(int argc, char* argv[])
{
	// Local variables
	string * dummy = new string("");
	Token * result;
    Token * temp;
    char inString[5];
    char classChar = 0;
    char classChars[100000];
    int numClasses = 0;
    int classIndex = 0;
	fstream * actualFile = NULL;

    if (argc != 2)
    {
        printf("Usage:\n\t./Replacer <classification file>\n");
        return -1;
    }

    // set up the source & destination streams (stdin/out)
    source = stdin;
    dest = &cout;

    classificationFile = fopen(argv[1], "r");
    // get the list of tokens
    result = getTokenList();

    // get the list of classifications
    while (!feof(classificationFile))
    {
        fscanf(classificationFile, "%s", inString);
        classChar = inString[0];
        classChars[numClasses] = classChar;
        classChars[numClasses+1] = 0;
        numClasses++;
    }

    // Handle the tokens
    temp = result;
    classIndex = 0;
    while (temp)
    {
        printf("%s", temp->getValue()->data());
		//cerr << "handling token " << *temp->toString() << endl;
        if (temp->getType() == FALSEEND || temp->getType() == ENDOFSENTENCE)
        {
            if (classChars[classIndex] == 'y')
               printf("\n");
            else
                printf(" ");
            classIndex++;
        }
        else
            printf(" ");

        temp = temp->getNext();
    }


// clean up
    delete result;
    delete dummy;
	if (source) fclose(source);
	if (actualFile) actualFile->close();
}
