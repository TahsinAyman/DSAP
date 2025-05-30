#pragma once
#include <iostream>

class ArrayList {
  public:
    virtual void add(int value) = 0;
    virtual ~ArrayList() = default;
    virtual std::string toString() = 0;
    static ArrayList* create();
};
