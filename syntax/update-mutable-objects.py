#!/usr/bin/env python

his_age = 19
her_age = his_age

his_age += 1

print(his_age) #-> 20
print(her_age) #-> 19


curry = ['chiken', 'onion']
stew = curry

curry.append('spice')

print(curry) #-> ['chiken', 'onion', 'spice']
print(stew)  #-> ['chiken', 'onion', 'spice']
