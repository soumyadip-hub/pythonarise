import os 
# print(dir(os))
print(os.getcwd())
print(os.listdir())
os.chdir('/home/kali/Desktop/')
print(os.getcwd())
print(os.stat('temp.txt'))