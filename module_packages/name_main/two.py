# two.py
import one

print("This is two.py file.")

one.one_file()

if __name__ == '__main__':
    print("It's run directly from two.py")
else:
    print("It import file from another directory")
    