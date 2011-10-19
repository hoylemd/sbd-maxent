/******************************************************************************
 * Token class for Tokenizer application
 * 	Written by Michael D. Hoyle
 * 	hoylemd@gmail.com
 * ***************************************************************************/

#include "globals.h"

// Constructor
Token::Token(tokenType type, string * value)
{
	this->value = value;
	this->type = type;
}

// Destructor
Token::~Token()
{
	if (value) delete value;
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

// Stringer
string * Token::toString()
{
	int i = 0;
	string * returner = new string();
	string * typeName = NULL;

	// get the string for the type name
	typeName = typeToString(this->type);

	// construct the return string
	returner->append("{\0");
	returner->append(*typeName);
	returner->append("}\"\0");
	returner->append(*this->value);
	returner->append("\"");

	// clean up
	delete typeName;

	// return the string
	return returner;
}