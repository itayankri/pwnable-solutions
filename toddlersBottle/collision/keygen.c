#include <stdio.h>
#include <string.h>
#include <stdlib.h>

unsigned long hashcode = 0x21DD09EC;
unsigned long check_password(const char* p){
        int* ip = (int*)p;
        int i;
        int res=0;
        for(i=0; i<5; i++){
                res += ip[i];
        }
        return res;
}

int main(int argc, char* argv[]) {
	time_t t;
	char pass[20];
	int s;

	//srand((unsigned) time(&t));

	//while (1) {
	//	for (int i = 0; i < 20; i++ ) {
	//		int rand_num = (rand() % 94) + 32;
	//		pass[i] = (char)rand_num;
	//		// printf("%d | %c\n", rand_num, (char)rand_num);
	//	}
	//	
	//	s = check_password(pass);
	//	if (hashcode == s) {
	//		printf("Founa a valid password - %s\n", pass);
	//		break;
	//	} else {
	//		printf("%d | %x\n", s, s);
	//	}
	//}

	s = check_password(argv[1]);
	printf("%x, %d\n", s, s);

	return 0;
}
