print("hello python", "welcome", 8, sep="..", end="---",)
print("hello", end="---")
print("Bonjour")
print('8')
print(10>5)
print(10*5)
a=2
b=3
print(a-b)
print("the subtraction of", a, "and", b, "is", a-b,)
print(f"the subtraction of {a} and {b} is {a-b}")
print("the subtraction of", a, "and", b, "is", a-b, sep="..", end="--")
print(f"the subtraction of {a} and {b} is {a-b}", sep="..")
print(f"the subtraction of {a} and {b} is", a-b,":)", sep=" .. ")
# meaning of f is formatting and string formatting

print(f"the value of pi is {22/7:.4f}")
#a = int(input("enter a number:"))
#print(a+1)
#p = int(input("enter first number:"))
#q = int(input("enter second number:"))
#print(p*q)
#x = float(input("enter first number:"))
#y = float(input("enter second number:"))
#print(f"the value is {x*y:.3f}")

help("keywords")

b=str(25)
print(b)

print('''1.one 
2.two
3.three''')

s=10
r=10
print(id(s))
print(id(r))     #save memory address of s and r.if value is diff then memory address also differ

u="python"
print(u.upper())    #all letters in uppercase

i="POKEMON"
print(i.lower())    #all letters in lowercase

m="\tthis is python"         #give tab(space) in starting
print(m.expandtabs(30))      #size of tab
print(m.find("i"))           #get the index number of first "i" letter

z="-"""
seq=("py", "th", "on")
print(z.join(seq))

h="my name is riya"
print(h.replace("name","Piya" ))

str1 = "Names:\na\nb\nc\nd"
print("before:" +str1)
print("after splitting the string", str1.splitlines())

k="Riyadh"
n="123456"
o="my name is Riyadha"
encoding = o.maketrans(k, n)
print(o.translate(encoding))