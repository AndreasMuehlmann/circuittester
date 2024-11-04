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

    if (element == "") { continue; }
    list.add(element);

    if (index + 1 >= string.length()) { break; }
    string = string.substring(index + 1);
  }
  return list;
}
