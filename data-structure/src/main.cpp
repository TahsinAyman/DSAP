#include <arraylist.h>
#include <iostream>

int main(void) {
  ArrayList* list = ArrayList::create();
  while (1) {
    int x;
    std::cout << "Value: ";
    std::cin >> x;
    if (x == -1) {
      break;
    }
    list->add(x);
  }
  std::cout << list->toString() << std::endl;
  return 0;
}

