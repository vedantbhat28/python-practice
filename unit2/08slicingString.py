email=str(input("Enter your name:"))
position=email.find("@")
username=email[:position]
print(f"Username:{username}")