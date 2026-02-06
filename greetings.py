
def sayhi(name):
    print(f"Hello {name}\n")
    return

if __name__ == "__main__":
    name = input("What is your name? ")
    if len(name) >= 1:
        sayhi(name)
        exit
    print("Goodbye!")

