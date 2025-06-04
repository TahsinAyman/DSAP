#include <iostream>
#include <linkedlist.h>
#include <string>
#include <sstream>

template<typename T>
class Node {
  public:
    T val;
    Node<T>* next;

    Node(T item) {
      this->val = item;
    }
};

template<typename T>
class LinkedListImpl : public LinkedList<T> {
  private:
    Node<T>* root = nullptr;

    Node<T>* getNode(int index) {
      if (this->root == nullptr) {
        throw 404;
      } 
      int i = -1;
      Node<T>* curr = this->root;
      while (curr) {
        i += 1;
        if (i == index) {
          return curr;
        }
        curr = curr->next;
      }
      throw 404;
    }

  public:
    void add(T item) override {
      if (this->root == nullptr) {
        this->root = new Node(item);
        return;
      }
      Node<T>* curr = this->root;
      while (curr->next) {
        curr = curr->next;
      } 
      curr->next = new Node<T>(item);
    }
    T get(int index) override {
      return this->getNode(index)->val;
    }
    void remove(int index) override {
      if (index == 0) {
        this->root = this->root->next;
        return;
      }
      Node<T>* prevNode = this->getNode(index - 1);
      prevNode->next = prevNode->next->next;
    }

    std::string toString() override {
      std::ostringstream out;
      out << "[ ";
      Node<T>* curr = this->root;
      while (curr) {
        out << curr->val << " ";
        curr = curr->next;
      }
      out << "]";
      return out.str();
    }  
};

template<typename T>
LinkedList<T>* LinkedList<T>::create() {
    return new LinkedListImpl<T>();
}

template class LinkedList<int>;
template class LinkedList<std::string>;

template class LinkedListImpl<int>;
template class LinkedListImpl<std::string>;
