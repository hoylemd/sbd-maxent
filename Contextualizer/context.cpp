#include "context.h"

// Constructor
Context::Context(Token * candidate)
{
    Token * temp = candidate;
    Token * head;
    // populate the context

    // see if there are 3
    this->tokens[3] = new Token(candidate);

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
                this->tokens[0] = NULL;

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
            else return tokens[3];
        }
    }
}

// function to output this context as a string
string * Context::output(ostream * out, string * delimiter)
{
	int i = 0;
	int first = 1;	
	Token * current;
	string * blankToken = new string("<//>");

	for (i = 0; i < 6; i++)
	{
		current = this->tokens[i];
		if (current)
			*out << current->getValue();
		else
			*out << *blankToken;

		if (first)
			first = 0;
		else
			*out << *delimiter;
	}

	delete blankToken;

}
