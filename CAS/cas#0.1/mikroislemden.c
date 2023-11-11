#include<stdio.h>
#include <stdint.h>

typedef struct {
    int bits[4]; // 4 bitlik bir dizi
} BinaryNumber;
//her bit 25 i temsil eder ve değerin hangi değer aralığında olduğu belirtilir
BinaryNumber ConvertToBinary(int number) {
    BinaryNumber binary;
    
    for (int i = 0; i < 4; i++) {
        binary.bits[i] = number >= 25;
        number -= 25;
    }
    
    return binary;
}


void PrintBinary(BinaryNumber binary) {
    for (int i = 3; i >= 0; i--) {
        printf("%d", binary.bits[i]);
    }
    printf("\n");
}


int main() {
    //değerler
    int ses = 72;
    int sarki_sayisi =12;
    int sure = 33;
    int pil_yuzde = 40; 
    BinaryNumber sesbin = ConvertToBinary(ses);
    PrintBinary(sesbin);

    printf("BU UYGULAMA SiSTEMiN 0-25,25,50,50-75,75-100 ARASiNDAKi DEgERLERi BELiRTiR ");
    
    //kolay işlem için başta verilen işlemciyi sıfırlanır
    uint16_t reg = 0b0110010111001011;
    reg &= ~reg;

    uint8_t sesDuzeyi = 0;
    for (int i = 0; i < 4; i++) {
        sesDuzeyi |= (sesbin.bits[i] << i);
    } 
    sesDuzeyi = (reg | sesDuzeyi) >> 12;
    printf("%d",reg);
    return 0;

}


/*void degeroku(BinaryNumber binary){
    if (binary == 0000) {
        prinf("0-25");
    }
    else if (binary == 0001)
    {
        prinf("25-50");
    }
    else if (binary == 0011)
    {
        prinf("50-75");
    }
    else if (binary == 0111)
    {
        prinf("75-100");
    }
    else{
        prinf("full");
    }
    

}*/