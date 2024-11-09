#include <Arduino.h>

#include "Tester.hpp"
#include "TesterState.hpp"

const size_t MAX_PINS = 32;
const uint32_t TIMEOUT = 500;


Tester tester;

void setup() {
  Serial.begin(9600);
}

String resetString = "Tester NothingTester";

void loop() {
  int start = millis();
  while(!Serial.available() > 0) {
      if (millis() - start > TIMEOUT) {
        String resetStringCopy = resetString;
        tester.execute(resetStringCopy);
      }
      delay(50);
  }
  String command = Serial.readStringUntil('\n');
  tester.execute(command);
}
