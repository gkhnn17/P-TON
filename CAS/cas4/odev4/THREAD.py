import threading
import time
"""
def func(x):
    
    print(f'ran{x}')
    time.sleep(3)
    print("done")
    time.sleep(1)
    print("now done")

x = threading.Thread(target=func,args=(5,))#args tuple
x.start()
print(threading.active_count())
time.sleep(1.2)
print("not now")
"""
"""
ran
2
done
not now
now done
"""
 
ls = []
def count(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)#thread değişimi başlar

def count2(n):
    for i in range(1,n+1):
        ls.append(i)
        time.sleep(0.5)


x = threading.Thread(target=count,args=(5,))
y = threading.Thread(target=count2,args=(5,))

x.start()
y.start()

x.join()#boundary 
y.join()
print(ls)#sınır olmasa sonuc [1,1] kalırdı
"""[1, 1, 2, 2, 3, 3, 4, 4, 5, 5]"""





"""# Python program to illustrate the concept
# of threading
# importing the threading module
import threading
 
 
def print_cube(num):
    # function to print cube of given num
    print("Cube: {}" .format(num * num * num))
 
 
def print_square(num):
    # function to print square of given num
    print("Square: {}" .format(num * num))
 
 
if __name__ =="__main__":
    # creating thread
    t1 = threading.Thread(target=print_square, args=(10,))
    t2 = threading.Thread(target=print_cube, args=(10,))
 
    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
 
    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()
 
    # both threads completely executed
    print("Done!")"""