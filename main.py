from dbhelper import DBhelper

def main():
    while True:
        print("************Welcome***************")
        print()
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to Exit program")
        print()

        try:
            choice = int(input())
            db = DBhelper()
            if(choice == 1):
                #insert user
                uid = int(input("Enter a id :"))
                username = input("Enter a user name :")
                phone  = input("Enter a phone number :")
                db.insert_user(uid,username,phone)
            elif(choice == 2):
                #display user
                db.fetch_user()
                pass
            elif(choice == 3):
                #delete user
                uid = int(input("Enter a user name"))
                db.delete_user(uid)
                pass
            elif(choice == 4):
                #update user
                uid = int(input("Enter a user id to update :"))
                username = input("Enter a user name to update :")
                phone  = input("Enter a phone number to update :")
                db.update_user(uid,username,phone)
                pass
            elif(choice == 5):
                #exit program
                break
            else:
                print("invalid input ! try again")
        except Exception as e:
            print(e)
            print("invalid details ! try again")

if __name__ == "__main__":
    main()



