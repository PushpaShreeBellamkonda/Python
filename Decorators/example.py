def user_login(f1):
    def inner(user,is_login):
        if is_login ==False:
            print("kindly login")
            return 
        return f1(user,is_login)
    return inner


@user_login
def home(user,is_login):
    print("welcome to home page")
@user_login
def orders(user,is_login):
    print("welcome to orders page")
def about():
    print("welcome to about page")

home("pushpa",True)
orders("pushpa",False)
about()

