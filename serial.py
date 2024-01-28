"""Python serial number generator."""

class SerialGenerator:
    def __init__(self, start=100):
        self.start = start
        self.current = start

    def generate(self):
        self.current += 1
        return self.current - 1

    def reset(self):
        self.current = self.start

    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>>  serial.reset()

    >>> serial.generate()
    100
    """

if __name__ == "__main__":
    serial = SerialGenerator(start=100)
    print(serial.generate())  # Should print 100
    print(serial.generate())  # Should print 101
    print(serial.generate())  # Should print 102
    serial.reset()            # Reset the serial number to start value
    print(serial.generate())