sum = 0
while (True):
	userInput = input(" Enter The Cost Of Item Or Press Y To Exit \n")
	if (userInput!='y'):
		sum = sum + int(userInput)
		print(f"You Have Buyed So Far Of {sum}")
	else:
		print(f"Total Cost Of What You Have Buyed Is {sum}.")
		break