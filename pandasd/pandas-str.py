import pandas as pd


data = pd.read_csv("C:/Users/Casper/PİTON/pandasd/all_seasons.csv")

data.dropna(inplace= True)
data["player_name"] = data["player_name"].str.upper()

#data["index"] = data["player_name"].str.find("A")
#data = data[data.player_name.str.contains("ED")]
#data = data.player_name.str.replace(' ','-')
data[["FirstName","LastName"]] = data["player_name"].loc[data["player_name"].str.split().str.len()==2].str.split(expand=True)

result = data

print(result.head(10))

