"""def greet():
    print('goodmorning')
greet()
print("Hellow")
greet()
#function argument
def display_info():
    name =input("What is your name? ")
    country=input("what is your country name?")
    print(name)
    print(country)
display_info()"""
#insert element using insert operations
def insert(arr,element):
    arr.append(element)
    #Driver's code
if __name__=='__main__':
    #declaring array and value to insert
    LA=[0,0,0]
    x=0
    #print array before inserting element
    print("Array Before Insertion:")
    for x in range(len(LA)):
        print('LA',[x],'=',LA[x])
    print("Inserting elements")
#Arrays after inserting element
for x in range(len(LA)):
    LA.append(x);
    LA[x]=x+1;
print("arrays after insertion:")
for x in range (len(LA)):
    print('LA',[x],'=',LA[x])
#python program to delete the value using delete operation
