#include <iostream>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	int i;
	int a;
	for (i=1;i<12;i+=2){
		printf("hola %d\n",i);
	}
	for(a=0;a<5;a+=1){
		for(i=0;i<10;i+=1){
			printf("#");
		}
		printf("\n");
	}
	printf("\n");
	for(a=0;a<5;a+=1){
		for(i=0;i<10;i+=1){
			if(a==0||a==4||i==0||i==9){
			printf("#");
			}
			else{
				printf(" ");
			}
		}
		printf("\n");
	}
	
	return 0;
}

