# Bitwise Operators Example

a = 10   # 1010
b = 4    # 0100

print("Value of a:", a)
print("Value of b:", b)

# AND
print("\nAND (a(1010) & b(0100)):", a & b)

# OR
print("OR (a=(1010) | b(0100)):", a | b)

# XOR()
print("xOR (a=(1010) xor b(0100)):", a ^ b)

# NOT
print("NOT (~a1010):", ~a)
print("NOT (~b0100):", ~b)

# Left Shift
print("\nLeft Shift (a(1010) << 1):", a << 1)
print("Left Shift (b(0100) << 1):", b << 1)

# Right Shift
print("\nRight Shift (a(1010) >> 1):", a >> 1)
print("Right Shift (b(0100) >> 1):", b >> 1)

"""
output:

Value of a: 10
Value of b: 4

AND (a(1010) & b(0100)): 0
OR (a=(1010) | b(0100)): 14
xOR (a=(1010) xor b(0100)): 14
NOT (~a1010): -11
NOT (~b0100): -5
"""
