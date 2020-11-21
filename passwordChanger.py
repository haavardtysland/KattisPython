import json

json_file =  open("user.json", "r")
data = json.load(json_file)
json_file.close()

checkU = input("Enter username")
checkP = input("Enter password")

if(data["username"] == checkU and data["password"] == checkP):
    newPassword = input("Enter new password")
    data["password"] = newPassword
    print("Password updated")
else: 
    print("False input")

outfile = open("user.json", "w") 
json.dump(data, outfile)
outfile.close()
