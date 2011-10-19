// File name class header
using namespace std;

#include <string>
#include <sstream>

#define MAXFILEEXTENSIONLENGTH 16

class FileName
{
	string * prefix;
	string * suffix;
	int number;

	public:
		FileName(string *, string *);
		FileName(string *);
		~FileName();

		string * nextFile();
		string * plain();
};

// Prototype for intToString routine.
string * intToString(int);