%{
	// Include the global header
	#include "globals.h"
%}

whitespace	[ \t\n]+
valid		[^ \t\n.?!]+
punctuation	[.?!]
candidate	{valid}*{punctuation}+{valid}*

%%

{valid}			{ return TOKEN;}
{candidate}		{ return CANDIDATE;}
{whitespace}	{ return WHITESPACE;}

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
	Token * returner = NULL;

	// construct the token, if any
	if (type)
		returner = new Token((tokenType)type,lexText);

	// clean up
	delete lexText;

	// return
	return returner;

}

Token * getTokenList()
{
    Token * list = NULL, * temp, *end;

    while(temp = getToken())
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

