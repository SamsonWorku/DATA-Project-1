def Samson(count):
    while count!=100:
      print(count)
      count=count+1;
Samson(0)
Sam = [None, "Fizz", "Buzz", "FizzBuzz"]
v = 0x30490610
for i in range(1, 101):
    j = v & 3
    print(Sam[j] if j else i)
    v = v >> 2 | j << 28
	
	