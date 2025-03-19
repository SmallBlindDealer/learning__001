# import hashlib
# import math

# class HyperLogLog:
#     def __init__(self, b):
#         self.b = b  # Number of bits for the registers
#         self.m = 1 << b  # Number of registers (2^b)
#         self.registers = [0] * self.m

#     def _hash(self, value):
#         # Hash the value and return the binary representation
#         return int(hashlib.md5(value.encode('utf8')).hexdigest(), 16)

#     def add(self, value):
#         x = self._hash(value)
#         j = x >> (x.bit_length() - self.b)  # Get the register index
#         w = x & ((1 << (x.bit_length() - self.b)) - 1)  # Get the hash value for leading zero count
#         self.registers[j] = max(self.registers[j], self._rho(w))

#     def _rho(self, w):
#         # Count leading zeros
#         return (w | (1 << w.bit_length())).bit_length() + 1

#     def estimate(self):
#         # Calculate the HyperLogLog estimate
#         alphaMM = (0.7213 / (1 + 1.079 / self.m)) * self.m * self.m
#         Z = 1.0 / sum(0.5 ** r for r in self.registers)
#         return alphaMM * Z

# # Example usage
# hll = HyperLogLog(b=3)  # Using 12 bits for registers
# elements = ["apple", "banana", "orange", "apple", "banana", "grape"]

# for el in elements:
#     hll.add(el)

# print(f"Estimated number of distinct elements: {hll.estimate()}")


# import hashlib

# import math

# def hyperloglog_estimate(data, num_registers=16):

#     registers = [0] * num_registers



#     for item in data:

#         hash_value = int(hashlib.sha256(item.encode()).hexdigest(), 16)

#         register_index = (hash_value >> (128 - int(math.log2(num_registers)))) % num_registers

#         leading_zeros = 0

#         while (hash_value & 1) == 0:

#             leading_zeros += 1

#             hash_value >>= 1

#         registers[register_index] = max(registers[register_index], leading_zeros)



#     # Calculation based on harmonic mean (simplified for demonstration)

#     estimate = num_registers * (math.log(num_registers) / (sum(1 / (x + 1) for x in registers)))

#     return estimate



# # Example usage

# data = ["apple", "banana", "orange", "apple", "grape", "shiv", "shankar", "keshari"]

# estimated_cardinality = hyperloglog_estimate(data, 16)

# print("Estimated unique elements:", estimated_cardinality) 

import math

# Number of registers (must be a power of 2)
m = 1024
# Initialize registers
registers = [0] * m

import hashlib

def hash_function(value):
    hash_value = hashlib.sha256(value.encode('utf8')).hexdigest()
    return int(hash_value, 16)

def leftmost_1_bit_position(hash_value, p):
    bin_hash = bin(hash_value)[2:]  # Convert hash to binary
    return bin_hash.find('1', p) + 1  # Find position of first '1' after p bits

def process_element(element, registers, m):
    hash_value = hash_function(element)
    p = int(math.log2(m))
    register_index = hash_value & (m - 1)  # Get first p bits for register index
    remaining_hash = hash_value >> p  # Shift out the first p bits
    position = leftmost_1_bit_position(remaining_hash, p)
    registers[register_index] = max(registers[register_index], position)

def harmonic_mean(registers):
    sum_of_inverses = sum([2**-reg for reg in registers])
    return len(registers) / sum_of_inverses

def bias_correction(raw_estimate, m):
    if raw_estimate <= 2.5 * m:
        V = registers.count(0)
        if V > 0:
            return m * math.log(m / V)  # Linear counting
    elif raw_estimate > (2**32) / 30:
        return -(2**32) * math.log(1 - raw_estimate / (2**32))  # Large range correction
    return raw_estimate  # No correction needed

def estimate_cardinality(registers):
    alpha_m = 0.7213 / (1 + 1.079 / len(registers))  # Alpha value for bias correction
    raw_estimate = alpha_m * len(registers)**2 * harmonic_mean(registers)
    return bias_correction(raw_estimate, len(registers))

def hyperloglog_estimate(dataset, m):
    registers = [0] * m
    for element in dataset:
        process_element(element, registers, m)
    return estimate_cardinality(registers)

# Example usage
dataset = ['A', 'B', 'C', 'D', 'A', 'B', 'E', 'F']
estimate = hyperloglog_estimate(dataset, m)
print(f"Estimated number of unique elements: {estimate}")
