def main():
    txt = input("select algo type: ")
    print(txt)
    if int(txt)==1:
        print("branch and bound starting...")
        branchBound()

if __name__=='__main__':
    main()
