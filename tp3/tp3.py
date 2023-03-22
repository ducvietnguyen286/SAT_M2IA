import sys
import os


def writeFile(nbVar,c,nbC,cout):
    nbVars=nbVar+nbC
    card=""
    pVars =[]


    card+="c relax clause\n"
    for i in range(nbC):
        for x in c[i]:
            card+=str(x)+" "
        card+=str(nbVar+i+1)
        card+=" 0\n"



    card+="c (10):\n"
    for i in range(cout):
        l=[]
        for j in range(nbC-cout+1):
            l.append(nbVars+1)
            nbVars+=1
        pVars.append(l)
        #ajout des contraintes
        for a in l:
            card +=str(a)+" "
        card+="0\n"
    

    card += "c (9):\n"
    for i in range(len(pVars)):
        for j in range(len(pVars[i])):
            l = []
            l.append(-pVars[i][j])
            l.append(-nbVar+1+i+j)
            #ajout des contraintes
            for a in l:
                card += str(a) +" "
            card+="0\n"

    card += "c (11):\n"
    for i in range(len(pVars)-1):
        l=[]
        for j in range(len(pVars[i])-1):
            l.append(pVars[i][j])
            l.append(-pVars[i+1][j])
            #ajout des contraintes
            for a in l:
                card+=str(a)+" "
            card+="0\n"
            l.pop()

    return card

def main():
    lines=[]
    with open(sys.argv[1],"r") as input:
        for line in input:
            lines.append(line)
    #print(lines)
    nbVar=-1
    c=[]
    for line in lines:
        split=line.split()
        #print(split)
        c.append([])
        for val in split[:-1]:
            c[-1].append(int(val))
            if(abs(int(val)) >nbVar):
                nbVar=abs(int(val))
    print(c)
    print("nbVar ="+str(nbVar))

    cout=0
    card=writeFile(nbVar,c,len(c),cout)
    with open('out.cnf','w') as out:
        out.write(card)

    upperBoundNotFound=True
    while upperBoundNotFound:
        if os.system("./minisat out.cnf sol")==2560:
            cout=0
            with open('sol','r') as solution:
                cpt=0
                for line in solution:
                    if cpt==1:
                        print(line)
                        split=line.split()
                        nb=nbVar+len(c)
                        for a in split[nbVar:nb]:
                            if int(a)<0:
                                cout+=1
                    cpt+=1
                card=writeFile(nbVar,c,len(c),cout+1)
                with open('out.cnf','w') as out:
                    out.write(card)
        else:
            print("Upper bound found :")
            print(str(len(c)-cout))
            upperBoundNotFound=False

if __name__ == "__main__":
    main()