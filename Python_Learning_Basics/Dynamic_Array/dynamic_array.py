class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        # initalize thae array fixed size
        self.dynamic_array = self.capacity * [0]

    def get(self, i: int) -> int:
        # Get from the array
        return self.dynamic_array[i]

    def set(self, i: int, n: int) -> None:
        # Set to particular index
        self.dynamic_array[i] = n

    # Add the elements to array
    def pushback(self, n: int) -> None:
        # let's say we have capacity of size 2
        # inserted element at index 0 and index 1
        # now size and capacity is 2. It means we need to resize the array
        if self.size == self.capacity:
            self.resize()
        self.dynamic_array[self.size] = n
        self.size = self.size + 1

    def popback(self) -> int:
        # Soft delete
        if self.size > 0:
            self.size = self.size - 1
        return self.dynamic_array[self.size]

    def resize(self) -> None:
        self.capacity = 2 * self.capacity
        self.new_array = self.capacity * [0]
        # Now initalize all the element from old array to new array.
        for index, element in enumerate(self.dynamic_array):
            self.new_array[index] = element
        self.dynamic_array = self.new_array

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity


if __name__ =="__main__":
    dynamicarray = DynamicArray(2)
    dynamicarray.pushback(22)
    dynamicarray.pushback(33)
    dynamicarray.pushback(44)
    print(dynamicarray)
    print(dynamicarray.get(1))


