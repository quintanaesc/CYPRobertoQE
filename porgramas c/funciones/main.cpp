#include <stdio.h>
#include "bibliotecas.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int sumar(int a ,int b){
	int c= a+b;
	return c;
}
int main(int argc, char** argv) {
	printf("la suma de 3 y 4es: %d",sumar(3,4));
	printa_A();
	return 0;
}
