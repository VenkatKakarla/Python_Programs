# (20.2) Using try block and except ,finally block.
try:
    print('Open the file')
    a,b=[int(i) for i in input('enter two numbers:').split()]
    c=a/b
except Exception as obj:
    print(obj)
else:
    print('result=',c)
finally:
    print('close all files')
