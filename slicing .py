
#string slicing
s = "sujithaswami"
print(s[:])
print(s[6:10])
print(s[3:])
print(s[-11:-8])
print(s[-11:-9])
#reverse of a string by using slicing
print(s[::-1])
#reverse of a string without using slicing
s = "sujitha swami"
s = "".join(reversed(s))
print(s)
#reverse a list items
s = ["sujitha", "anusha", "madhuha"]
print(s[::-1])
#reverse of a list without using slicing
a = ["sujitha", "anusha", "madhuha"]
a.reverse()
print(a)
