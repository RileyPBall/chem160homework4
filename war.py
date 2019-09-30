from cards import *
import math
ntrials = 1000
for i in range(ntrials):
    adeck=deck()
    bdeck=deck()
    adeck.shuffle()
    bdeck.shuffle()
    awinpile=[]
    bwinpile=[]
    diff=0
    diffratio=0
    ratio=[]
    totalresults=[]
    totalratio=[]
    results=[]
    while adeck.cardsleft()>1:
        acard=adeck.dealcard()
        bcard=bdeck.dealcard()
        if acard.value()>bcard.value():
            awinpile.append(bcard)
            awinpile.append(acard)
        if bcard.value()>acard.value():
            bwinpile.append(acard)
            awinpile.append(bcard)
            diff=(abs(len(awinpile)-len(bwinpile)))
        results.append(diff)
    totalresults.extend(results)
    totalresults.sort()
    totalresults.count(0)
    totalresults.count(2)
    totalresults.count(4)
    totalresults.count(6)
    totalresults.count(8)
    totalresults.count(10)
    totalresults.count(12)
    totalresults.count(14)
    totalresults.count(16)
    totalresults.count(18)
    totalresults.count(20)
    totalresults.count(22)
    totalresults.count(24)
    totalresults.count(26)
    totalresults.count(28)
    totalresults.count(30)
    totalresults.count(32)
    totalresults.count(34)
    totalresults.count(36)
    totalresults.count(38)
    totalresults.count(40)
    totalresults.count(42)
    totalresults.count(44)
    totalresults.count(46)
    totalresults.count(48)
    totalresults.count(50)
    totalresults.count(52)
    ratio.append(totalresults.count(0))
    ratio.append(totalresults.count(2))
    ratio.append(totalresults.count(4))
    ratio.append(totalresults.count(6))
    ratio.append(totalresults.count(8))
    ratio.append(totalresults.count(10))
    ratio.append(totalresults.count(12))
    ratio.append(totalresults.count(14))
    ratio.append(totalresults.count(16))
    ratio.append(totalresults.count(18))
    ratio.append(totalresults.count(20))
    ratio.append(totalresults.count(22))
    ratio.append(totalresults.count(24))
    ratio.append(totalresults.count(26))
    ratio.append(totalresults.count(28))
    ratio.append(totalresults.count(30))
    ratio.append(totalresults.count(32))
    ratio.append(totalresults.count(34))
    ratio.append(totalresults.count(36))
    ratio.append(totalresults.count(38))
    ratio.append(totalresults.count(40))
    ratio.append(totalresults.count(42))
    ratio.append(totalresults.count(44))
    ratio.append(totalresults.count(46))
    ratio.append(totalresults.count(48))
    ratio.append(totalresults.count(50))
    ratio.append(totalresults.count(52))
    totalratio = [i/27 for i in ratio]
    totalratio.sort()
for i in totalresults:
    for j in totalratio:
        print("diff=%4d ratio=%4.2f"%(i,j))
        
    

    
