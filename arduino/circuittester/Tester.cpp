#include <Arduino.h>

#include "Tester.hpp"
#include "WaitState.hpp"

Tester::Tester() {
  _state = new WaitState();
}

auto Tester::execute(String command) -> void {
  _state->execute(command);
}

