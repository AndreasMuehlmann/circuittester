#include <Arduino.h>

#include "NothingTester.hpp"

auto NothingTester::execute(String command) -> void {
  Serial.println(command);
}
