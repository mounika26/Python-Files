#8.Python Program to Find the Sum of Elements in a List using Recursion
def sumOfElements(list1,size):
    if size==0:
        return 0
    else:
       return list1[size-1]+sumOfElements(list1,size-1)
li1=[1,2,3,4,5]
n=len(li1)
k=sumOfElements(li1,n)
print(k)










# def sum_arr(arr,size):
#    if (size == 0):
#      return 0
#    else:
#      return arr[size-1] + sum_arr(arr,size-1)
# n=int(input("Enter the number of elements for list:"))
# a=[]
# for i in range(0,n):
#     element=int(input("Enter element:"))
#     a.append(element)
# print("The list is:")
# print(a)
# print("Sum of items in list:")
# b=sum_arr(a,n)
# print(b)