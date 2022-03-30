def ifelse():
    x = int(input("Please enter an integer: "))
    if x < 0:
        print("negative")
    elif x == 0:
        print("zero")
    else:
        print("positive")

def forloop():
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))


if __name__ == '__main__':
    forloop()
    # ifelse()
