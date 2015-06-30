#include <chibi.h>
#include "DHT.h"

#define nub_val 6
#define SRC_ADDR 5
#define DEST_ADDR 3
#define DHTPIN 2        
#define DHTTYPE DHT22   

byte len, data[100];
float value[nub_val];

void setup()
{  
  chibiInit();
  chibiSetShortAddr(SRC_ADDR);

  Serial.begin(9600);
}

void loop()
{
  if (chibiDataRcvd() == true)
  {
    len = chibiGetData(data);
        
    if (len == 0)
      return;
   
    memcpy(value,data, 6*sizeof(float));
    
    Serial.print(value[0]);  
    Serial.print(",");
    Serial.print(value[2]);
    Serial.print(",");
    Serial.print(value[3]);
    Serial.print(",");
    Serial.print(value[4]);
    Serial.print(",");
    Serial.println(value[5]);
   
  delay(10000); //wait a second and get values again.
  }
}
