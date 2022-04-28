import os
import hashlib

print("Generating Test_Automatizados build coherence...")

with open('build_coherence.cfg', "w") as bc:
    print("\nTest_Automatizados\n")
    bc.write("\nTest_Automatizados\n")
    for elem in sorted(os.listdir("Test_Automatizados")):

        if((".py" in elem) or (".xlsx" in elem) or (".cmd" in elem)): 
            print("   |-> ["+ hashlib.md5(open("Test_Automatizados/"+elem,'rb').read()).hexdigest()  +"]   "+elem)
            bc.write("   |-> ["+ hashlib.md5(open("Test_Automatizados/"+elem,'rb').read()).hexdigest()  +"]   "+elem+"\n")


    print("\nGenerating Setup build coherence...")

    print("\nSet up\n")
    bc.write("\nSetup\n")
    for elem in sorted(os.listdir("Setup")):
       if((".py" in elem) or (".xlsx" in elem) or (".cmd" in elem)):
           print("   |-> ["+ hashlib.md5(open("Setup/"+elem,'rb').read()).hexdigest()  +"]   "+elem)
           bc.write("   |-> ["+ hashlib.md5(open("Setup/"+elem,'rb').read()).hexdigest()  +"]   "+elem+"\n")

