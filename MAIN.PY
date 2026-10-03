class IOSstring():
    def __init__(self):
        self.str=""
    def get_string(self):
        self.str=input("Enter a string: ")
    def print_string(self):
        print("result is: ",self.str.upper())
str1=IOSstring()
str1.get_string()
str1.print_string()