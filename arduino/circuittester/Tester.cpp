#include <Arduino.h>

#include "Tester.hpp"
#include "WaitState.hpp"
#include "variant.h"

Tester::Tester() {
  _state = new WaitState();
}

auto Tester::execute(String& command) -> void {
  if (handleStateChangeCommand(command)) {
    return;
  }
  _state->execute(command);
}

auto Tester::handleStateChangeCommand(String& command) -> bool {
  if (!command.startsWith("ChangeState ")) {
    return false;
  }
  command = command.substring(12);

  String newState;

  int index = command.indexOf(" ");
  if (index == -1) {
    newState = command;
    command = "";
  } else {
    newState = command.substring(0, index);
  }

  Serial.println(newState);
  if (newState == "TruthTable") {
    Serial.println("change state to truth table");
  } else if (newState == "Wait") {
    Serial.println("change state to wait");
    changeState(new WaitState());
  }
}

auto Tester::changeState(TesterState* state) -> void {
  delete _state;
  _state = state;
}
