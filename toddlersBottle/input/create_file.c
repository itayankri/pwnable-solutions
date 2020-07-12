#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char* argv[]) {
	// file
	FILE* fp = fopen("\x0a", "w+");
	if(!fp) {
		printf("File could not be opened\n");
		return 0;
	}

	printf("file descriptor: %d\n", fileno(fp));

	char buf[4];
	
	int bytes = fread(buf, 4, 1, fp);
	printf("bytes that has been red: %d\n", bytes);
	
	if( bytes != 1 ) {
		printf("Could not read from file\n");
		return 0;
	}

	if( memcmp(buf, "\x00\x00\x00\x00", 4) ) {
		printf("The data is not equal\n");
		return 0;
	}

	fclose(fp);
	printf("Stage 4 clear!\n");
}
