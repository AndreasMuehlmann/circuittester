#pragma once

const size_t CAPACITY = 100;

template <class T>
class List {
public:
  auto add(T element) -> void;
  auto at(size_t index) -> T;
  auto set(size_t index, T element) -> void;
  auto getSize() -> size_t;
private:
  T array[CAPACITY];
  size_t size;
};
