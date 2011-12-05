/***************************************************************************
 * Tokenizer lex file for Tokenizer application
 *		Written by Michael D. Hoyle
 *		hoylemd@gmail.com
 * ************************************************************************/

%{
	/* Include the global header */
	#include "globals.h"
%}

whitespace		[ \t\n]+
valid			[^ \t\n.?!]+
punctuation		[.?!]
candidate		[^ \t\n]+

%option nounput
%%

{valid}			{ return TOKEN;}
{candidate}\n	{ return ENDOFSENTENCE;}
{candidate}		{ return FALSEEND;}
{whitespace}	{ /*return WHITESPACE*/;}

%%

/* Handle any errors */
void yyerror(const char *str)
{
	fprintf(stderr, "error: %s\n", str);
	exit(0);
}

/* handle document wrapping: just say no. */
int yywrap()
{
	return 1;
}

/* routine to get the next token and return a useable token object */
Token * getToken()
{
	static int firstTime = TRUE;

	/* set up input if it's the first time */
	if (firstTime)
	{
		firstTime = FALSE;
		if (source) yyin = source;
	}

	/* get the data from the scanner. */
	tokenType type = (tokenType)yylex();
	string * lexText = new string(yytext);
	string * stripped = new string(
		lexText->substr(0, (lexText->length() -1)));
	Token * returner = NULL;

	/* construct the token, if any. */
	if (type)
	{	
		if (type == ENDOFSENTENCE)
			returner = new Token((tokenType)type, stripped);
		else
			returner = new Token((tokenType)type,lexText);
	}

	/* clean up */
	delete lexText;
	delete stripped;

	/* return */
	return returner;

}

/* routine to construct a list of tokens using the defined lexer. */
Token * getTokenList()
{
    Token * list = NULL, * temp, *end, *temp2;
	string * newString;

	/* keep adding to the list as long as there are tokens. */
    while((temp = getToken()))
    {

		/* handle the first token */
        if (!list)
        {
            list = temp;
            end = list;
        }

		/* handle all following tokens */
        else
        {	
			/* debugging output */
			/* cout << *temp->toString() << endl; */
	
			/* Check if we got just an EOS punctiation character, and stick
			it to the last token.*/
			if 	(((temp->getType() == ENDOFSENTENCE) || 
					(temp->getType() == FALSEEND)) &&
				 (temp->getValue()->size() == 1))
			{

				/* glue the single punctuation to the end of the preceeding 
				token's string.*/
				newString = new string(*end->getValue() + *temp->getValue());

				/* set the preceeding token's type accordingly */
				temp = new Token(ENDOFSENTENCE, newString);
				
				temp2 = end->getPrev();
				delete end;
				end = temp2;
			}
			
			/* add the new token to the list and advance */  
		 	end->concat(temp);
           	end = temp;
			
        }
    }

	/* throw back the list */
    return list;
}

