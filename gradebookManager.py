dict = {"Kevin":["90%", "80%", "85%"], "Jayden":["50%", "60%", "65%"], "Mike":["70%", "75%", "80%"]}
print(dict)
Choice = input("What would you like to do?(New (g)rade, New (s)tudent, Su(m)mary)").strip().lower()
if input == "g":
    grade = input("Who's grade are you changing?" )
    if grade == "Kevin":
        print(dict["Kevin"])
        Kgrade1 = input("What is Kevin's new grade?" )
        Kgrade2 = input("What is Kevin's new grade?" )
        Kgrade3 = input("What is Kevin's new grade?" )
        dict["Kevin"] = Kgrade1, Kgrade2, Kgrade3
        print(dict["Kevin"])