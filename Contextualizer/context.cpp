#include "context.h"

// Constructor
Context::Context(Token * candidate)
{
    Token * temp = candidate;
    Token * head;

	this->isEOS = false;

    // add the radix
    this->tokens[3] = new Token(candidate);

	// add the prefix
	temp = candidate;
    if ((temp = temp->getPrev()))
    {
        this->tokens[2] = new Token(temp);

        if ((temp = temp->getPrev()))
        {
            this->tokens[1] = new Token (temp);

            if ((temp = temp->getPrev()))
            {
                this->tokens[0] = new Token (temp);
                temp = this->tokens[0];
            }
            else
			{
                this->tokens[0] = NULL;
			}
            if (temp) temp->concat(this->tokens[1]);
            temp = this->tokens[1];
        }
        else
        {
            this->tokens[0] = NULL;
            this->tokens[1] = NULL;
        }

        if (temp) temp->concat(this->tokens[2]);
        temp = this->tokens[2];
    }
    else
    {
        this->tokens[0] = NULL;
        this->tokens[1] = NULL;
        this->tokens[2] = NULL;
    }

    if (temp) temp->concat(this->tokens[3]);
    head = this->tokens[3];
    temp = candidate;

    if ((temp = temp->getNext()))
    {
        this->tokens[4] = new Token(temp);
        head->concat(this->tokens[4]);

        if ((temp = temp->getNext()))
        {
            this->tokens[5] = new Token (temp);
            head->concat(this->tokens[5]);

            if ((temp = temp->getNext()))
            {
                this->tokens[6] = new Token (temp);
                head->concat(this->tokens[6]);
            }
            else
                this->tokens[6] = NULL;
        }
        else
        {
            this->tokens[6] = NULL;
            this->tokens[5] = NULL;
        }
    }
    else
    {
        this->tokens[6] = NULL;
        this->tokens[5] = NULL;
        this->tokens[4] = NULL;
    }
}

// Destructor
Context::~Context()
{
    int i = 0;
    for (i=0; i < 7; i++)
    {
        if (this->tokens[i]) delete tokens[i];
    }
}

// function to get the list of tokens in this context
Token * Context::getList(void)
{
    if (tokens[0]) return tokens[0];
    else
    {
        if (tokens[1]) return tokens[1];
        else
        {
            if (tokens[2]) return tokens[2];
        }
    }
	return tokens[3];
}

// accessor for end-of-sentence state
int Context::isEndOfSentence(void)
{
	return this->isEOS;
}

// mutator for end-of-sentence state
void Context::setEndOfSentence(int newValue)
{
	this->isEOS = newValue;
}

// function to output this context as a string
void Context::output(ostream * out, string * delimiter)
{
	int i = 0;
	Token * current;
	string * blankToken = new string("</>");

	#ifdef DEBUGCONTEXT
	cerr << "outputting context to stream, using '" << delimiter->data() << "' as a delimiter.\n";
	#endif

	for (i = 0; i < 7; i++)
	{
	
		current = this->tokens[i];
		if (current)
			*out << *current->getValue();
		else
			*out << *blankToken;
	
		*out << *delimiter;
	}

	if (this->isEOS)
		*out << "<Y>";
	else
		*out << "<N>";

	delete blankToken;

}
