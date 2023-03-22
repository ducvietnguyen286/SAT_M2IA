import sys

def main():

    with open(sys.argv[1],"r") as f:
        content = f.read()

    nb_support = int(sys.argv[2])
    items = set()
    lits = []

    for l in content.split("\n"):
        l = l.strip()
        if l == "":
            continue
        transaction = list(map(int,l.split(" ")))
        lits.append(transaction)
        for i in transaction: items.add(i)
    print(lits)
    print(items)

    cnf = ""

    t = ""
    n = len(items)+1


    for i in range(n, n + len(lits)):
        cnf += f"{i} "
    cnf += f" 0\n"
    

    for i, t in enumerate(lits):
        cnf += f"{n + i} "
        for it in items:
            if it not in t:
                cnf += f"{it} "
        cnf += f"0\n"

    for i, t in enumerate(lits):
        for it in items:
            if it not in t:
                cnf += f"-{n+i} -{it} 0\n"


    for it in items:
        for i, t in enumerate(lits):
            if it not in t:
                cnf += f"{n+i} "
        cnf += f"{it} 0\n"
    

    n2 = len(cnf.split("\n")) -1
    header = f"p cnf {n+len(items)-1} {n2}\n"
    content = header+cnf

    with open("output.cnf", "w+") as out:
        out.write(content)

if __name__ == "__main__":
    main()