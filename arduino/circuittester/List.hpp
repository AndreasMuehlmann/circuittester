#pragma once

#include "variant.h"
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
  auto extend(List<T> list) -> void;
  auto toInt() -> List<int>;
  auto println() -> void;
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

template <class T>
auto List<T>::extend(List<T> list) -> void {
  for (int i = 0; i < list.getSize(); i++) {
    add(list.at(i));
  }
}

template <class T>
auto List<T>::println() -> void {
  for (int i = 0; i < m_size - 1; i++) {
    Serial.print(String(at(i)) + ",");
  }
  Serial.println(String(at(m_size - 1)));
}

template <>
inline auto List<String>::toInt() -> List<int> {
  List<int> list;
  for (int i = 0; i < m_size; i++) {
    list.add(at(i).toInt());
  }
  return list;
}
