my_dict = {"player1 score" : 123123132 , "player2 score": 2323236533 , "player3 score" : 54654654546}
my_dict ["player2 score"] = 8556565
my_dict ["player4 score"] = 465465565
my_dict.update({"player5 score": 8787898465 ,
                "player6 score" : 78798768464})

print (my_dict)
w = my_dict.pop("player1 score")
print (my_dict)
print (w)


my_set = { 1 , 2 , 3 ,5 ,5 ,5 , 78 , "pumpum" , False}
print(my_set)
my_set.update(["sun" , "flower"])
my_set.remove(5)
print(my_set)


