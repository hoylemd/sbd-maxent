// Include the global header
#include "globals.h"

// include file io libs
#include <fstream>

// define the IOstreams
FILE * source = NULL;

// main routine
int main(int argc, char* argv[])
{
    // Local variables
    string * resultString;
    string * filePath;
    Token * result;
    Token * tokenList = NULL;
    Token * current;
    ofstream out;
    int ignoreANewline = 0;
    FileName * fileName = NULL;

    // open files
    if (argc > 1)
        source = fopen(argv[1], "r");
    if (argc > 2)
    {
        // set up the fileName object
        filePath = new string(argv[2]);
        fileName = new FileName(filePath);
        delete filePath;

        // open up the output file
        filePath = fileName->nextFile();
        out.open(filePath->data());
        delete filePath;
    }

    // parse the tokens
    while(result = getToken())
    {
        if(tokenList)
        {
            current->setNext(result);
            current = result;
        }
        else
        {
            tokenList = result;
            current = tokenList;
        }
    }

    /*current = tokenList;
    while(current)
    {
        cout << *current->toString();
        current = current->getNext();
    }*/
    
    current = tokenList;

    while(current)
    {
        //cout << current->getType() << " [" << *current->getValue() <<
        //    "]" << endl;
        // handle simple end of sentences
        if (ignoreANewline)
        {
            // get the next token if this one's a newline
            if (current->getType() == NEWLINE)
                if (current->getNext()) current = current->getNext();

            // reset flag
            ignoreANewline = 0;
        }

        // handle all token types
        switch(current->getType())
        {
            case (TOKEN):
            {
                out << *current->getValue();
                
                result = current;
                current = current->getNext();
                delete result;
                break;
            }
            case (CANDIDATE):
            {
                out << *current->getValue() << "\n";
                ignoreANewline = 1;
                
                result = current;
                current = current->getNext();
                delete result;
                break;
            }
            case (WHITESPACE):
            {
                out << " ";
                
                result = current;
                current = current->getNext();
                delete result;
                break;
            }
            case (NEWLINE):
            {
                out << "\n";
                
                result = current;
                current = current->getNext();
                delete result;
                break;
            }
            case (DOC):
            {
                // consume the DOC token
                // consume the next token (it'll be whitespace)
                if (current->getNext()) current = current->getNext();
                // consume the next token too (it'll be a number)
                if (current->getNext()) current = current->getNext();
                // ignore a following newline
                ignoreANewline = 1;

                // close the open output file
                out.close();
                delete filePath;

                // open the next output file
                filePath = fileName->nextFile();
                out.open(filePath->data());
                
                result = current;
                current = current->getNext();
                delete result;
                break;
            }
            case (TAG):
            {
                // consume the token
                // ignore a following newline
                ignoreANewline = 1;
                
                result = current;
                current = current->getNext();
                delete result;
                
                break;
            }
            default:
            {
                result = current;
                current = current->getNext();
                delete result;
                // consume the token
            }
        }
    }

    // clean up
    if (source) fclose(source);
    if (out.is_open()) out.close();
}
