#include <Arduino.h>

#include "List.hpp"

template <class T>
auto List<T>::add(T element) -> void {
  if (size >= CAPACITY) { 
    Serial.println("ERROR: trying to add more elements than possible to list.");
    return;
  }
  
  array[size] = element;
  size++;
}

template <class T>
auto List<T>::at(size_t index) -> T {
  if (index >= size) { 
    Serial.println("ERROR: trying to access not existent index.");
    return;
  }
  
  return array[index];
}

template <class T>
auto List<T>::set(size_t index, T element) -> void {
  if (index >= size) {
    Serial.println("ERROR: trying to set not existent index.");
    return;
  }
  
  array[index] = element;
}

template <class T>
auto List<T>::getSize() -> size_t {
  return size;
}
