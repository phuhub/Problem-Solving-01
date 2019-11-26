import time
start= time.time()
text="THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"
text2=text.split()
text3=text2[0]
text4=text2[1]
text5=text2[2]
text6=text2[3]
text7=text2[4]
text8=text2[5]
text9=text2[6]
text10=text2[7]
text11=text2[8]



zero1=ord(text3[0])
zero2=ord(text3[1])
zero3=ord(text3[2])
allzero=zero1+zero2+zero3


one1=ord(text4[0])
one2=ord(text4[1])
one3=ord(text4[2])
one4=ord(text4[3])
one5=ord(text4[4])
allone=one1+one2+one3+one4+one5

two1=ord(text5[0])
two2=ord(text5[1])
two3=ord(text5[2])
two4=ord(text5[3])
two5=ord(text5[4])
alltwo=two1+two2+two3+two4+two5

three1=ord(text6[0])
three2=ord(text6[1])
three3=ord(text6[2])
allthree=three1+three2+three3


four1=ord(text7[0])
four2=ord(text7[1])
four3=ord(text7[2])
four4=ord(text7[3])
four5=ord(text7[4])
allfour=four1+four2+four3+four4+four5

five1=ord(text8[0])
five2=ord(text8[1])
five3=ord(text8[2])
five4=ord(text8[3])
allfive=five1+five2+five3+five4

six1=ord(text9[0])
six2=ord(text9[1])
six3=ord(text9[2])
allsix=six1+six2+six3

sev1=ord(text10[0])
sev2=ord(text10[1])
sev3=ord(text10[2])
sev4=ord(text10[3])
allsev=sev1+sev2+sev3+sev4

eig1=ord(text11[0])
eig2=ord(text11[1])
eig3=ord(text11[2])
alleig=eig1+eig2+eig3

print(allzero+allone+alltwo+allthree+allfour+allfive+allsix+allsev+alleig)
end=time.time()
print("Time : ",(end-start)*1000)