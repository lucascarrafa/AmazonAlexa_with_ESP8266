#include <ESP8266WiFi.h>
#include <ESP8266HTTPClient.h>
#include <ArduinoJson.h> 
 
const char* ssid = "nomedarede";
const char* password = "senha";
 
void setup () {
 
WiFi.begin(ssid, password);
pinMode(1, OUTPUT);
 
while (WiFi.status() != WL_CONNECTED) {
  delay(1000);
}
 
}
 
void loop() {
 
if (WiFi.status() == WL_CONNECTED) { //Verifica o status da conexão do WiFi
 
  HTTPClient http;
  
  http.begin("https://www.minhaapi.com/estado");
  int httpCode = http.GET(); //envia a requisição                                                                  
  
  if (httpCode > 0) { //Verifica o codigo de retorno
    StaticJsonDocument<53> doc; //Verificar no tamanho no site https://arduinojson.org/v6/assistant/
    deserializeJson(doc, http.getString());

      if(doc["status"]=="desligado"){
        digitalWrite(1, HIGH);
      }else{
        digitalWrite(1, LOW);
      }
  }
}
 
http.end();   //Fecha conexão
 
}
 
delay(1000);
 
}
