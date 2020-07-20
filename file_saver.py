import sqlite3
import os
import hashlib
import base64
import time


class Encryption:
    def decode(self, text):
        pass

    def encode(self, text):
        pass


class DataBase:
    conn = sqlite3.connect("fileenc.db")
    crsr = conn.cursor()
    crsr.execute(
        """
	CREATE TABLE IF NOT EXISTS files (name TEXT, ext TEXT, file TEXT, size INT)
	"""
    )


class File(DataBase):
    def new(self, path: str):
        name = path.split("/")[-1]
        check = self.crsr.execute("SELECT * FROM files WHERE name = ?", (name,))
        if check.fetchall():
            return "This file already exists"
        with open(path, "rb") as f:
            ext = f.name.split(".")[-1]
            size = os.path.getsize(f.name)
            self.crsr.execute(
                "INSERT INTO files (name, ext, file, size) VALUES(?,?,?,?)",
                (name, ext, f.read(), size),
            )
            self.conn.commit()

    def show(self):
        ou = self.crsr.execute("SELECT * FROM files")
        output = ou.fetchall()
        summary = ""
        for i in output:
            summary += f"""
NAME:{i[0]}
EXT:{i[1]}
SIZE:{i[3]}

"""
        return summary

    def clone(self, name: str):
        check = self.crsr.execute("SELECT * FROM files WHERE name = ?", (name,))
        if check.fetchall():
            self.crsr.execute("SELECT file FROM files WHERE name = ?", (name,))
            nm = self.crsr.fetchone()
            with open(name, "wb") as f:
                f.write(nm[0])
            return "Cloned"
        return "No saved file with that name"

    def delete(self, name: str):
        check = self.crsr.execute("SELECT * FROM files WHERE name = ?", (name,))
        if check.fetchall():
            self.crsr.execute("DELETE FROM files WHERE name = ?", (name,))
            self.conn.commit()
            return "Deleted"
        return "No file with that name"


class Main:
    filec = File()
    stat = True

    @property
    def opt(self):
        option = input(
            """
[+] OPTIONS [+]
[1] add new file
[2] clone file to current dir
[3] show file's info
[4] delete file
[5] quit\n"""
        )
        return option

    def conv(self, option):
        _conv = {
            "1": self.new_f,
            "2": self.clone_f,
            "3": self.show_f,
            "4": self.delete_f,
            "5": self.stop_f
        }
        try:
        	return _conv[option]
        except:
        	pass

    def new_f(self):
    	path = input("File path: ")
    	self.filec.new(path)
    	print("Added")

    def show_f(self):
        print(self.filec.show())

    def delete_f(self):
        name = input("File name: ")
        print(self.filec.delete(name))

    def clone_f(self):
        name = input("File name: ")
        print(self.filec.clone(name))
        
    def stop_f(self):
    	print("quiting...")
    	self.stat = False

    @property
    def start(self):
        m = self.opt
        try:
            self.conv(m).__call__()
        except:
            pass


if __name__ == "__main__":
    main = Main()
    while main.stat:
        main.start
