from replit import db
import stdiomask

keys = db.keys()


def score(us, s):
    score = s
    usern = us
    fh = open("scoes.txt", "w")
    fh.write(usern + " ")
    fh.write(str(score))


def get_score():
    fh = open("scoes.txt", "r")
    for line in fh:
        l = line.split()
        print(l)
    fh.close()


def register():
    new_u = input("Enter a new username: ")
    new_pas = stdiomask.getpass(prompt="Enter a new password: (8 characters, uppercase, lowercase) ", mask="*")
    confirm = stdiomask.getpass(prompt="Confirm password: (8 characters, uppercase, lowercase) ", mask="*")
    if (confirm == new_pas):
        db[new_u] = new_pas
    else:
        print("passwords do not match")
    return 0


def main():
    print("not a valid command")
    return 0


def login(use):
    u = use
    password = stdiomask.getpass(prompt="Enter your password: (8 characters, uppercase, lowercase) ", mask="*")
    if (len(password) < 8 or password.islower() == True or password.isupper() == True):
        print("invalid entry")
        return 0
    for i in keys:
        if u == i:
            if db[u] == password:
                print("logged in")
                return u
    else:
        print("incorrect username or password")


scores = 5

u = input("Enter username: ")

login(u)

score(u, scores)

get_score()



