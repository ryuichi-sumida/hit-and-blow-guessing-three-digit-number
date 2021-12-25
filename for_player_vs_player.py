

def hit_blow(x,y,z,a,b,c):
    hit=0
    blow=0
    if x == a:
        hit = hit + 1
    if x == b:
        blow = blow + 1
    if x == c:
        blow = blow + 1
    if y == a:
        blow = blow + 1
    if y == b:
        hit = hit + 1
    if y == c:
        blow = blow + 1
    if z == a:
        blow = blow + 1
    if z == b:
        blow = blow + 1
    if z == c:
        hit = hit + 1 
    return (hit, blow)

def f(a):
    i = int(a//100)
    j = int((a-(i*100))//10)
    k = int(a-(i*100)-(j*10))
    if i != j and j != k and k != i:
        return int(100*i + 10*j + k)

def g(a):
    i = int(a//100)
    j = int((a-(i*100))//10)
    k = int((a-(i*100)-(j*10)))
    return (i,j,k)

l = []
for i in range(1000):
    if i == f(i):
        l.append(i)
    else :
        continue

def possible_number(x,y,z,s,t):
    m = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t :
            m.append(i)
        else:
            continue
    return len(m)

def possible_set(x,y,z,s,t):
    m = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t :
            m.append(i)
        else:
            continue
    return m


def possible_number2(x,y,z,s,t,p,q,r,d,e):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e :
            n.append(i)
        else:
            continue
    return len(n)
#Given two pairs of hits and blows, this will give the set of possible numbers that will not contradict the input
def possible_set2(x,y,z,s,t,p,q,r,d,e):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e :
            n.append(i)
        else:
            continue
    return n

def possible_hb2(x,y,z,s,t,p,q,r):
    l1 = []
    l2 = [(3,0), (2,0), (1,2), (1,1),(1,0), (0,3), (0,2), (0,1), (0,0)]
    for (i,j) in l2:
        if possible_number2(x,y,z,s,t,p,q,r,i,j) == 0:
            continue
        else:
            l1.append((i,j))
    return l1
    
#nopl2 = number of possibilities eliminated
def nopl2(x,y,z,s,t,p,q,r):
    m = len(possible_set(x,y,z,s,t))
    nopl = []
    for (i,j) in possible_hb2(x,y,z,s,t,p,q,r):
        nopl.append(m - possible_number2(x,y,z,s,t,p,q,r,i,j))
    return min(nopl)



def fton_2(x,y,z,s,t):
    m = possible_set(x,y,z,s,t)
    if len(possible_set(x,y,z,s,t)) == 1:
        return possible_set(x,y,z,s,t)
    else:
        l3=[1,-10]
        for i in m:
            p = g(i)[0]
            q = g(i)[1]
            r = g(i)[2]
            if nopl2(x,y,z,s,t,p,q,r) > l3[1]:
                l3.clear()
                l3.append(i)
                l3.append(nopl2(x,y,z,s,t,p,q,r))
    return l3

def possible_number3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1:
            n.append(i)
        else:
            continue
    return len(n)
#Given two pairs of hits and blows, this will give the set of possible numbers that will not contradict the input
def possible_set3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 :
            n.append(i)
        else:
            continue
    return n

def possible_hb3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1):
    l1 = []
    l2 = [(3,0), (2,0), (1,2), (1,1),(1,0), (0,3), (0,2), (0,1), (0,0)]
    for (i,j) in l2:
        if possible_number3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,i,j) == 0:
            continue
        else:
            l1.append((i,j))
    return l1
    
#nopl2 = number of possibilities eliminated
def nopl3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1):
    m = len(possible_set2(x,y,z,s,t,p,q,r,d,e))
    nopl = []
    for (i,j) in possible_hb3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1):
        nopl.append(m - possible_number3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,i,j))
    return min(nopl)



def fton_3(x,y,z,s,t,p,q,r,d,e):
    m = possible_set2(x,y,z,s,t,p,q,r,d,e)
    if len(possible_set2(x,y,z,s,t,p,q,r,d,e)) == 1:
        return possible_set2(x,y,z,s,t,p,q,r,d,e)
    else:
        l3=[1,-10]
        for i in m:
            p1 = g(i)[0]
            q1 = g(i)[1]
            r1 = g(i)[2]
            if nopl3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1) > l3[1]:
                l3.clear()
                l3.append(i)
                l3.append(nopl3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1))
    return l3

def possible_number4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 and \
                    hit_blow(p2,q2,r2,a,b,c)[0] == d2 and hit_blow(p2,q2,r2,a,b,c)[1] == e2:
            n.append(i)
        else:
            continue
    return len(n)
#Given two pairs of hits and blows, this will give the set of possible numbers that will not contradict the input
def possible_set4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 and \
                    hit_blow(p2,q2,r2,a,b,c)[0] == d2 and hit_blow(p2,q2,r2,a,b,c)[1] == e2 :
            n.append(i)
        else:
            continue
    return n

def possible_hb4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2):
    l1 = []
    l2 = [(3,0), (2,0), (1,2), (1,1),(1,0), (0,3), (0,2), (0,1), (0,0)]
    for (i,j) in l2:
        if possible_number4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,i,j) == 0:
            continue
        else:
            l1.append((i,j))
    return l1
    
#nopl2 = number of possibilities eliminated
def nopl4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2):
    m = len(possible_set3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1))
    nopl = []
    for (i,j) in possible_hb4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2):
        nopl.append(m - possible_number4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,i,j))
    return min(nopl)


def fton_4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1):
    m = possible_set3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1)
    if len(possible_set3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1)) == 1:
        return possible_set3(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1)
    else:
        l3=[1,-10]
        for i in m:
            p2 = g(i)[0]
            q2 = g(i)[1]
            r2 = g(i)[2]
            if nopl4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2) > l3[1]:
                l3.clear()
                l3.append(i)
                l3.append(nopl4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2))
        return l3

def possible_number5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 and \
                    hit_blow(p2,q2,r2,a,b,c)[0] == d2 and hit_blow(p2,q2,r2,a,b,c)[1] == e2 and \
                        hit_blow(p3,q3,r3,a,b,c)[0] == d3 and hit_blow(p3,q3,r3,a,b,c)[1] == e3:
            n.append(i)
        else:
            continue
    return len(n)
#Given two pairs of hits and blows, this will give the set of possible numbers that will not contradict the input
def possible_set5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 and \
                    hit_blow(p2,q2,r2,a,b,c)[0] == d2 and hit_blow(p2,q2,r2,a,b,c)[1] == e2 and \
                        hit_blow(p3,q3,r3,a,b,c)[0] == d3 and hit_blow(p3,q3,r3,a,b,c)[1] == e3 :
            n.append(i)
        else:
            continue
    return n

def possible_hb5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3):
    l1 = []
    l2 = [(3,0), (2,0), (1,2), (1,1),(1,0), (0,3), (0,2), (0,1), (0,0)]
    for (i,j) in l2:
        if possible_number5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,i,j) == 0:
            continue
        else:
            l1.append((i,j))
    return l1
    
#nopl2 = number of possibilities eliminated
def nopl5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3):
    m = len(possible_set4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2))
    nopl = []
    for (i,j) in possible_hb5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3):
        nopl.append(m - possible_number5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,i,j))
    return min(nopl)


def fton_5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2):
    m = possible_set4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2)
    if len(possible_set4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2)) == 1:
        return possible_set4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2)
    else:
        l3=[1,-10]
        for i in m:
            p3 = g(i)[0]
            q3 = g(i)[1]
            r3 = g(i)[2]
            if nopl5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3) > l3[1]:
                l3.clear()
                l3.append(i)
                l3.append(nopl5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3))
        return l3

def possible_number6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 and \
                    hit_blow(p2,q2,r2,a,b,c)[0] == d2 and hit_blow(p2,q2,r2,a,b,c)[1] == e2 and \
                        hit_blow(p3,q3,r3,a,b,c)[0] == d3 and hit_blow(p3,q3,r3,a,b,c)[1] == e3 and \
                            hit_blow(p4,q4,r4,a,b,c)[0] == d4 and hit_blow(p4,q4,r4,a,b,c)[1] == e4:
            n.append(i)
        else:
            continue
    return len(n)
#Given two pairs of hits and blows, this will give the set of possible numbers that will not contradict the input
def possible_set6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 and \
                    hit_blow(p2,q2,r2,a,b,c)[0] == d2 and hit_blow(p2,q2,r2,a,b,c)[1] == e2 and \
                        hit_blow(p3,q3,r3,a,b,c)[0] == d3 and hit_blow(p3,q3,r3,a,b,c)[1] == e3 and \
                            hit_blow(p4,q4,r4,a,b,c)[0] == d4 and hit_blow(p4,q4,r4,a,b,c)[1] == e4 :
            n.append(i)
        else:
            continue
    return n

def possible_hb6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4):
    l1 = []
    l2 = [(3,0), (2,0), (1,2), (1,1),(1,0), (0,3), (0,2), (0,1), (0,0)]
    for (i,j) in l2:
        if possible_number6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,i,j) == 0:
            continue
        else:
            l1.append((i,j))
    return l1
    
#nopl2 = number of possibilities eliminated
def nopl6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4):
    m = len(possible_set5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3))
    nopl = []
    for (i,j) in possible_hb6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4):
        nopl.append(m - possible_number6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,i,j))
    return min(nopl)


def fton_6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3):
    m = possible_set5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3)
    if len(possible_set5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3)) == 1:
        return possible_set5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3)
    else:
        l3=[1,-10]
        for i in m:
            p4 = g(i)[0]
            q4 = g(i)[1]
            r4 = g(i)[2]
            if nopl6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4) > l3[1]:
                l3.clear()
                l3.append(i)
                l3.append(nopl6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4))
        return l3

def possible_number7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5,d5,e5):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 and \
                    hit_blow(p2,q2,r2,a,b,c)[0] == d2 and hit_blow(p2,q2,r2,a,b,c)[1] == e2 and \
                        hit_blow(p3,q3,r3,a,b,c)[0] == d3 and hit_blow(p3,q3,r3,a,b,c)[1] == e3 and \
                            hit_blow(p4,q4,r4,a,b,c)[0] == d4 and hit_blow(p4,q4,r4,a,b,c)[1] == e4 and \
                                hit_blow(p5,q5,r5,a,b,c)[0] == d5 and hit_blow(p5,q5,r5,a,b,c)[1] == e5:
            n.append(i)
        else:
            continue
    return len(n)
#Given two pairs of hits and blows, this will give the set of possible numbers that will not contradict the input
def possible_set7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5,d5,e5):
    n = []
    for i in l:
        a = g(i)[0]
        b = g(i)[1]
        c = g(i)[2]
        if hit_blow(x,y,z,a,b,c)[0] == s and hit_blow(x,y,z,a,b,c)[1] == t and \
            hit_blow(p,q,r,a,b,c)[0] == d and hit_blow(p,q,r,a,b,c)[1] == e and \
                hit_blow(p1,q1,r1,a,b,c)[0] == d1 and hit_blow(p1,q1,r1,a,b,c)[1] == e1 and \
                    hit_blow(p2,q2,r2,a,b,c)[0] == d2 and hit_blow(p2,q2,r2,a,b,c)[1] == e2 and \
                        hit_blow(p3,q3,r3,a,b,c)[0] == d3 and hit_blow(p3,q3,r3,a,b,c)[1] == e3 and \
                            hit_blow(p4,q4,r4,a,b,c)[0] == d4 and hit_blow(p4,q4,r4,a,b,c)[1] == e4 and \
                                hit_blow(p5,q5,r5,a,b,c)[0] == d5 and hit_blow(p5,q5,r5,a,b,c)[1] == e5 :
            n.append(i)
        else:
            continue
    return n

def possible_hb7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5):
    l1 = []
    l2 = [(3,0), (2,0), (1,2), (1,1),(1,0), (0,3), (0,2), (0,1), (0,0)]
    for (i,j) in l2:
        if possible_number7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5,i,j) == 0:
            continue
        else:
            l1.append((i,j))
    return l1
    
#nopl2 = number of possibilities eliminated
def nopl7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5):
    m = len(possible_set7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4))
    nopl = []
    for (i,j) in possible_hb7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5):
        nopl.append(m - possible_number7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5,i,j))
    return min(nopl)


def fton_7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4):
    m = possible_set6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4)
    if len(possible_set6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4)) == 1:
        return possible_set6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4)
    else:
        l3=[1,-10]
        for i in m:
            p5 = g(i)[0]
            q5 = g(i)[1]
            r5 = g(i)[2]
            if nopl7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5) > l3[1]:
                l3.clear()
                l3.append(i)
                l3.append(nopl7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4,p5,q5,r5))
        return l3


x = 1
y = 2
z = 3
s,t = input("first guess hit and blow")
s = int(s)
t = int(t)
a1 = fton_2(x,y,z,s,t)
print(a1)
p,q,r = g(a1[0])
d,e = input("2nd guess hit and blow")
d = int(d)
e = int(e)
a2 = fton_3(x,y,z,s,t,p,q,r,d,e)
print(a2)
p1,q1,r1 = g(a2[0])
d1,e1 = input("3rd guess hit and blow")
d1 = int(d1)
e1 = int(e1)
a3 = fton_4(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1)
print(a3)
p2,q2,r2 = g(a3[0])
d2,e2 = input("4th guess hit and blow")
d2 = int(d2)
e2 = int(e2)
a4 = fton_5(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2)
print(a4)
p3,q3,r3 = g(a4[0])
d3,e3 = input("5th guess hit and blow")
d3 = int(d3)
e3 = int(e3)
a5 = fton_6(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3)
print(a5)
p4,q4,r4 = g(a5[0])
d4,e4 = input("6th guess hit and blow")
d4 = int(d4)
e4 = int(e4)
a6 = fton_7(x,y,z,s,t,p,q,r,d,e,p1,q1,r1,d1,e1,p2,q2,r2,d2,e2,p3,q3,r3,d3,e3,p4,q4,r4,d4,e4)
print(a6)