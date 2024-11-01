#pragma once

#include <Arduino.h>

class Tester;

class TesterState {
public:
  virtual ~TesterState() = default;
  virtual auto execute(String command) -> void = 0;
protected:
  void changeState(Tester*, TesterState*);
};

