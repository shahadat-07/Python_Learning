 # function is a first class object

def double_decker():
    print("starting the double decker")
    def inner_func():
        print("inside the inner")
        return 300
    return  inner_func

# print(double_decker())
# print(double_decker()())


def do_something(word):
    print("work started")
    print(word)
    print('work ended')

# do_something(2)
# do_something('busy')

def coding():
    print("coding in python")
    return 0

do_something(coding())