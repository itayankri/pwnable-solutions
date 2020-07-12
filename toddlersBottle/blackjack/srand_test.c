#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
	int x;
	srand((unsigned) time(NULL));
	x = rand()%13+1;
	printf("Random 1: %d | time: %u\n", x, (unsigned)time(NULL));
	srand((unsigned) time(NULL) + 1);
	x = rand()%13+1;
	printf("Random 2: %d | time: %u\n", x, (unsigned)time(NULL) + 1);
}
