#include <Arduino.h>

#include "WaitState.hpp"

auto WaitState::execute(String command) -> void {
  Serial.println(command);
}
