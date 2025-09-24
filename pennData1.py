import pandas as pd
import random

fnames = ["Keaton", "Mac", "Van", "Lucian", "Alex", "Noah", "Michael", "Josh", "Alexis", "Jill", "Emma", "Lily", "Marge", "Lisa"]
lnames = ["Smith", "Jones", "brown", "Johnson", "Watkins", "Anderson", "Wilson", "Moore", "Davis"]
years = ["Freshman", "Sophmore", "Junior", "senior", "Super senior"]
pathways = ["Early college", "Engineering", "Business", "Computer Science", "Culinary", "Bio Med"] 
names = []
for i in range(20):
    names.append(f"{random.choice(fnames)} {random.choice(lnames)}")

print(names)

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.5),2)for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(years) for _ in names],
    "Pathway": [random.choice(pathways) for _ in names]
}

pennData = pd.DataFrame(data)
pennData.to_csv()