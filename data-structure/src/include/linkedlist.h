class LinkedList {
  virtual ~LinkedList() = default;
  static LinkedList* create();

  virtual void add(int item);
};
