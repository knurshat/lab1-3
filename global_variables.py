x = "awesome"

def myfunc():
    print("Python is" + " " + x)

def func():
    x =  "fantastic"
    print("Python is" + " " + x)
# если изменять переменную внутри функции она не изменится во всем коде
myfunc()
func()
print("Python is " + x)

def mfunc():
    global x
    x = "fantastic"

mfunc()

print("Python is " + x)