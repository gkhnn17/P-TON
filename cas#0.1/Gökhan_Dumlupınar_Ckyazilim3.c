#include <stdio.h>
#include <stdint.h>

int main() {
    int sesDuzeyi = 72;
    int sarkiSayisi = 12;
    int sureYuzdesi = 33;
    int pilYuzdesi = 40;

    uint16_t reg = 0;
    reg |= (sesDuzeyi & 0x000F) << 12;
    reg |= (sarkiSayisi & 0x000F) << 8;
    reg |= (sureYuzdesi  & 0x000F) << 4;
    reg |= pilYuzdesi  & 0x000F;
    
    printf("Ses Düzeyi: %d\n", sesDuzeyi);
    printf("Hafızadaki Şarkı Sayısı: %d\n", sarkiSayisi);
    printf("Süre: %d\n", sureYuzdesi );
    printf("Pil Yüzdesi: %d\n", pilYuzdesi) ;
    
    return 0;
}


