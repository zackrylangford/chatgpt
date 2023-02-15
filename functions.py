
#Save user input to database

def append_user_input(file_name, prompt):
	file_in = open(file_name, 'a')
	user_input = prompt
	file_in.write(user_input+"\n")
            
	file_in.close()


# Save Marcus input to database