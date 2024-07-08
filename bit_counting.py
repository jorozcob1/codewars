#Implement a function to convert a number in its binary representation and return the numbers of 1 the number has 
def count_bt(n):
  return str(bin(n))[2:]
print(count_bt(135))