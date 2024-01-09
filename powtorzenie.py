s = '0123456'
s = s[:4]+'a'+s[5:] # 0123a56
print('01)', s)

s = '0123456'
s = s[0:4]+'a'+s[17:] # 0123a56
print('02)', s)

t = 'abcdefg'
print('03)', t)
print('04)', t[::-1]) # gfedcba

u = [0]*10 # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print('05)', u)

print('06)', ord('a')) # ord('a') = 97
print('07)', chr(97))  # chr(97)  = a

animals = ['cat', 'dog', 'rabbit', 'dog', 'horse']
print('08)', animals.count('dog'))
print('09)', animals.index('dog'))

animals += ['turtle']
print('10)', animals)

napis = 'alamakota'
print('11)', napis.count('a'))
print('12)', napis.index('l'))

napis += 'X'
print('13)', napis)

