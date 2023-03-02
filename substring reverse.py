#USING RECURSION

def rev(s):
    k = s.split()
    l= [revs(w) for w in k]
    return " ".join(l)

def revs(w):
    if len(w) == 1:
        return w
    else:
        return revs(w[1:]) + w[0]

string = input()
print(rev(string))
