#pragma once

#include <Arduino.h>

class TesterState;

class Tester {
public:
  Tester();
  auto execute(String command) -> void;
private:
  friend class TesterState;
  auto changeState(TesterState*) -> void;

  TesterState* _state;
};
