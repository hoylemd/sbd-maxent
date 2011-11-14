/******************************************************************************
 * Token class for Tokenizer application
 *     Written by Michael D. Hoyle
 *     hoylemd@gmail.com
 * ***************************************************************************/

using namespace std;
#include "token.h"
// Constructor
Token::Token(tokenType type, string * value)
{
	this->next = NULL;
	this->prev = NULL;
    this->value = new string(*value);
    this->type = type;
}

// Copy constructor
Token::Token(Token * other)
{
    if (other)
    {
		this->next = NULL;
		this->prev = NULL;
        this->value = new string(*(other->getValue()));
        this->type = other->getType();
    }
    else
    {
        cerr << "attempt to copy a null token.";
        exit(0);
    }
}

// Destructor
Token::~Token()
{
    if (value) delete value;
    next = NULL;
    prev = NULL;
    value = NULL;
}

// static method to get the name of a token type
string * Token::typeToString(tokenType type)
{
    switch(type)
    {
        case TOKEN :        return new string("Token");
        case WHITESPACE :   return new string("Whitespace");
        case NONE:          return new string("None");
        default:            return new string("Unknown");
    }
}

// Attacher
// attaches the provided lists to one another
Token * Token::attachLists(Token * head, Token * list)
{
	
    Token * headFoot = head;
	#ifdef DEBUGTOKENS
	cerr << "attaching lists";
	if (head) cerr << " head exists,";
	else cerr << " head DNE!!!!,";
	if (list) cerr << " list exists." << endl;
	else cerr << " list DNE!!!!." << endl;
    #endif
	// find the end of the new head
    while (headFoot->getNext())
	{
        headFoot = headFoot->getNext();
	}

    // attach this to it
    list->setPrev(headFoot);
    headFoot->setNext(list);

    return head;
}

// Accessor for value
string * Token::getValue()
{
    return this->value;
}

// Mutator for value

void Token::replaceValue(string * newS)
{
    delete this->value;
    this->value = new string(*newS);
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
	#ifdef DEBUGTOKENS
	if (this->next) cerr << "getting next. exists.\n";
	else cerr << "getting next. DNE!\n";
	#endif
    return this->next;
}

// Mutator for prev
void Token::setPrev(Token * tok)
{
    this->prev = tok;
}

// Accessor for prev
Token * Token::getPrev()
{
    return this->prev;
}

// Appender
// adds this list to the provided list
// returns the new head of the list
Token * Token::append(Token * head)
{
    return Token::attachLists(head, this);
}

// Concatenator
// adds the provided list to the end of this one
// returns the new head of the list
Token * Token::concat(Token * list)
{
    return Token::attachLists(this, list);
}

// Stringer
string * Token::toString()
{
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


// Outputter
void Token::outputList(string * delimiter)
{
    Token * current = this;
    string *outString;

    outString = current->getValue();
    cout << *outString;
    current = current->getNext();

    while (current)
    {
        cout << *delimiter;
        outString = current->getValue();
        cout << *outString;
        current = current->getNext();
    }
}

// Outputter
void Token::outputList(ostream * out, string * delimiter)
{
    Token * current = this;
    string *outString;

    outString = current->getValue();
    *out << *outString;
    current = current->getNext();

    while (current)
    {
        *out << *delimiter;
        outString = current->getValue();
        *out << *outString;
        current = current->getNext();
    }

}
