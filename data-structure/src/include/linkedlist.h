#include <iostream>

template<typename T>
class LinkedList {
  public:
    virtual ~LinkedList() = default;
    static LinkedList<T>* create();

    virtual void add(T item) = 0; 
    virtual T get(int index) = 0;
    virtual void remove(int index) = 0;

    virtual std::string toString() = 0;
};

extern template class LinkedList<int>;
extern template class LinkedList<std::string>;
