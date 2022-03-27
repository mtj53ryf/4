linedata=open('score.txt','r')
a=1
for line in linedata:
    b=0
    ls=[int(s) for s in line.split()]
    print("{}年级成绩：{}".format(a,ls))
    print("{}年级人数：{}".format(a,len(ls)))
    print("{}年级成绩总和：{}".format(a,sum(ls)))
    print("{}年级成绩平均分：{:.2f}".format(a,sum(ls)/len(ls)))
    print("{}年级成绩最高分：{}".format(a,max(ls)))
    print("{}年级成绩最低分：{}".format(a,min(ls)))
    for i in range(len(ls)):
        if ls[i]<60:
            b+=1
    print("{}年级不及格人数：{}".format(a,b))
    print()
    a+=1
linedata.close()