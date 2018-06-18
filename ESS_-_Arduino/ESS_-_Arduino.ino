#include <SoftwareSerial.h> 
#include <TinyGPS.h>
#define GPS_DELAY_MS 1500
float lat = 1.000,lon = 1.000000; // create variable for latitude and longitude object  
SoftwareSerial gpsSerial(4,3);//rx,tx 
TinyGPS gps; // create gps object 

void setup(){ 
Serial.begin(9600); // connect serial 
Serial.println("The GPS Received Signal:"); 
gpsSerial.begin(9600); // connect gps sensor 

}

void getPosition(){ // get latitude and longitude 
   static unsigned long start = millis();
   if(millis() - start > GPS_DELAY_MS){
      while(gpsSerial.available()){ // check for gps data 
          if(gps.encode(gpsSerial.read())){// encode gps data   
            gps.f_get_position(&lat,&lon); // get latitude and longitude 
            // display position 
            Serial.println("GPS Signal");
            Serial.print("Position: "); 
            Serial.print("Latitude:"); 
            Serial.print(lat,6); 
            Serial.print(";"); 
            Serial.print("Longitude:"); 
            Serial.println(lon,6);  
            Serial.println(millis() - start);
            start = millis();
          }
           
      }
    }      
}


void loop(){
  
  getPosition();
  
   
  
} 

 
