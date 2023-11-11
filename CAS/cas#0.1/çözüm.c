//
//  main.c
//  linkedList
//
//  Created by Buğra Aslan on 2.04.2023.
//

#include <stdio.h>
#include <stdlib.h>
struct workers{
    char name[25];
    int workHour;
    struct workers * next;
};
typedef struct workers person;

void work(int workTime,int workerAmount ,person*root,person*iter){//Liste uzerinde ilerlemek icin iter baslangıc adresini tutmak icin root'u kullanıcaz.
    for (int i=1;i<=workTime;i++){
        printf("%s 1 saat calisti %d\n",iter->name,i);
        iter->workHour++;
        if(i%(workerAmount)==0 && i != 1){//Listede basa donmek istedigimiz zaman root'u kullanıyoruz
            printf("1 shift gecti\n\n");
            iter=root;
        }
        else{
            iter=iter->next;
        }
    
    }
}
void initialize(int workerAmount,person*root){
    for (int i=0;i<workerAmount;i++){
        scanf("%s",root->name);
        root->workHour=0;
        root->next=(person*)malloc(sizeof(person));//Sonraki adresler icin hafızada yer acıyoruz.
        root=root->next;//Adresleri birbirine baglıyoruzz
    }
}
void printStr(int workerAmount,int workHour,person*root,person*iter){
    for (int i=0;i<workerAmount;i++){
        printf("Name = %s Work Hour=%d\n",iter->name,iter->workHour);

        if(i%workerAmount==0 && i !=0){
            iter=root;
        }
        else{
            iter=iter->next;
        }
    }
}
int main(int argc, const char * argv[]) {
    person*root;
    root=(person*)malloc(sizeof(person)); //Hafızada baslangıc listenin adresi icin yer acıyoruz.
    
    initialize(4, root);
    
    work(15, 4, root, root);
    
    printStr(4, 15, root, root);
    
    return 0;
}
