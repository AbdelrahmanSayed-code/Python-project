#start python 1-10 الرسمه numder 6


print("     /|")
print("    / |")
print("   /  |")
print("  /   |")
print(" /    |")
print("/_____|")


#varables number 7


man ="abdelrahman"
age ="20"
print("he is "+man)
print("he has " +age)
man="ahmed"
#هنا اتغيرت عادي علشان البايثون شغاله ب الانتر برتر 
#""=strang
print(man +" is ENG")
print(age +" yaers ago he was born")


#string   8


text ="theking"
#.upper&replace=function /[]=arry
#.lower بيخلي الحروف s
#.upper بيخلي الحروف k
#len    بيشوف طول الكلمه 
#index  بيجيب رقم البت الي فيها الحرف
#rplace بيبدل كلمتين معا بعض
print(text.upper())
print(text.isupper)
print(text [0]) 
print(text.replace("the","AL"))
print(text.index("k"))


# numbers 9


print (str(5) +("is my num"))
#function numbers
#abs convart - to +
#pow بياخد رقمين الرقم الاول اس التاني
#max بتاخد رقمين بتقلك مين الاكبر 
#min عكس ال max
#round بتاخد الرقم و تقربه لاقرب جزء من 10
print(abs (-5))
print(pow(5,2))
print(round(5.5))
print(max(6,6.6))


#number 2/ 10


name =input("enter your name:")
age =input("inter your yeer")
print ("hello "+name)
#يجب اضافهint لكي يتعامل معامله الارقام
print (2026-int(age))
#leson 2
# buld calculator  11

# في المتغيرات لما تستخدم input مع الارقام لازم تحط قبليها float
num1= float(input("enter the firest number"))
num2= float( input("enter the scand number"))
result =(num1)+(num2)
print (result) 

#Build MadLibs in Python 12

name =input("enter your name")
age  =input("enter your age")
job  =input("enter your job")
print("your name is "+name)
print("i have "+(age)+" yers old")
print("my job is "+job)

#{Python Lists}   13

frinde = ["abdelnaser" ,"alsazly","fadl",16,True,"awny",15,15,15]
colore =["red","brown","blue"]
#[x:y]من xالىyبستثناء y
print (frinde[0:4])
#[x:]من x الى اخر اليست
print (frinde[2:])
#(frinde[x])= كده انت بتخير ال x للقيمه الجديده الي انت هتدهالها


  
#{Python Lists2}     14


#some function   
#liet1.extend(list2) &list1+=list2 لضم 2 ليست 
#list.append(x) لاضافه عنصر في اخر الليست
#list.insert(0,"x")اولا تحديد المكان ثم الاضفه
#list.remove(x)بتمسح العنصر المكتوب
#list.clear()بتمسح كل الليست
#list.pop () بتشيل اخر عنصر في الليست &اقدر اخزنه في متغير ويظهر العنصر الي تمسح
#list.index(x)بتقول ال x في البت رقم كام
#list.count()بتقول ايه عدد العناصر &لو ادتها عنصر تقلك كام واح موجود
#list.sort()ترتيب العناصر حسب الحروف 
#new-list =list.copy()هتطبع نفس الليست
frinde.extend(colore)
print(frinde)
frinde.append(15)
print(frinde)
frinde.insert(3,"ar")
print(frinde)
frinde.remove(16)
print(frinde)
x=frinde.pop(5)
print(x)
print(frinde.index(15))
print(frinde.count(15))
colore.sort()
print(colore)
#frinde.clear()
print(frinde)

#{Python Tuples      15


# Tuples= list بس التابلس ينفعش اغير البيانات الي جواها
cairo=(123,156)
print (cairo[0])
list_of_tupls=[(55,16),(5,16),(856,56)]
#برضوا مقدرش اغير حتى لو حطينها في ليست.
#functions   16

#def functions ( x ,y): وتكنب الداله بعيدا عن كلمه لو ضفتx&y هتتضاف

def say_hi(ade):
    print("hello"+ade)
    name =input ("enter your name")
    age  =input("enter your age")
    print("name is "+name+" age is "+age)
say_hi(" theking")   


#functions 2    17 

def math(num):

    return (num*num*num)
resolt= math(7)
print(resolt)
def sum(x,y):
    print("gj")
    return x+y
plus=sum(5,9)
print(plus)

#Python Conditionals if     18

have_mony=True
buy_car=False
if have_mony & buy_car:
    print("he have mony")
elif have_mony and not buy_car :
    print("pelas buy a car")

else :
    print("he is poor")


#Python Comparisons  if  19

def max_num (num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else :
        return num3 ,
print(max_num(20,22.5,22))


#Build Calculator in Python 2   20

num1 = float(input("enter num1 :"))
num2 =float(input("enter num2 :"))
opretor =input("enter the opretor :")
if opretor =="+":
    print(num2+num1)
elif opretor =="-":
    print(num1-num2)
elif opretor =="*":
    print(num2*num1)
elif opretor =="/":
    print(num1/num2)
else :
    print("rong opretor")
    #Python Dictionaries "key":"valu"        21
month ={
"jen" :"jenere",
"fbr": "fbrale",
"mrs ":"maers",
}
print (month.get ("ff","no valu"))

#while loop       22

#continue    لو عملت كوندشن و حطيتها فيه بلغي الرقم
#break   دي بتطلع من اللوب خالص

i=1
while i<=10 :
    print(i)
    i+=1
else:
 print ("the loop has end")