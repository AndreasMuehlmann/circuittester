#include "TruthTableTester.hpp"
#include "Utils.hpp"
#include "variant.h"

TruthTableTester::TruthTableTester(String creationCommand) {
  List<String> inputAndOutputPins = split(creationCommand, ';');
  if (inputAndOutputPins.getSize() != 2) {
    Serial.println("Error: Expected input and output pins with delimiter \";\" for TruthTableTester creation. Got " + String(inputAndOutputPins.getSize() - 1) + " \";\" .");
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
  }
}

auto TruthTableTester::execute(String command) -> void {
  Serial.println(command);
}
