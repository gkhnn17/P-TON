import pandas as pd

data = pd.read_csv("C:/Users/Casper/PİTON/pandasd/USvideos_modified.csv")
df = pd.DataFrame(data)


#df.drop(columns="ratings_disabled", inplace=True)
#df = df.head(200)
#df.to_csv("C:/Users/Casper/PİTON/pandasd/USvideos_modified.csv", index=False)

result = df[df["views"].max()==df["views"]]["title"].iloc[0]

result =df.sort_values("views",ascending=False)[["title","views"]].head(10)

df['likes'] = pd.to_numeric(df['likes'], errors='coerce')  # Convert "likes" column to numeric
result = df.groupby("category_id")["likes"].mean().sort_values()

result = df["category_id"].value_counts()

df["title_len"]=df["title"].apply(len)

df["tag_count"]=df["tags"].apply(lambda x:x.split('|'))

def likedislke(dataset):
    likelist = list(data["likes"])
    dislikelist = list(data["dislikes"])

    liste =list(zip(likelist,dislikelist))
    oranliste = []
    
    print(liste)

likedislke(df)