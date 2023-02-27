class string_upper:
    def getString(self):
        self.name = input("")

    def printString(self):
        print(self.name.upper())

    def delete(self):
        for i in range(len(self.name)):
            if i % 2 == 0:
                print(self.name[i])


s1 = string_upper()
s1.getString()
s1.printString()
s1.delete()