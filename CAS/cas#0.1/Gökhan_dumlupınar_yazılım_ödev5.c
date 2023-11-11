#include <stdio.h>
#include<math.h>

int main(){
    int hamnot[10];
    int birinci_v_ort = 0 ;
    int ikinci_v_ort = 0 ;
    int ucuncu_v_ort = 0 ;
    int hamnot_ort = 0 ;
    char isimler[10][9]= {"ozgur","ozay ","selen","Begum",   "Sema", "Melih", "Batuhan", "Ahmet", "Amiraslan", "Mubariz"   };
    int birinci_v[10] = {14, 82, 22, 70, 74, 81, 25, 43, 48, 29};
    int ikinci_v[10] = {50, 85, 72, 64, 80, 66, 34, 25, 61, 30};
    int ucuncu_v[10]= {43,70,52,35,45,73,28,33,82,65};
    
    //hamnot
    for (int j = 0;j <10 ;j++){
    hamnot[j]= round((birinci_v[j]*30/100)+(ikinci_v[j]*30/100)+(ucuncu_v[j]*40/100));
    }
    for(int d = 0 ;d<10 ;d++){
     hamnot_ort += hamnot[d]/10;
    }

    //birinci_v_ort
    printf("%s\n","notunuz");
    for(int a = 0 ; a <10 ; a ++){
        if (hamnot[a]<hamnot_ort-15){
           printf("%s,  " ,isimler[a]);
           printf(" %d ,  ",hamnot[a]);
           printf("%s\n","FF");
        }       
         else if(hamnot[a]<hamnot_ort-10){
            printf("%s" ,isimler[a]);
            printf("%d ,  ",hamnot[a]);
            printf("%s\n","FD");
        
         }
        else if(hamnot[a]<hamnot_ort-5){
            printf("%s" ,isimler[a]);
            printf("%d ,  ",hamnot[a]);
            printf("%s\n","DD");
        
         }
        else if(hamnot[a]<hamnot_ort){
            printf("%s" ,isimler[a]);
            printf("%d ,  ",hamnot[a]);
            printf("%s\n","DC");
        
         }
        else if(hamnot[a]<hamnot_ort+5){
            printf("%s" ,isimler[a]);
            printf("%d ,  ",hamnot[a]);
            printf("%s\n","CC");
        
         }
        else if(hamnot[a]<hamnot_ort+10){
            printf("%s" ,isimler[a]);
            printf("%d ,  ",hamnot[a]);
            printf("%s\n","CB");
        
         }
        else if(hamnot[a]<hamnot_ort+15){
            printf("%s" ,isimler[a]);
            printf("%d ,  ",hamnot[a]);
            printf("%s\n","BB");
        
         }
         else if(hamnot[a]<hamnot_ort+20){
            printf("%s" ,isimler[a]);
            printf("%d ,  ",hamnot[a]);
            printf("%s\n","BA");
        
         }
        else{
            printf("%s" ,isimler[a]);
            printf("%d ,  ",hamnot[a]);
            printf("%s\n","AA");
        
         }
  

    }
}
