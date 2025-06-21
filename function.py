def my_fun():
    print("python")


my_fun()                             #for calling a function change indentation and skip two lines after declaration
#parameter
def my_fun(a, b):
    print("sum = ", a+b)


my_fun(2, 5)

#default value(hum bina parameter pass kre bhi run kra skte hai ya only ek parameter pass bhi krke run hoga)
def my_fun(a=0, b=0):
    print("sum = ", a+b)


my_fun(4)

#if no. of arguments are unknown(access element through index number)
def my_fun(*city):
    print(city[1])


my_fun("a", "b", "c")

#.......order
def my_function(city3, city2, city1):
    print("the first city is" + city1)


my_function(city1="mumbai", city2="delhi", city3="agra")

#.......no. of argument are unknown using key value (use double astrict)
def my_fun(**city):
    print(city['bn'])


my_fun(fn="a", ln="b", bn="c")