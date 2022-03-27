linedata=open('score2.txt','r',encoding='UTF-8')
next(linedata)
ls1=[]
ls2=[]
ls3=[]
ls4=[]
b=0
c=0
for line in linedata:
    a=line.split()
    if int(a[3])==2:
        ls1.append(int(a[1]))
        ls2.append(int(a[2]))
    else:
        ls3.append(int(a[1]))
        ls4.append(int(a[2]))
print("2年级专业课1成绩：{}".format(ls1))
print("2年级专业课2成绩：{}".format(ls2))
print("3年级专业课1成绩：{}".format(ls3))
print("3年级专业课2成绩：{}".format(ls4))
print("2年级人数：{}".format(len(ls1)))
print("3年级人数：{}".format(len(ls3)))
print("2年级专业课1成绩总和：{}".format(sum(ls1)))
print("2年级专业课2成绩总和：{}".format(sum(ls2)))
print("3年级专业课1成绩总和：{}".format(sum(ls3)))
print("3年级专业课2成绩总和：{}".format(sum(ls4)))
print("2年级专业课1成绩平均分：{:.2f}".format(sum(ls1)/len(ls1)))
print("2年级专业课2成绩平均分：{:.2f}".format(sum(ls2)/len(ls2)))
print("3年级专业课1成绩平均分：{:.2f}".format(sum(ls3)/len(ls3)))
print("3年级专业课2成绩平均分：{:.2f}".format(sum(ls4)/len(ls4)))
print("2年级专业课1成绩最高分：{}".format(max(ls1)))
print("2年级专业课2成绩最高分：{}".format(max(ls2)))
print("3年级专业课1成绩最高分：{}".format(max(ls3)))
print("3年级专业课2成绩最高分：{}".format(max(ls4)))
print("2年级专业课1成绩最低分：{}".format(min(ls1)))
print("2年级专业课2成绩最低分：{}".format(min(ls2)))
print("3年级专业课1成绩最低分：{}".format(min(ls3)))
print("3年级专业课2成绩最低分：{}".format(min(ls4)))
for i in range(len(ls1)):
    if ls1[i]<60 or ls2[i]<60:
        b+=1
for i in range(len(ls3)):
    if ls3[i]<60 or ls4[i]<60:
        c+=1
print("2年级不及格人数：{}".format(b))
print("3年级不及格人数：{}".format(c))
linedata.close()