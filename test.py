import math
import mmh3  # Hashing library
from bitarray import bitarray

class BloomFilter:
    def __init__(self, size, num_hashes):
        """Initialize the Bloom Filter with a bit array and the number of hash functions."""
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = bitarray(size)
        self.bit_array.setall(0)

    def add(self, item):
        """Add an item to the Bloom Filter."""
        for i in range(self.num_hashes):
            index = mmh3.hash(item, i) % self.size
            self.bit_array[index] = 1

    def contains(self, item):
        """Check if an item is possibly in the Bloom Filter."""
        for i in range(self.num_hashes):
            index = mmh3.hash(item, i) % self.size
            if not self.bit_array[index]:
                return False  # Definitely not in the set
        return True  # Possibly in the set

# Example usage
if __name__ == "__main__":
    n = 20  # Expected number of items
    p = 0.01  # Desired false positive probability

    # Calculate the optimal size and number of hash functions
    size = -int(n * math.log(p) / (math.log(2) ** 2))
    num_hashes = int((size / n) * math.log(2))

    bloom = BloomFilter(size, num_hashes)

    # Add some elements
    bloom.add("apple")
    bloom.add("banana")
    bloom.add("grape")

    # Test for membership
    print(bloom.contains("apple"))   # True (possibly)
    print(bloom.contains("banana"))  # True (possibly)
    print(bloom.contains("orange"))  # False (definitely not)
    print(bloom.contains("shiv"))    # False (definitely not)
    print(bloom.bit_array)

