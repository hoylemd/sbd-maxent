/******************************************************************************
 * Token class for Tokenizer application
 *     Written by Michael D. Hoyle
 *     hoylemd@gmail.com
 * ***************************************************************************/

#include "globals.h"
#include <cstdio>
// Constructor
Token::Token(tokenType type, string * value)
{
    this->value = new string(*value);
    this->type = type;
}

// Destructor
Token::~Token()
{
    if (value) delete value;
    next = NULL;
    value = NULL;
}

// static method to get the name of a token type
string * Token::typeToString(tokenType type)
{
    switch(type)
    {
        case(TOKEN):
        {
            return new string("Token");
            break;
        }
        case(CANDIDATE):
        {
            return new string("Candidate");
            break;
        }
        case(WHITESPACE):
        {
            return new string("Whitespace");
            break;
        }
        case(NEWLINE):
        {
            return new string("Newline");
            break;
        }
        case(DOC):
        {
            return new string("Doc Marker");
            break;
        }
        case(TAG):
        {
            return new string("Tag");
            break;
        }
        case(NONE):
        {
            return new string("None");
        }
        default:
        {
            return new string("Unrecognized");
        }
    }
}

// Accessor for value
string * Token::getValue()
{
    return this->value;
}

// Accessor for type
tokenType Token::getType()
{
    return this->type;
}

// Mutator for next
void Token::setNext(Token * tok)
{
    this->next = tok;
}

// Accessor for next
Token * Token::getNext()
{
    return this->next;
}

// Stringer
string * Token::toString()
{
    int i = 0;
    string * returner = new string();
    string * typeName = NULL;

    // get the string for the type name
    typeName = typeToString(this->type);

    // construct the return string
    returner->append("{");
    returner->append(*typeName);
    returner->append("}\"");
    returner->append(*this->value);
    returner->append("\"");

    // clean up
    delete typeName;

    // return the string
    return returner;
}
