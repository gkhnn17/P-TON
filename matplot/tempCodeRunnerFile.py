fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(4,4))

axes[0].plot(x,z)
axes[0].set_title("Square")

axes[1].plot(x,y)
axes[1].set_title("Cube")
#obstructing titles are overlapping
plt.tight_layout()
fig.savefig("figure1.png")
plt.show()