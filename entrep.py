file = open("entrep.txt", "r+")
lines = file.read()
new_lines = lines.replace("**", "")
file.seek(0) #moves file pointer to the beginning 
file.write(new_lines)
file.truncate() #removes everything after the new lines
print(new_lines)
file.close()
