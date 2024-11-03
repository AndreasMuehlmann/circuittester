#include "Utils.hpp"


auto splitByComma(String& string) -> List<String> {
  List<String> list;
  int index = 0;
  while (index != -1) {
    index = string.indexOf(",");

    if (index == -1) { 
      string.trim();
      list.add(string);
      break;
    }

    String element = string.substring(0, index);
    element.trim();
    list.add(element);
  }
}