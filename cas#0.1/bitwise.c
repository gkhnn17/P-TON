#include<stdio.h>
/*
reg = 0b011001011;

reg = reg|4;
reg |= (1<<2) //2bit 1 kere sola

reg |=(1<<6) | (1<<5)
reg ^=(1<<2) //belli bit değişir
*/
int main()
{

unsigned int x;
printf("bir tam sayi giriniz: ");
scanf("%u", &x);
bprint(x);
bprint(~x);
printf("x = %u\n", x);
}