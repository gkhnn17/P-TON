#**********************************MATPLOTLİB**************************************
import matplotlib.pyplot as plt
import numpy as np 

"""
x = [1,2,3,4]
y = [1,4,9,16]
plt.plot(x,y,"o--",linewidth="3",color="red")#[marker,line,color]
plt.axis([0,6,0,20])#x,y

plt.title("Chart title")
plt.xlabel("x label")
plt.ylabel("y label")
plt.show()"""

"""x = np.linspace(0,2,100)
plt.plot(x,x,label="linear")
plt.plot(x,x**2,label="quadratic")
plt.plot(x,x**3,label="cubic")

plt.title("simple plot")
plt.xlabel("x label")
plt.ylabel("y label")

plt.legend()#showing info

plt.show()
"""
"""x = np.linspace(0,2,100)
fig,axs = plt.subplots(3)

axs[0].plot(x,x,color="red")
axs[0].set_title("linear")

axs[1].plot(x,x**2,color="green")
axs[1].set_title("x**2")

axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("x**3")

plt.tight_layout()

plt.show()"""

"""x = np.linspace(0,2,100)
fig,axs = plt.subplots(2,2)
fig.suptitle("chartitle")


axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="blue")
axs[1,0].plot(x,x**3,color="green")
axs[1,1].plot(x,x//2,color="yellow")
"""
import pandas as pd

df = pd.read_csv("C:/Users/Casper/PİTON/pandasd/USvideos_modified.csv")

df = df.drop(["comment_count"],axis= 1).groupby("title")
df.head(2).plot(x="title",subplots=True)
plt.legend()
plt.show()