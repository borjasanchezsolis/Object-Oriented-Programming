class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError('Wrong capacity')
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self.size * '🍪'

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError('Exceed capacity') 
        if self.size + n > self.capacity:
            raise ValueError('Exceed capacity')
        self._size += n    # when you wanna update the value of size or capacity you have to use the underscore

    def withdraw(self, n):
        if n > self.size:
            raise ValueError('There are less cookies than you want to remove') 
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar = Jar()
jar.deposit(2)
jar.withdraw(0)
print(jar)

