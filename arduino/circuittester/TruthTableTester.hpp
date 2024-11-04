#pragma once

#include "TesterState.hpp"
#include "List.hpp"

class TruthTableTester : public TesterState {
public:
  TruthTableTester(String creationCommand);
  auto execute(String command) -> void;
private:
  List<int> m_inputPins;
  List<int> m_outputPins;
};
