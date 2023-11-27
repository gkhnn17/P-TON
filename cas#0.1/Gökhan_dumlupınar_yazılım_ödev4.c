#include <stdio.h>

int main() {
    float boy,kilo,vki;
    printf("kilo");
    scanf("%f",&kilo);
    printf("boy");
    scanf("%f9",&boy);
    vki = kilo / (boy * boy);
   if (vki < 18.5) {
        printf("Zayif.\n");
    } else if (vki < 25) {
        printf("Normal.\n");
    } else if (vki < 30) {
        printf("Fazla kilolu.\n");
    } else {
        printf("Obez.\n");
    }
    return 0;

}
