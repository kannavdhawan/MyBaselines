

try:
    a = 10/0
except Exception as e:
    print("Exception handeled")

finally:
    print("finally")


a = lambda x:x*x
print(a(2))


try:
    a=10/0

except(ArithmeticError, IOError):
    print("Arithmetic Exception")
else:
    print("Successfully Done")

dic = {1:'a', 2:'b'}
dic[1] = 'c'
print(dic[1])
import sys
print(type(sys.argv))
print('The command line arguments are:')
for i in sys.argv:
    print(i)

print(type(str(123)))


def multiple_yield():
    str1 = "First String"
    yield str1

    str2 = "Second string"
    yield str2

    str3 = "Third String"
    yield str3


obj = multiple_yield()
print(next(obj))
print(next(obj))
print(next(obj))
