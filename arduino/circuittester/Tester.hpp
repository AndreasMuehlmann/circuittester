#pragma once

#include <Arduino.h>

class TesterState;

class Tester {
public:
  Tester();
  auto execute(String& command) -> void;
private:
  friend class TesterState;
  auto handleStateChangeCommand(String& command) -> bool;
  auto changeState(TesterState*) -> void;

  TesterState* _state;
};
