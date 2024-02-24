alist = ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'blueberry',3,4]
# the word start with 01234567etc..
print("first word:",alist[0])
print("third word:",alist[3])
print("seventh word:",alist[7])
name = ['jaihari','hari','sabari','apple', 'banana', 'cherry', 'mango', 'pineapple', 'blueberry']
# the word start with 01234567etc..
i = name[2:]
print("the list of word:",i)
r = name[3:4:3]
print("the list of word in certain place:",r)
# the word start with 01234567etc..
print(type(i))
# int,float,str,
a = 10
b = 5
c = 2.5
d = 2.3
e = ['apple']
f = ['orange']
Num_a = int(a)
Num_b = int(b)
Num_c = float(c)
Num_d = float(d)
Num_e = str(e)
Num_f = str(f)
total = Num_a + Num_b
total1 = Num_c + Num_d
total2 = Num_e + Num_f
print("int value(numbers):",total)
print("float value(Decimal no):",total1)
print("string value(alphabetic Letters):",total2)
#split function .split()
sentence = "Hello bro, vanakkam"
words = sentence.split()
print("spliting word are:",words)
#joining a function .join(-)
result = "-".join(sentence)
print("join a assign sign (in letter by letter):",result)
passage = ['red', 'green', 'blue']
result1 = "-".join(passage)
print("join a assign sign (in word by word):",result1)
# generate by an references place name or code
country_code = {'india': 1, 'usa': 2, 'japan': 3, 'delhi': 4, 'nepal': 5}
print("references by place name:",country_code['japan'])
#alist functions
alist = ['vignesh']
print("name:",alist)
#.append(-)
alist.append('23')
print("name with append function:",alist)
alist.append("i am vignesh")
alist.append("my age is 23")
print("name with (2) append function:",alist)
#captilize[0] and .capitalize()
captilize = ["i am vignesh"]
captilize[0] = captilize[0].capitalize()
print("captilize the first word in the sentence:",captilize[0])
Name = "my name is vignesh and my age is 23"
Name = Name.capitalize()
print(Name)
#single_string (without quotations)and (with in quotations) double_string
single_string = "I am vignesh, my age is 23"
print("single string refer to don't use the quotations and all{''}:",single_string)
double_string = "I'm vignesh, my age is 23"
print("double string refer to  use the quotations and all{''}:",double_string)
#call a name by an inputing an values (012345678910)
name = "my name is vignesh and my age is 23"
name_list = name[8:25:8]
name_list1 = name[5:21:2]
print("value:",name_list)
print("Value2:",name_list1)
#append with an user input append(-)
Name = []
Age = []
DOB = []
Input_name = input("Enter Name:")
Name.append(Input_name)
print("name:",Name)
Input_age = input("Enter Age:")
Age.append(Input_age)
print("username is:",Name, "user age is:",Age)
Input_DOB = input("Enter ur DOB:")
DOB.append(Input_DOB)
print("user DOB:",DOB)
# if  by calculating the odd or even statement
a = input("number:")
A_Number = int(a)
b = A_Number % 2
if b == 0:
    print("even")
if b == 1:
    print("odd")
# student result
MA = (input("Enter  Marks for MA :"))
Tally = (input("Enter  Marks for Tally :"))
It = (input("Enter  Marks for It :"))
Mis = (input("Enter  Marks for Mis:"))
Hrm = (input("Enter  Marks for Hrm :"))
Num_MA = int(MA)
Num_Tally = int(Tally)
Num_It = int(It)
Num_Mis = int (Mis)
Num_Hrm = int(Hrm)
grand_mark = 500
total_marks = Num_MA + Num_Tally + Num_It + Num_Mis + Num_Hrm
print("TOTAL MARKS:", total_marks)
Percentage = (total_marks / grand_mark) * 100
passing_score = 275
Result = []
student_score = total_marks
if(total_marks < passing_score):
    Result = "Fail"
else:
    Result = "Pass"
percentage = (total_marks / grand_mark) * 100
print(total_marks, "/500", ",", Percentage, Result)


# range      for - in -
for i in range(21):
    print(i)
    even_number = [2,4,6,8,10,12,14,16,18,20]
    sum_first_ten = sum(even_number[ :10 ])
    print("even.number:", sum_first_ten)

#  while statement values
num = 10
while num > 5:
    num = num - 1
    print(num)



