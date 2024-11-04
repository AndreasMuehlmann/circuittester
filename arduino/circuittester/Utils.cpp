#include "Utils.hpp"


auto split(String& string, char delimiter) -> List<String> {
  List<String> list;
  int index = 0;
  while (index != -1) {
    index = string.indexOf(delimiter);

    if (index == -1) { 
      string.trim();
      list.add(string);
      break;
    }

    String element = string.substring(0, index);
    element.trim();

    if (element == "") { continue; }
    list.add(element);

    if (index + 1 >= string.length()) { break; }
    string = string.substring(index + 1);
  }
  return list;
}

auto reoccurences(List<int> list) -> bool {
  for (int i = 0; i < list.getSize(); i++) {
    for (int j = 0; j < list.getSize(); j++) {
      if (i != j && list.at(i) == list.at(j)) {
        return true;
      }
    }
  }
  return false;
}
