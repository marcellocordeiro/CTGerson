#include <SoftwareSerial.h>
#include <TinyGPS.h>

#define GPS_DELAY_MS 1500
#define BUTTON_PIN 8
#define RGB_GREEN_PIN 10
#define RGB_RED_PIN 11
#define RGB_BLUE_PIN 9

float lat = 1.000, lon = 1.000000;  // create variable for latitude and longitude object
bool activateAlarm = false;

SoftwareSerial gpsSerial(4, 3);  // rx,tx
TinyGPS gps;                     // create gps object

void setup() {
    Serial.begin(9600);  // connect serial
    Serial.println("The GPS Received Signal:");
    gpsSerial.begin(9600);  // connect gps sensor
    pinMode(BUTTON_PIN, INPUT);
    pinMode(RGB_GREEN_PIN, OUTPUT);
    pinMode(RGB_RED_PIN, OUTPUT);
    pinMode(RGB_BLUE_PIN, OUTPUT);
    unsigned long start_teste = millis();
}

void getPosition() {  // get latitude and longitude
    static unsigned long start = millis();
    if (millis() - start > GPS_DELAY_MS) {
        while (gpsSerial.available()) {          // check for gps data
            if (gps.encode(gpsSerial.read())) {  // encode gps data
                gps.f_get_position(&lat, &lon);  // get latitude and longitude
                // display position
                Serial.println("GPS Signal");
                Serial.print("Position: ");
                Serial.print("Latitude:");
                Serial.print(lat, 6);
                Serial.print(";");
                Serial.print("Longitude:");
                Serial.println(lon, 6);
                Serial.println(millis() - start);
                start = millis();
            }
        }
    }
}

void loop() {
    if (digitalRead(BUTTON_PIN)) {
        activateAlarm = true;
    }

    if (activateAlarm) {
        getPosition();
        analogWrite(RGB_GREEN_PIN, 0);
        analogWrite(RGB_RED_PIN, 50);
    } else {
        analogWrite(RGB_GREEN_PIN, 50);
        analogWrite(RGB_RED_PIN, 0);
    }
}
