#pragma once

#include "TesterState.hpp"

class NothingTester : public TesterState {
public:
  NothingTester() = default;
  auto execute(String command) -> void;
};
