#include <string.h>
#include <stdlib.h>
#include <stdio.h>
void mycpy(char* str)
{   
  char foo[24];   
  strcpy(foo, str);
  //printf("foo = %s\n",foo);
}

int main(int argc,char* argv[])
{   
  mycpy(argv[1]);   
  printf("Done\n");   
  return 0;
}

