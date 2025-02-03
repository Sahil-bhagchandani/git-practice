# app.py
def login(username, password):
    if username == "admin" and password == "admin":
        return "Login successful"
    else:
        return "Invalid credentials"

def logout():
    return "Logout successful"

print("Hello, Git!")
