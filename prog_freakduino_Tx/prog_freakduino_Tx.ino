#include <chibi.h>
#include "DHT.h"
#include "Barometer.h".
#include <Wire.h> 

#define nub_val 6
#define SRC_ADDR 3
#define DEST_ADDR 5
#define DHTPIN 2     
#define DHTTYPE DHT22   

Barometer myBarometer;
byte data[100];
float value[nub_val];

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  myBarometer.init();
  dht.begin();
  
  chibiInit();
  chibiSetShortAddr(SRC_ADDR);
}

void loop()
{
      delay(2000);
     
      value[0] = dht.readHumidity();
      value[1] = dht.readTemperature();
      value[2] = myBarometer.bmp085GetTemperature(myBarometer.bmp085ReadUT()); 
      value[3] = myBarometer.bmp085GetPressure(myBarometer.bmp085ReadUP());
      value[4] = myBarometer.calcAltitude(value[3]); 
      value[5] = value[3] / 101325; 
      
 
 
  memcpy(data,value,(6*sizeof(float)));
  
  chibiTx(DEST_ADDR, data, (6*sizeof(float)));
}
