%{
	// Include the global header
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

// Handle any errors
void yyerror(const char *str)
{
	fprintf(stderr, "error: %s\n", str);
	exit(0);
}

// handle document wrapping: just say no.
int yywrap()
{
	return 1;
}

// routine to get the next token and return a useable token object
Token * getToken()
{
	static int firstTime = TRUE;

	if (firstTime)
	{
		firstTime = FALSE;
		if (source) yyin = source;
	}

	// get the data from the scanner.
	tokenType type = (tokenType)yylex();
	string * lexText = new string(yytext);
	string * stripped = new string(lexText->substr(0, (lexText->length() -1)));
	Token * returner = NULL;

	// construct the token, if any
	if (type)
	{	
		/*if (type == ENDOFSENTENCE)
		{	
			string * tempString = new string(lexText->substr(0, (lexText->length() - 1)));
			delete lexText;
			lexText = tempString;
		}
		else*/
		if (type == ENDOFSENTENCE)
			returner = new Token((tokenType)type, stripped);
		else
			returner = new Token((tokenType)type,lexText);
	}
	// clean up
	delete lexText;
	delete stripped;

	// return
	return returner;

}

Token * getTokenList()
{
    Token * list = NULL, * temp, *end;

    while((temp = getToken()))
    {
        if (!list)
        {
            list = temp;
            end = list;
        }
        else
        {
            end->concat(temp);
            end = temp;
        }
    }

    return list;

}

