"""
şehirler =["kocaeli","istanbul"]
plakalar = [41,34]
print(plakalar[şehirler.index("istanbul")])
"""
plakalar ={"kocaeli" : 41 , "istanbul" : 34}#key : value şeklinde eklemeyi sağlar

print(plakalar["kocaeli"])


plakalar["ankara"] = 6
print(plakalar)

users = {
    "gökhan" :{
    "age" : 3,
    "iq" : "1010",
    "roles":["admin","user"],
    },
    "eksta" :"asdf"
}
print(users["gökhan"]["age"])
print(users["gökhan"]["roles"][0])