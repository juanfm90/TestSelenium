import os
import hashlib

print("Loading build coherence...")
dic=[]

with open('build_coherence.cfg',"r") as fr:
    for line in fr:
        if("|->" in line): 
#            print(line.split("[")[1].split("]")[0])
            dic.append(line.split("[")[1].split("]")[0])	 


print("Checking build coherence...")

print("\nTest_Automatizados\n")

for elem in sorted(os.listdir("Test_Automatizados")):

    if((".py" in elem) or (".xlsx" in elem) or (".cmd" in elem)): 
        if(hashlib.md5(open("Test_Automatizados/"+elem,'rb').read()).hexdigest() in dic):
            print(chr(27)+"[32;40m"+"   |-> ["+ hashlib.md5(open("Test_Automatizados/"+elem,'rb').read()).hexdigest()  +"]   "+elem)
        else: print(chr(27)+"[31;40m"+"   |-> ["+ hashlib.md5(open("Test_Automatizados/"+elem,'rb').read()).hexdigest()  +"]   "+elem)

print("\nSetup")
for elem in sorted(os.listdir("Setup")):
    if((".py" in elem) or (".xlsx" in elem) or (".cmd" in elem)):
        if(hashlib.md5(open("Setup/"+elem,'rb').read()).hexdigest() in dic):
            print(chr(27)+"[32;40m"+"   |-> ["+ hashlib.md5(open("Setup/"+elem,'rb').read()).hexdigest()  +"]   "+elem)
        else: print(chr(27)+"[31;40m"+"   |-> ["+ hashlib.md5(open("Setup/"+elem,'rb').read()).hexdigest()  +"]   "+elem)


