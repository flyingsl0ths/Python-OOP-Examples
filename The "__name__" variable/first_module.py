# Whenever the Python interpreter runs a file directly
# a series of variables are set, __name__ being
# one of them is set to "__main__"

# Whenever another file imports this module
# __name__ is set to the name of this file the reason
# for this is, that this file is no longer being ran
# directly by python but the file containing the import statement

# Tldr __name__ == "__main__" is used to determine
# whether the file is being used as an entry point

# This allows the use of writing code that runs only
# when the file is the entry point however code defined
# in the global scope is still ran due to the interpreter
# parsing through the file before the if-statement (__name__ == "__main__")
# is reached

print("This will always run")


def get_name(num):
    if(num == 1):
        return "First"
    elif(num == 2):
        return "Second"
    return "Last"


def print_name(num=0, name=__name__):
    print(f"{get_name(num)} Module's Name {name}")


def main():
    print_name(1)


if __name__ == "__main__":
    main()
else:
    print("Ran from import")
