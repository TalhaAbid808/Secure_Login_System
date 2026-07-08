import hashlib
while True:
   print("1.===Register===\n")
   print("2.Login")
   print("3.Exit")
   choice =input("Enter choice: ")
   if choice == "1":
      first_name = input("Enter first_name: ")
      second_name = input("Enter second_name: ")
      email = input("Enter email: " )
      password = input("Enter password: ")
      confirm_password = input("Enter confirm_password: ")
      with open("username.txt","a") as file:
         file.write(f"{first_name}|{second_name}|{email}|{password}|{confirm_password}\n")
         print("Register successfull: ")
   elif choice == "2":
      username = input("Enter username: ")
      password = input("Enter password: ")
      hash_value = hashlib.sha256(password.encode())
      print("SHA256 Hash:")
      print(hash_value.hexdigest())
      with open("username.txt","r") as file:
         found = False
         for line in file:
            data = line.strip().split("|")
            if data [0] == username and data[1]==password:
               found = True
               
            if found:
                print("Login successful")
            else:
               print("Invalid credentials")
               break
   elif choice =="3":
     print("Exit")
   else:
      ("Invalid choice")