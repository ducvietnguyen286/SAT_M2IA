#pour compiler : python3 tp2_DucVietNGUYEN.py example.txt k
import sys

def addClause(cl):
    file = open("dimacs.txt", "a")
    for val in cl:
        file.write(str(val)+" ")
    file.write("0 \n")
    file.close()

def card_cons(transactions, items, k):
    nb_variables = len(transactions) + len(items)
    nb_items = len(items)
    p_Vars = []
    for i in range(k):
        l = []
        for j in range(nb_items - k + 1):
            l.append(nb_variables + 1)
            nb_variables += 1
        p_Vars.append(l)
        addClause(l)
    
    for i in range(len(p_Vars)):
        for j in range(len(p_Vars[i])):
            clause = []
            clause.append(-p_Vars[i][j])
            clause.append(list(items)[i+j])
            addClause(clause)
    
    for i in range(len(p_Vars)-1):
        l = []
        for j in range(len(p_Vars[i])-1):
            l.append(p_Vars[i][j])
            l.append(-p_Vars[i+1][j])
            addClause(l)
            l.pop()


if __name__ == "__main__":

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

    t = ""
    cnf = ""

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
    
    card_cons(lits,items, nb_support)

    n2 = len(cnf.split("\n")) -1
    dimacs = open('dimacs.txt', 'r').read()
    header = f"p cnf {n+len(items)-1} {n2}\n"
    content = header+dimacs+cnf

    with open("output.cnf", "w+") as out:
        out.write(content)