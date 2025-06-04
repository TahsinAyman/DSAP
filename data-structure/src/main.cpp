#include <iostream>
#include <linkedlist.h>
#include <ostream>

int main(void) {
  LinkedList<int>* list = LinkedList<int>::create();
  list->add(2);
  list->add(3);
  list->add(4);
  list->remove(2);
  std::cout << list->toString() << std::endl;
  std::cout << list->get(0) << std::endl;
  return 0;
}

