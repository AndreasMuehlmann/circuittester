#include "InputOutputTester.hpp"
#include "Utils.hpp"
#include "variant.h"
#include "wiring_constants.h"

InputOutputTester::InputOutputTester(String creationCommand) {
  //Tester InputOutputTester 3, 4; 5, 6
  List<String> inputAndOutputPins = split(creationCommand, ';');
  if (inputAndOutputPins.getSize() < 2) {
    Serial.println("Error: Expected input and output pins with delimiter \";\" for InputOutputTester creation. Got " + String(inputAndOutputPins.getSize() - 1) + " \";\" .");
    return;
  }
  String inputPins = inputAndOutputPins.at(0);
  String outputPins = inputAndOutputPins.at(1);
  List<String> stringInputPins = split(inputPins, ',');
  List<String> stringOutputPins = split(outputPins, ',');

  m_inputPins = stringInputPins.toInt();
  m_outputPins = stringOutputPins.toInt();

  List<int> reoccurencesCheckList = m_inputPins;
  reoccurencesCheckList.extend(m_outputPins);
  if (reoccurences(reoccurencesCheckList)) {
    Serial.println("Error: Found reoccurences in list of pins. This could also be the case if a pin specifier couldn't be parsed to an int.");
    return;
  }

  for (int i = 0; i < m_inputPins.getSize(); i++) {
    if (m_inputPins.at(i) <= 2) {
      Serial.println("Error: Pins 1 and 2 don't work.");
      return;
    }
    pinMode(m_inputPins.at(i), INPUT);
  }
  for (int i = 0; i < m_outputPins.getSize(); i++) {
    if (m_inputPins.at(i) <= 2) {
      Serial.println("Error: Pins 1 and 2 don't work.");
      return;
    }
    pinMode(m_outputPins.at(i), OUTPUT);
  }
}

auto InputOutputTester::execute(String command) -> void {
  List<String> outputValues = split(command, ',');

  for (int i = 0; i < outputValues.getSize(); i++) {
    if (outputValues.at(i) != "0" && outputValues.at(i) != "1") {
      Serial.println("Error: Expected output values to be either 0 or 1. Got \"" + outputValues.at(i) + "\".");
      return;
    }
  }

  if (outputValues.getSize() != m_outputPins.getSize()) {
    Serial.println("Error: Length of output values doesn't match lenght of output pins.");
    return;
  }

  for (int i = 0; i < outputValues.getSize(); i++) {
    if (outputValues.at(i) == "1") {
      digitalWrite(m_outputPins.at(i), HIGH);
    } else {
      digitalWrite(m_outputPins.at(i), LOW);
    }
  }

  List<int> inputValues;
  for (int i = 0; i < m_inputPins.getSize(); i++) {
    inputValues.add(digitalRead(m_inputPins.at(i)));
  }

  inputValues.println();
}
