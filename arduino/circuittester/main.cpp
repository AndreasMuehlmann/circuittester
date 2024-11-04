#include <Arduino.h>

#include "Tester.hpp"
#include "TesterState.hpp"
#include "List.hpp"
#include "Utils.hpp"

const size_t MAX_PINS = 32;
const uint32_t TIMEOUT = 100;


Tester tester;

void setup() {
  Serial.begin(9600);
}

void loop() {
  int start = millis();
  while(!Serial.available() > 0) {
      if (millis() - start > TIMEOUT) {
        // timeout
      }
  }
  String string = "1, 2, 8,";
  List<String> list = split(string, ',');
  for (int i = 0; i < list.getSize(); i++) {
    Serial.println("Element: " + list.at(i));
  }
  List<int> intList = list.toInt();
  for (int i = 0; i < list.getSize(); i++) {
    Serial.println("Number: " + list.at(i));
  }
  String command = Serial.readStringUntil('\n');
  Serial.println(command);
  tester.execute(command);
}
