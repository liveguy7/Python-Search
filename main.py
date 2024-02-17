
def findElement(arr,n,value):
  for i in range(n):
    if(arr[i] == value):
      return i
  return -1

if __name__ == '__main__':
  LA = [1,3,5,7,9]
  for x in range(len(LA)):
    print(LA[x])
  value = 2
  n = len(LA)
  index = findElement(LA, n, value)

  if(index != -1):
    print("Element ", value, " found at pos ", str(index+1))
  else:
    print("Element not found")


  