#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, char* argv[])
{
	char* buf = argv[1];
	//printf("%s\n", buf);
	char command[30] = "cat ";
	strcat(command, buf);
	printf("%s\n", command);
	system(command);
	return 0;
}
