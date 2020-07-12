#include <stdio.h>

size_t fread(void *ptr, size_t size, size_t nmemb, FILE *stream) {
	printf("Injection\n");
	*((char*)ptr) = '\x00';
	*((char*)ptr+1) = '\x00';
	*((char*)ptr+2) = '\x00';
	*((char*)ptr+3) = '\x00';
	return 1;
}
