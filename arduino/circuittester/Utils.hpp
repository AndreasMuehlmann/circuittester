#pragma once

#include <Arduino.h>

#include "List.hpp"

auto split(String& string, char delimiter) -> List<String>;
auto reoccurences(List<int> list) -> bool;
