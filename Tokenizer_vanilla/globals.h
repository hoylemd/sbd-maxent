/******************************************************************************
 * Header file for Tokenizer application
 * 	Written by Michael D. Hoyle
 * 	hoylemd@gmail.com
 * ***************************************************************************/

// Standard includes for all files
#ifndef STD_INCLUDES
using namespace std;
#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#define STD_INCLUDES
#endif

// local includes
#ifndef LOCAL_INCLUDES
#include "token.h"
#include "context.h"
#define LOCAL_INCLUDES
#endif

/* declaration of io streams */
#ifndef IOSTREAMS
#define IOSTREAMS
extern FILE * source;
#endif

/* declaration of macros */
#define TRUE 256
#define FALSE 0

// Prototype for getToken routine
// Is used to get the next token from the stream and generate an object for it.
Token * getToken();
Token * getTokenList();