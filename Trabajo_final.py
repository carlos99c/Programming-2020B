list = ["2,4,6,8,10","1,3,7,9,10"]

listA = list[0].split(sep=',')
listB = list[1].split(sep=',')


print("\n::: INTERSECCIÓN ::: \n")
i=0
counter=0
while i < len(listA) :
  j=0
  while j < len(listB) :
    if listA[i] == listB[j] :
      print ("lista A",listA[i])
      counter+=1
    j+=1
  i+=1

if counter == 0 :
  print("no hay numeros repetidos en la lista")


list = ["1,2,3,4,5,6","1,2,3,4,5,6"]

listA = list[0].split(sep=',')
listB = list[1].split(sep=',')


print(" ::: INTERSECCIÓN ::: ")
i=0
counter=0
while i < len(listA) :
  j=0
  while j < len(listB) :
    if listA[i] == listB[j] :
      print ("lista B",listA[i])
      counter+=1
    j+=1
  i+=1

if counter == 0 :
  print("no hay numeros repetidos en la lista")


list = ["5,10,15,20,25,30","1,14,21,28,35"]

listA = list[0].split(sep=',')
listB = list[1].split(sep=',')


print("\n::: INTERSECCIÓN ::: \n")
i=0
counter=0
while i < len(listA) :
  j=0
  while j < len(listB) :
    if listA[i] == listB[j] :
      print ("lista c",listA[i])
      counter+=1
    j+=1
  i+=1

if counter == 0 :
  print("no hay numeros repetidos en la lista")