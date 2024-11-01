#include "Tester.hpp"
#include "TesterState.hpp"

auto TesterState::changeState(Tester* tester, TesterState* state) -> void {
  tester->changeState(state);
}
