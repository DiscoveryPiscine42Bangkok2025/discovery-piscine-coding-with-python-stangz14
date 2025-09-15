from sys import argv

def main():
    if not len(argv) > 1:
        print("none")
        return
    for i in argv[1:]:
        if i[-1:-4:-1] == "msi":
            continue
        print(i, "ism", sep="")

main()