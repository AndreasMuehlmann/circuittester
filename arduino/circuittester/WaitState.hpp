#pragma once

#include "TesterState.hpp"

class WaitState : public TesterState {
public:
  WaitState() = default;
  auto execute(String command) -> void;
};
