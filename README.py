#num1
num1=[3,4,5,7,9]
num2=[1,3,5,7,0]

print(num1)
print(num2)
sum=map(lambda x,y :x+y,num1,num2)
print(list(sum))
#num2
list1=[1,2,3,4,5]

def cube(x):
    return x*x*x
result=map(cube,list1)
print(list(result))
#num3
a={10,20,40,50}
b=["a","b","c","d","e",]

print("a=",a)
print("b=",b)
result=list(zip(a,b))
print("Result",result)
student=["Aman","vibhor","arjun","tarunya"]
roll=[1,2,3,4]
dict={stud:roll for stud,roll in zip(student,roll)}
print("dict=",dict)
#num4
for i in range(10):
    if i==5:
        print("exit")
        exit
    print(i)
