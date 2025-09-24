import pandas as pd
bnames = ["Noah", "Liam", "Jacob", "William", "Mason", "Ethan", "Michael", "Alexander", "James", "Elijah"]
gnames = ["Emma", "Olivia", "Sophia", "Isabella", "Ava", "mia", "Abigail", "Emily", "Charolette", "Madison"]
bfreq = [183330, 173981, 163266, 159945, 157875, 1490982, 145171, 142142, 139652, 137093]
gfreq = [195028, 184628, 181132, 170559, 155884, 129088, 118712, 119626, 102470, 98419]

df = pd.DataFrame({'boysnames':bnames, 'bfreq':bfreq, 'girlnames':gnames, 'gfreq':gfreq})

print(df)

print(df.describe())