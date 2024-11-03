#pragma once

#include <Arduino.h>

#include "List.hpp"

auto splitByComma(String& string) -> List<String>;
