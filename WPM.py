from time import time
a=input("Press Enter to start")
initial=time() #start to type
string=input("Enter some sentence: ")
final=time()
words=string.split()
n=len(words)
print(n,words,final-initial)

time_h=float((final-initial)/60)
print(time_h)
print("Words per minutes are: ",int(n/time_h))