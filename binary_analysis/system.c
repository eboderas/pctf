#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char* argv[])
{
	char buff[20];
	strcpy(buff, "/bin/cat");
	execl(buff,buff,argv[1],NULL);
	return 0;
}
