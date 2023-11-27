#include<stdio.h>

int main(){

/*
    printf("hello");

return 0 ;//döndürme işlemi

*/

//gcc -o.ornek.out ornek.c
// => ./ornek.out

/*
    # => ön işlem

*/

// bit AND(&) bitsel OR(|) EXOR(^)

    unsigned int a = 10 ; //Dec : 10 Binary: 1010 Hex:A     0 + 2^1 + 0 + 2^3 
    unsigned int b = 5 ;  //DEc  : 5 Binary: 0101 Hex:5     2^0 + 0 + 2^2 + 0 
    unsigned int c = a&b ; // 0000 == 0
    unsigned int d = a|b ;// 1111  == 15 Hex:F
    unsigned int e = a^b; // 1111 == 15

    printf("Bitsel and:%u \n",c);
    printf("Bitsel or:%u \n",d);
    printf("Bitsel xor:%u \n",e);
    printf("Bitsel xor:%x \n",e);  //%x harfi göster
//Birsel kaydırma sola kaydır << 2 ile çarp  ,  >> sağa kaydır 2 ye böl

    a<<=2 ;  
    printf ("%d\n",a);










}