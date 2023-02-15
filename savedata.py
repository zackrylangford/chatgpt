def append_user_input(file_name):
	file_in = open(file_name, 'a')
	while True:
		user_input = input("Enter your text (Press Q to quit): ")
		if user_input == "Q":
			break
		else:
			file_in.write(user_input+"\n")
	file_in.close()

#calling the function
append_user_input("sample.txt")





def append_user_input(file_name):
	file_in = open(file_name, 'a')
	while True:
		user_input = input("Enter your text (Press Q to quit): ")
		if user_input == "Q":
			break
		else:
			file_in.write(user_input+"\n")
	file_in.close()

#calling the function
append_user_input("sample.txt")