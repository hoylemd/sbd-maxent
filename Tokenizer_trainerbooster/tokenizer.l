%{
    // Include the global header
    #include "globals.h"
%}

whitespace    [ \t]+
newline        [\n]+
valid        [^ \t\n.?!]+
punctuation    [.?!]
candidate    {valid}*{punctuation}+{valid}*

%%
">>>END<<<"         { return 0;}
"$DOC"              { return DOC;}
"$"{valid}          { return TAG;}
{valid}             { return TOKEN;}
{candidate}         { return CANDIDATE;}
{whitespace}        { return WHITESPACE;}
{newline}           { return NEWLINE;}

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
    tokenType type;
    string * lexText;
    Token * returner = NULL;
    static int firstTime = TRUE;
    static int done = FALSE;

    if (firstTime)
    {
        firstTime = FALSE;
        if (source) yyin = source;
    }
    
    if (!done)
    {
        //printf("parsing\n");
        // get the data from the scanner.
        type = (tokenType)yylex();
        lexText = new string(yytext);

        // construct the token, if any
        if (type)
            returner = new Token((tokenType)type,lexText);
        else
        {
            //printf("EOF found\n");
            done = true;
            returner = NULL;
        }
        // clean up
        delete lexText;
    }

    // return
    return returner;

}

