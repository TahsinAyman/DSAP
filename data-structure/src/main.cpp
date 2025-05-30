#include <arraylist.h>
#include <iostream>

int main(void) {
  ArrayList* list = ArrayList::create();
  for (int i = 0; i < 20; i++) {
    list->add(i);
  }
  std::cout << list->toString() << std::endl;
  return 0;
}

