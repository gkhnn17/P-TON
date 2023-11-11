

class Movie():
    def __init__(self,title,director,duration) :
        self.title = title
        self.director =director
        self.duration = duration
        print("movie spawned")
    
    def __str__(self):
        return f"{self.title} by {self.director}" #bellek bilgisi değil string bilgisi verildi

    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("film silindi")

m = Movie("wick","unknown",100)
print(m)#normalde bellek adresi == print(str(m))
print(len(m))


del m 
