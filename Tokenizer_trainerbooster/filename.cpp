// File name class
#include "filename.h"

FileName::FileName(string * prefix, string * suffix)
{
	this->prefix = new string(*prefix);
	this->suffix = new string(*suffix);
	this->number = 0;
}

FileName::FileName(string * raw)
{
	int indexOfPeriod = 0;

	// split it up into it's components
	indexOfPeriod = raw->find_last_of('.');
	prefix = new string(raw->substr(0, indexOfPeriod));
	suffix = new string(raw->substr(
		indexOfPeriod, MAXFILEEXTENSIONLENGTH));
}

FileName::~FileName()
{
	delete prefix;
	delete suffix;
}

string * FileName::nextFile()
{
	string *out = new string();
	string *outNumber = intToString(number);
	number++;
	*out += *prefix + *outNumber + *suffix;
	delete outNumber;
	return out;
}

string * FileName::plain()
{
	string *out = new string();
	*out += *prefix + *suffix;
	return out;
}

// Function to make a string out of an int.
string * intToString(int i)
{
	stringstream ss;
	ss << i;
	return new string(ss.str());
}
