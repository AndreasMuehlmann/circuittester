#include <Arduino.h>

#include "Tester.hpp"
#include "InputTester.hpp"
#include "NothingTester.hpp"
#include "InputOutputTester.hpp"
#include "variant.h"

const String STATE_CHANGE_PREFIX = "Tester ";

Tester::Tester() {
  _state = new NothingTester();
}

auto Tester::execute(String& command) -> void {
  if (handleStateChangeCommand(command)) {
    return;
  }
  _state->execute(command);
}

auto Tester::handleStateChangeCommand(String& command) -> bool {
  if (!command.startsWith(STATE_CHANGE_PREFIX)) {
    return false;
  }
  command = command.substring(STATE_CHANGE_PREFIX.length());

  String newState;
  int index = command.indexOf(" ");
  if (index == -1) {
    newState = command;
    command = "";
  } else {
    newState = command.substring(0, index);
    command = index == command.length() ? "" : command.substring(index + 1);
  }

  if (newState == "InputOutputTester") {
    changeState(new InputOutputTester(command));
  } else if (newState == "InputTester") {
    changeState(new InputTester(comman));
  } else if (newState == "NothingTester") {
    changeState(new NothingTester());
  } else {
    Serial.println("Error: No matching Tester found for \"" + newState + "\".");
  }
  return true;
}

auto Tester::changeState(TesterState* state) -> void {
  delete _state;
  _state = state;
}

