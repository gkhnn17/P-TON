#include <stdio.h>
#include <stdlib.h>
struct person {
    char isimler[15];
    int main_board_count;
    int bms_count;
    int smart_power_box_count;
    int control_station_count;
    int hydrophone_count;
    int joystick_count;
    struct person* next;
};
enum works{
    MainBoard =15,//1
    BMS = 10,//2
    SmartPowerBox = 7,//3
    ControlStation = 13,//4
    Hydrophone = 8 ,//5
    Joystick = 9 ,//6
};

int main(){
    struct person yasin ={"yasin",0,0,0,0,0,0};
    struct person alper ={"alper",0,0,0,0,0,0};
    struct person eren ={"eren",0,0,0,0,0,0};
    struct person guler ={"guler",0,0,0,0,0,0};

    int mainboard = 0;
    int bms = 0 ;
    int smatpowerbox = 0 ;
    int controlstation = 0 ;
    int hyrdrophone =0;
    int joystick = 0;


    yasin.next = &alper;
    alper.next = &eren;
    eren.next= &guler;
    guler.next = &yasin;
    


    int secim;
    struct person *current = &yasin;
    for(int i = 0 ; i <63 ; i++){

        printf("calisilacak alan seciniz: ");
        scanf("%d",&secim);

        switch (secim) {          
            case 1:
            if(mainboard>MainBoard){
                printf("mainboardda is bitti baska is seciniz");
            continue;
            }
            else{
            current->main_board_count++ ;
            current = current->next; 
            mainboard++ ;                
            }
            break;  
            case 2:
            if(bms>BMS){
                printf("BMS iş bitti başka iş seçiniz");
                continue;
            }
            else{
            current->bms_count++;
            current = current->next;
            bms++;
            break;
            }                           
            case 3:
            if(smatpowerbox>SmartPowerBox){
                printf("smatpowerbox iş bitti başka iş seçiniz");
                continue;
            }            
            else{
            current->smart_power_box_count++;
            current = current->next;
            smatpowerbox++;
            }
            break;
            case 4:
            if(controlstation>ControlStation){
                printf("controlstation iş bitti başka iş seçiniz");
                continue;
            }
            else{
            current->control_station_count++;
            current = current->next;
            controlstation++;
            }
            break;
            case 5:
            if(hyrdrophone>Hydrophone){
                printf("hyrdrophone iş bitti başka iş seçiniz");
                continue;
            }
            else{            
            current->hydrophone_count++;
            current = current->next;
            }
            break;
            case 6:
            if(joystick>Joystick){
                printf("joystick iş bitti başka iş seçiniz");
                continue;
            }
            else{         
            current->joystick_count++;
            current = current->next;
            joystick++;
            }   
            break;
            default:
            printf("Invalid choice.\n");
            continue;
            }
    

    }
    for (int i = 0 ; i<4 ; i ++){
        printf("%s: %s %d, %s %d, %s %d, %s %d, %s %d, %s %d \n", 
        current->isimler, 
        "MainBoard count:", current->main_board_count, 
        "BMS count:", current->bms_count, 
        "SmartPowerBox count:", current->smart_power_box_count,
        "ControlStation count:", current->control_station_count, 
        "Hydrophone count:", current->hydrophone_count, 
        "Joystick count:", current->joystick_count);
        current = current->next;
    }   
    return 0 ;
}
