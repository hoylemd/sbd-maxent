#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

const int MAX_LINE_LENGTH = 65536;

int getSample( int argc, const char *argv[] ) {

  if( argc != 4 ) {
    cerr << "Usage: " << argv[0] << " <number> <total> <infile>" << endl;
    return -1;
  }

  int number = atoi( argv[1] );
  if( number <= 0 ) {
    cerr << "Number must be greater than 0" << endl;
    return -1;
  }

  int total = atoi( argv[2] );
  if( number >= total ) {
    cerr << "Number must be smaller than total" << endl;
    return -1;
  }

  map<int, bool> numberMap;
  map<int, bool>::iterator iter;
  srandom( time(0) );
  int count = 0;
  for( ; ; ) {
    double rand = random() * 1.0 / RAND_MAX;
    int num = (int)(rand * total);
    iter = numberMap.find( num );
    if( iter == numberMap.end() ) {
      numberMap[num] = true;
      count++;
    } 
    if( count == number )
      break;
  }

  //for( iter = numberMap.begin(); iter != numberMap.end(); iter++ )
  //  cout << "random: " << iter->first << endl;

  ifstream fin( argv[3] );
  if( !fin ) {
    cerr << "Can't open file " << argv[3] << endl;
    return -1;
  }

  char line[MAX_LINE_LENGTH];
  count = 0;
  for( int i = 0;  
       fin.getline(line, MAX_LINE_LENGTH - 10) && count < number; 
       i++ ) {
    iter = numberMap.find( i );
    if( iter != numberMap.end() ) {
      cout << line << endl; 
      count++;
    }
  }

  fin.close();

  return 0;
}

int main( int argc, const char *argv[] )
{
	return getSample(argc, argv);
}
