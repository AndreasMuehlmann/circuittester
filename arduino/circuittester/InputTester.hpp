#pragma once

#include "TesterState.hpp"
#include "List.hpp"

class InputTester : public TesterState {
public:
  InputTester(String creationCommand);
  auto execute(String command) -> void;
private:
  List<int> m_inputPins;
};
