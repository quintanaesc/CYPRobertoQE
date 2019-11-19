#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char *argv[]) {
	int x;
	x=10;
	int y=10;
    printf("hola mundo de programacion en C\n");
    printf("introduce un numero entero");
    scanf("%d",&y);
    printf("\tx vale: %d y Y vale : %d\a",x,y);
    if(y<10){
    	printf("\n%d es mayor a 10",y);
    }
    if(y>10){
        printf("\n%d es menor a 10",y);
	}
	printf("\ncon if_else");
	if(y<10){
		printf("\n%d es mayor a 10",y);
	}
	if(y>10){
		printf("\n%d es mayor a 10",y);
	}
	printf("\nintroduce un valor entre 1 y 5");
	scanf("%d",&x);
	switch(x){
		case 1:
			printf("\nhola");
			break;
		case 2:
			printf("\nAdios");
			break;
		case 3:
			printf("\nhello");
			break;
		case 4:
			printf("\nby");
			break;
		case 5:
			printf("\nguten tag");
			break;
		case 6:
			printf("\bonjorno");
			break;
		default:
			printf("\nopcion no valida");
	}
	return 0;
}
