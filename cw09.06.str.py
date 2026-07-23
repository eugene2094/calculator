"python"
'a'
text = """ some text """

print(type(text))
print(text)
print(id(text))
text = " python "
print(id(text))

print(text[0])
print(text[1])
print(text[-1])

# print(text[11]) error
# text[0] = 'f' error

print('len:', len(text))

# +  *
str1 = "hello"
str2 = ' admin'
print(str1 + str2)
print(str1 * 3)

str3 = str1 + str2
print(str3[0:5])
print(str3[6:])
print(str3[:len(str3) // 2])

new_str = "PYthon language"

print(new_str.lower())
print(new_str.upper())
print(new_str.capitalize())
print(new_str.title())
print(new_str.swapcase())
print(new_str)

print(new_str.count('PYthon'))
print(new_str.find('n', 3, 10))

print(new_str.startswith('t'))
print(new_str.endswith('p'))

num = '   432   '
print(num.isdigit())
print(num.isalnum())
print(num.isnumeric())

print(num.strip())
print(num)



