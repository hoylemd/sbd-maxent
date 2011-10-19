/******************************************************************************
 * Token class header for Tokenizer application
 * 	Written by Michael D. Hoyle
 * 	hoylemd@gmail.com
 * ***************************************************************************/

using namespace std;
#include <cstdlib>
#include <string>

// Token type list.
#ifndef TOKENTYPE
typedef enum
{
	TOKEN = 255,
	CANDIDATE = 254,
	WHITESPACE = 253,
	NONE = 0
} tokenType;
#define TOKENTYPE
#endif

#define MAXTOKENLENGTH 128

class Token
{
	string * value;
	tokenType type;

	public:
		Token(tokenType, string *);
		~Token();

		static string * typeToString(tokenType);

		string * getValue();
		tokenType getType();
		string * toString();
};