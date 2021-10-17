value1=4
value2=12
# list1=[2,4,6,-8]
list2=[42,8,15,23,42]
def insertShiftArray(listParam,value1):
  myList=[]
  if len(listParam)%2==0:
    result=int(len(listParam)/2)
  else:
    result=int(len(listParam)/2)+1
  myList = listParam[0:result]+[value1]
  myList = myList+listParam[result:len(listParam)]
  return myList
print(insertShiftArray(list2,value2))