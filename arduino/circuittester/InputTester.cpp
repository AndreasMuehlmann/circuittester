#include "InputTester.hpp"
#include "Utils.hpp"
#include "variant.h"

InputTester::InputTester(String creationCommand) {
  //Tester InputTester 3, 4
  List<String> stringInputPins = split(creationCommand, ',');
  m_inputPins = stringInputPins.toInt();

  List<int> reoccurencesCheckList = m_inputPins;
  if (reoccurences(reoccurencesCheckList)) {
    Serial.println("Error: Found reoccurences in list of pins. This could also be the case if a pin specifier couldn't be parsed to an int.");
    return;
  }

  for (int i = 0; i < m_inputPins.getSize(); i++) {
    if (m_inputPins.at(i) <= 2) {
      Serial.println("Error: Pins 1 and 2 don't work.");
      return;
    }
    pinMode(m_inputPins.at(i), INPUT_PULLUP);
  }
}

auto InputTester::execute(String command) -> void {
  List<int> inputValues;
  for (int i = 0; i < m_inputPins.getSize(); i++) {
    inputValues.add(digitalRead(m_inputPins.at(i)));
  }

  inputValues.println();
}
