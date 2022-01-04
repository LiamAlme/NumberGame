from hashlib import blake2b

def reset():
    global e
    e = blake2b(key=b'DoNotCrackThisKey82394', digest_size=32)

def registry():
    reset()
    new_password_written = False
    new_username_written = False
    index = 0
    flag = 0
    user_list = open("user_list.txt", "r")
    while new_username_written == False:
        new_username = input("What would you like your username to be?\n")
        for line in user_list:
            index += 1
            if (str(new_username)+str("\n")) == line:
                if index % 2 == 1:
                    flag = 1
        if flag == 0:
            user_list.close()
            user_list = open("user_list.txt", "a")
            user_list.write(new_username +str("\n"))
            new_username_written = True
        else:
            print("Username is taken, please enter a new username")
            flag = 0
            index = 0
            user_list.close()
            user_list = open("user_list.txt", "r")
    while new_password_written == False:
        new_password = input("What would you like your password to be?\n")
        new_password_check = input("Confirm your password\n")
        if new_password == new_password_check:
            e.update(new_password.encode())
            user_list.write(str(e.hexdigest()) +str("\n"))
            print("Account Created")
            new_password_written = True
    user_list.close()
    return new_username


def login():
    reset()
    index = 0
    index2 = 0
    flag = 0
    user_list = open("user_list.txt", "r")
    login_username = input("Enter your username\n")
    for line in user_list:
        index += 1
        if (str(login_username)+str("\n")) == str(line):
            if index % 2 == 1:
                flag = 1
                break
    if flag == 1:
        user_list.close()
        user_list = open("user_list.txt", "r")
        login_password = str(input("Enter your password\n",))
        e.update(login_password.encode())
        login_password = e.hexdigest()
        for line in user_list:
            index2 +=1
            if (str(login_password)+str("\n")) == str(line):
                if index + 1 == index2:
                    print("Logged In")
                    user_list.close()
                    return login_username
            if index2 > index+1:
                user_list.close()
                return False
    if flag == 0:
        input("Enter your password\n")
    user_list.close()
    return False