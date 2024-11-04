#pragma once

#include <Arduino.h>

const size_t CAPACITY = 100;

template <class T>
class List {
public:
  List();
  auto add(T element) -> void;
  auto at(size_t index) -> T;
  auto set(size_t index, T element) -> void;
  auto getSize() -> size_t;
private:
  T m_array[CAPACITY];
  size_t m_size;
};

template <class T>
List<T>::List() : m_size(0) {}

template <class T>
auto List<T>::add(T element) -> void {
  if (m_size >= CAPACITY) { 
    Serial.println("ERROR: trying to add more elements than possible to list.");
    return;
  }
  
  m_array[m_size] = element;
  m_size++;
}

template <class T>
auto List<T>::at(size_t index) -> T {
  if (index >= m_size) { 
    Serial.println("ERROR: trying to access not existent index.");
    return T();
  }
  
  return m_array[index];
}

template <class T>
auto List<T>::set(size_t index, T element) -> void {
  if (index >= m_size) {
    Serial.println("ERROR: trying to set not existent index.");
    return;
  }
  
  m_array[index] = element;
}

template <class T>
auto List<T>::getSize() -> size_t {
  return m_size;
}
