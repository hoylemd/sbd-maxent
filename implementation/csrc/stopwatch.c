/*
**	stopwatch - calculates elapsed time between events
**
**	File:    stopwatch.c
**	Author:  John Fitzgibbon (fitz@jfitz.com http://www.jfitz.com)
**	Version: 1.0
**	Date:    11/08/1999
**
**	This program and code is FREEWARE.
**
**  Command line format:
**      stopwatch start > timestamp.txt
**      stopwatch stop < timestamp.txt
**
**  Revision History
**  2006-04-11 1.0 Original Version
*/

char helpstr[] =
"\n"
"stopwatch - calculates the elapsed time between events \n"
"\n"
"syntax is: stopwatch start > timestamp.txt\n"
"       or: stopwatch stop < timestamp.txt\n"
"\n"
"When the stop command is issued, the elapsed time in seconds is printed.\n"
;

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

int main (int argc, char * argv[])
{
    time_t now;

    if ((argc <= 1) || (strcmp(argv[1],"start") && strcmp(argv[1],"stop")))
    {
        printf(helpstr);
        exit(0);
    }

    time(&now);

    if (!strcmp(argv[1],"start"))
    {
        printf("%lu\n",now);
    }
    else
    {
        char buf[100];
        time_t start;

        fgets(buf,100,stdin);
        start = atol(buf);
        now -= start;
        printf("%lu\n",now);
    }

    return (0);
}


