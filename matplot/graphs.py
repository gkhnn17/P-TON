import matplotlib.pyplot as plt



yil = [2001,2002,2003,2004,2005]
oyuncu1=[6,7,12,5,10]
oyuncu2=[4,5,4,5,5]
oyuncu3=[9,7,13,11,10]


"""#Stack Plot
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="y",label="oyuncu2")
plt.plot([],[],color="y",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])
plt.title("Goller")
plt.xlabel("yil")
plt.ylabel("goller")
plt.legend()

plt.show()
"""
"""#Pie Graphs
goal_types = "penaltı","kaleye","serbest vurus"
goals = [12,35,7]
colors =["y","r","b"]

plt.pie(goals,labels=goal_types,colors=colors,shadow=True,explode=(0.05,0.05,0.05),autopct="%1.1f%%")

plt.show()"""

"""#Bar Grafiği
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,20,60,70,40],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[70,50,30,70,60],label="Audi",width=.5)

plt.legend()
plt.xlabel("Gün")
plt.xlabel("Mesafe(km)")
plt.title("Araç Bilgileri")

plt.show()"""

#Histogram Grafiği
yaslar = [5,22,55,62,45,21,18,22,3,43,65,72,85,97,85,74,345,15,34,54,456,14,35,65,123]
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)

plt.xlabel("yaş grupları") 
plt.ylabel("kişi sayısı")
plt.title("Histogram Grafiği")
plt.show()