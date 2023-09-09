#!/usr/bin/env python

print(0b10) #-> 2
print(0o10) #-> 8
print(0x10) #-> 16

print(int('10', 2))  #-> 2
print(int('10', 8))  #-> 8
print(int('10', 16)) #-> 16

print(bin(2))  #-> 0b10
print(oct(8))  #-> 0o10
print(hex(16)) #-> 0x10

print(0b1 == 0B1) #-> True
print(0o7 == 0O7) #-> True
print(0xf == 0XF) #-> True
