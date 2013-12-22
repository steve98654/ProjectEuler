import pickle 

pospms = (2,3,5,7,11,13,17,19,23,29)

mxind = (29, 18, 12, 10, 8, 8, 7, 7, 6, 5)

p2 = [2**i for i in range(1,30)]
p3 = [3**i for i in range(0,19)]        
p5 = [5**i for i in range(0,13)]        
p7 = [7**i for i in range(0,11)]        
p11 = [11**i for i in range(0,9)]        
p13 = [13**i for i in range(0,9)]        
p17 = [17**i for i in range(0,8)]        
p19 = [19**i for i in range(0,8)]        
p23 = [23**i for i in range(0,7)]        
p29 = [29**i for i in range(0,6)]        

lst = []

for c1 in xrange(0, mxind[0]):
    print c1
    for c2 in xrange(0, min(30-c1, mxind[1])):
        for c3 in xrange(0, min(30-c1-c2, mxind[2])):
            for c4 in xrange(0, min(30-c1-c2-c3, mxind[3])):
                for c5 in xrange(0, min(30-c1-c2-c3-c4,mxind[4])):
                    for c6 in xrange(0, min(30-c1-c2-c3-c4-c5,mxind[5])):
                        for c7 in xrange(0, min(30-c1-c2-c3-c4-c5-c6,mxind[6])):
                            for c8 in xrange(0, min(30-c1-c2-c3-c4-c5-c6-c7,mxind[7])):
                                for c9 in xrange(0,\
                                        min(30-c1-c2-c3-c4-c5-c6-c7-c8,mxind[8])):
                                    for c10 in xrange(0, mxind[9]):
                                        if(c1+c2+c3+c4+c5+c6+c7+c8+c9+c10<30):
                                            lst.append(p2[c1]*p3[c2]*p5[c3]*p7[c4]*p11[c5]\
                                                *p13[c6]*p17[c7]*p19[c8]*p23[c9]*p29[c10])

mxvl = int(1e9)

anums = filter(lambda x: x < mxvl, lst)

pickle.dump(anums, open("anums.p", "wb"))

