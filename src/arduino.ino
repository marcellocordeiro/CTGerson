#include <KNoTThing.h>
#include <SoftwareSerial.h>
#include <TinyGPS.h>

#define GPS_DELAY_MS 1500
#define BUTTON_PIN 3
#define RGB_GREEN_PIN 10
#define RGB_RED_PIN 11
#define RGB_BLUE_PIN 9

#define LON_ID 2
#define LON_NAME "Longitude"

#define LAT_ID 3
#define LAT_NAME "Latitude"

#define ALARM_STATUS_ID 4
#define ALARM_STATUS_NAME "Alarm Status"

float lat = 2.123123, lon = 3.312312;  // create variable for latitude and longitude object
bool statusAlarm = false;

SoftwareSerial gpsSerial(5, 4);  // rx,tx
TinyGPS gps;                     // create gps object
KNoTThing thing;

static float lon_read(int32_t *val_int, uint32_t *val_dec, int32_t *multiplier) {
    *val_int = (int)lon;
    *val_dec = (lon - *val_int) * 1000000;
    *multiplier = 1;
    return 0;
}
static float lon_write(int32_t *val_int, uint32_t *val_dec, int32_t *multiplier) {
    return 0;
}

static float lat_read(int32_t *val_int, uint32_t *val_dec, int32_t *multiplier) {
    *val_int = (int)lat;
    *val_dec = (lat - *val_int) * 1000000;
    *multiplier = 1;

    return 0;
}

static float lat_write(int32_t *val_int, uint32_t *val_dec, int32_t *multiplier) {
    return 0;
}

static int alarm_status_read(uint8_t *val) {
    *val = statusAlarm;
    return 0;
}

static int alarm_status_write(uint8_t *val) {
    statusAlarm = *val;

    return 0;
}

void setup() {
    Serial.begin(9600);  // connect serial

    // Serial.println("The GPS Received Signal:");
    gpsSerial.begin(9600);  // connect gps sensor

    pinMode(BUTTON_PIN, INPUT);
    pinMode(RGB_GREEN_PIN, OUTPUT);
    pinMode(RGB_RED_PIN, OUTPUT);
    pinMode(RGB_BLUE_PIN, OUTPUT);

    unsigned long start_teste = millis();

    // KNoT code
    thing.init("ALARME DAORA");
    thing.registerBoolData(ALARM_STATUS_NAME, ALARM_STATUS_ID, KNOT_TYPE_ID_SWITCH, KNOT_UNIT_NOT_APPLICABLE, alarm_status_read, alarm_status_write);

    // thing.registerFloatData(LON_NAME, LON_ID, KNOT_TYPE_ID_LONGITUDE,
    //   KNOT_UNIT_LONGITUDE_DEGREE, lon_read,lon_write);

    thing.registerFloatData(LAT_NAME, LAT_ID, KNOT_TYPE_ID_LATITUDE, KNOT_UNIT_LATITUDE_DEGREE, lat_read, lat_write);

    /* Send data every 10 seconds*/
    // thing.registerDefaultConfig(LON_ID, KNOT_EVT_FLAG_TIME, 1, 0, 0, 0, 0);
    thing.registerDefaultConfig(LAT_ID, KNOT_EVT_FLAG_TIME, 1, 0, 0, 0, 0);
    thing.registerDefaultConfig(ALARM_STATUS_ID, KNOT_EVT_FLAG_TIME, 1, 0, 0, 0, 0);
}

void getPosition() {  // get latitude and longitude
    static unsigned long start = millis();

    if (millis() - start > GPS_DELAY_MS) {
        while (gpsSerial.available()) {          // check for gps data
            if (gps.encode(gpsSerial.read())) {  // encode gps data
                gps.f_get_position(&lat, &lon);  // get latitude and longitude
                // display position
                // Serial.println("GPS Signal");
                // Serial.print("Position: ");
                // Serial.print("Latitude:");
                // Serial.print(lat,6);
                // Serial.print(";");
                // Serial.print("Longitude:");
                // Serial.println(lon,6);
                // Serial.println(millis() - start);
                start = millis();
            }
        }
    }
}

void loop() {
    thing.run();
    getPosition();
    statusAlarm = digitalRead(BUTTON_PIN);
}
