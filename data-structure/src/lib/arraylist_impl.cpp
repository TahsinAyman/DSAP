#include <arraylist.h>

class ArrayListImpl : public ArrayList {
  private:
    int loadFactor;
    int* arr;
    int count = 0;
    int size;
    const double threshold = 0.75;

    void increaseSize() {
      int reach = this->count - 1;
      int newSize = this->size + this->loadFactor;
      int* newArr = new int[this->size];
      std::copy(this->arr, this->arr + this->size, newArr);
      this->arr = new int[newSize];
      std::copy(newArr, newArr + this->size, this->arr);
      this->size = newSize;
    }
  public:
    ArrayListImpl() {
      this->loadFactor = 10;
      this->size = this->loadFactor;
      this->arr = new int[this->loadFactor];
    }
    void add(int item) override {
      if (this->size * this->threshold < this->count) {
        this->increaseSize();
      }
      this->arr[count] = item;
      this->count += 1;
    }
    std::string toString() override {
      std::string output = "[";
      for (int i = 0; i < this->count; i++) {
        output += std::to_string(this->arr[i]) + " ";
      }
      output += "]";
      return output;
    }
};

ArrayList* ArrayList::create() {
  return new ArrayListImpl();
}
