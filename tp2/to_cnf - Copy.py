import sys

# def card_cons(lits, b):
#     pVars = []
#     for i in range(b):
#         pVars.append([])
#         l = []
#         for j in range(n-b+1):
#             pVars[i].push(False)
#             l.append(False)
#         addClause(l)
    
#     for i in range(len(pVars)):
#         for j in range(len(pVars[i])):
#             clause = []
#             clause.append(not pVars[i][j])
#             clause.append(lits[i+j])
#             addClause(clause)
    
#     for i in range(len(pVars-1)):
#         l = []
#         for j in range(len(pVars)-1):
#             l.append(pVars[i][j])
#             l.append(not pVars[i+1][j])
#             addClause(l)
#             l.pop()

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

    # frequency

    for i in range(n, n + len(lits)):
        cnf += f"{i} "
    cnf += f" 0\n"
    
    # support

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

    # closure

    for it in items:
        for i, t in enumerate(lits):
            if it not in t:
                cnf += f"{n+i} "
        cnf += f"{it} 0\n"
    
    # card_cons(items, nb_support)

    n2 = len(cnf.split("\n")) -1
    header = f"p cnf {n+len(items)-1} {n2}\n"
    content = header+cnf

    with open("out2.cnf", "w+") as out:
        out.write(content)

if __name__ == "__main__":
    main()