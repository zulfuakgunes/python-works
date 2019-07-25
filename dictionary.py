class AnException(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        if self.code == 1:
            return repr("Your index must be an integer")
        elif self.code == 2:
            return repr("Index out of range")
        else:
            return repr("An error occured")


class MyList:

    def __init__(self, length):
        self.length = length
        self.mylist = [None]*self.length

    def __setitem__(self, key, value):
        try:
            if not isinstance(key, int):
                raise AnException(1)
            if abs(key) >= self.length:
                raise AnException(2)
        except AnException as e:
            print(e)
        else:
            self.mylist[key] = value

    def __getitem__(self, item):
        try:
            if not isinstance(item, int):
                raise AnException(1)
            if abs(item) >= self.length:
                raise AnException(2)
        except AnException as e:
            print(e)
        else:
            return self.mylist[item]

    def __len__(self):
        return len(self.mylist)


languages = MyList(4)
languages[0] = "Turkish"
languages[1] = "English"
languages[2] = "Russian"
languages[3] = "Chinese"
languages[4] = "Abc"  # Throws an exception
print(languages[3])  # Chinese
print(languages[-2])  # Russian
print(languages[5])  # Throws an exception
print(languages[-6])  # Throws an exception
