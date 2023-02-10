class string_upper:
    def getString(self):
        self.name = input("")

    def printString(self):
        print(self.name.upper())

s1 = string_upper()
s1.getString()
s1.printString()