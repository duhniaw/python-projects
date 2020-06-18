import sqlite3
import re
conn = sqlite3.connect("info-signup-login")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS loginginfo (username TEXT, email TEXT, password TEXT)")
class Signup:

	def __init__(self, username, email, password):
		self.username = username
		self.email = email
		self.password = password
		
	def signup(self):
		c.execute("SELECT * FROM loginginfo WHERE (username =? AND email = ?)", (self.username, self.email))
		if c.fetchone() is None:
			c.execute("INSERT INTO loginginfo(username , email, password ) VALUES (? , ?, ?)", (self.username, self.email, self.password))
			conn.commit()
			print("Registered ! now try to log in !")
		else:
			print("This username or email is already registered ! ")

class Login:
	def __init__(self, email, password):
		self.email = email
		self.password = password
	def login(self):
		check = c.execute("SELECT * FROM loginginfo WHERE (email = ? AND password =? )", (self.email, self.password))
		if check.fetchone() is None:
			print("Couldn't find member with this informations ")
		else:
			print("Logged in !")
			
def forgetpass():
	e = input("Email :")
	lstps = input("Old password :")
	checking = c.execute("SELECT * FROM loginginfo WHERE (email = ? AND password = ?)", (e, lstps))
	if checking.fetchone() is None:
		print("Couldn't find user with this informations ! ")
	else:
		newpass = input("Enter new password :")
		c.execute("UPDATE loginginfo SET password = ? WHERE email = ? AND password = ?", (newpass, e ,lstps))
		conn.commit()
		print("Password set to {}".format(newpass))
			
def main():
	choose = input("Sign up / Logging : ")
	if choose == "Sign up":
		user = input("Username : ")
		email = input("Email : ")
		if re.match("[^@]+@[^@]+\.[^@]+", email) and email.endswith(".com"):
			password = input("Password : ")
			sg = Signup(user, email1, password)
			sg.signup()
		else:
			print("Please enter a valid email")
	elif choose == "Logging":
		mail = input("Email :")
		pass_ = input("Password or Update password ? : ")
		if pass_ == "Update password":
			emai = "Email : "
			password = "Password : "
			forget = forgetpass
			forget()
		else:
			lg = Login(mail, pass_)
			lg.login()

		
if __name__ == "__main__":
	while True:
		main()