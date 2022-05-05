import sys
import os
import shutil
from datetime import date

# current date
today = date.today()
d1 = today.strftime("%Y%m%d")

shutil.copy2('results_template.html', 'results.html')

INT_001_BAG_perf_status="test-result-step-result-cell-notperformed"
INT_001_BAG_perf_result="Not_performed"
ST_001_perf_status="test-result-step-result-cell-notperformed"
ST_001_perf_result="Not_performed"
ST_002_perf_status="test-result-step-result-cell-notperformed"
ST_002_perf_result="Not_performed"
ST_003_perf_status="test-result-step-result-cell-notperformed"
ST_003_perf_result="Not_performed"
ST_011_perf_status="test-result-step-result-cell-notperformed"
ST_011_perf_result="Not_performed"
ST_012_perf_status="test-result-step-result-cell-notperformed"
ST_012_perf_result="Not_performed"
ST_013_perf_status="test-result-step-result-cell-notperformed"
ST_013_perf_result="Not_performed"

# no log -> not performed
dircontent = os.listdir('.')

for f in dircontent:

    ## INT 001 BAG
    #print(f)
    #print("INT_001_log_"+str(d1))
    if (f=="INT_001_log_"+str(d1)):
       # ejecucion de INT_001
       print ("Analysing INT_001_log..."+f)
       with open(f, "rt") as log:
           content = log.read()
       if "ANC_BAG_OK" in content:
           INT_001_BAG_perf_status="test-result-step-result-cell-ok"
           INT_001_BAG_perf_result="OK"
           print("INT_001_BAG OK")
       else:
           INT_001_BAG_perf_status="test-result-step-result-cell-failure"
           print("INT_001_BAG KO")
           INT_001_BAG_perf_result="KO"
           
    ## Sanity 001
    if (f=="Sanity_001_log"):
       print ("Analysing Sanity_001_log...")
       with open("Sanity_001_log", "rt") as log:
           content = log.read()
       if "Sanity_001_OK" in content:
           ST_001_perf_status="test-result-step-result-cell-ok"
           ST_001_perf_result="OK"
           print("ST_001 OK")
       else:
           ST_001_perf_status="test-result-step-result-cell-failure"
           print("ST_001 KO")
           ST_001_perf_result="KO"

    ## Sanity 002
    if (f=="Sanity_002_log"):
       print ("Analysing Sanity_002_log...")
       with open("Sanity_002_log", "rt") as log: 
           content = log.read()
       if "Sanity_002_OK" in content:
           ST_002_perf_status="test-result-step-result-cell-ok"
           ST_002_perf_result="OK"
           print("ST_002 OK")
       else:
           ST_002_perf_status="test-result-step-result-cell-failure"
           print("ST_002 KO")
           ST_002_perf_result="KO"

    ## Sanity 003
    if (f=="Sanity_003_log"):
       print ("Analysing Sanity_003_log...")
       with open("Sanity_003_log", "rt") as log:
           content = log.read()
       if "Sanity_003_OK" in content:
           ST_003_perf_status="test-result-step-result-cell-ok"
           ST_003_perf_result="OK"
           print("ST_003 OK")
       else:
           ST_003_perf_status="test-result-step-result-cell-failure"
           print("ST_003 KO")
           ST_002_perf_result="KO"
           
     ## Sanity 011
    if (f=="Sanity_011_log_Tarjeta_Regalo_Directa"):
       print ("Analysing Sanity_011_log_Tarjeta_Regalo_Directa...")
       with open("Sanity_011_log_Tarjeta_Regalo_Directa", "rt") as log:
           content = log.read()
       if "Tarjeta_Regalo_Directa_OK" in content:
           ST_011_perf_status="test-result-step-result-cell-ok"
           ST_011_perf_result="OK"
           print("ST_011 OK")
       else:
           ST_011_perf_status="test-result-step-result-cell-failure"
           print("ST_011 KO")
           ST_011_perf_result="KO"
           
    ## Sanity 012
    if (f=="Sanity_012_log"):
       print ("Analysing Sanity_012_log...")
       with open("Sanity_012_log", "rt") as log:
           content = log.read()
       if "Sanity_012_OK" in content:
           ST_012_perf_status="test-result-step-result-cell-ok"
           ST_012_perf_result="OK"
           print("ST_012 OK")
       else:
           ST_012_perf_status="test-result-step-result-cell-failure"
           print("ST_012 KO")
           ST_012_perf_result="KO"

    ## Sanity 013
    if (f=="Sanity_013_log_Tarjeta_Regalo_Terceros"):
       print ("Analysing Sanity_013_log_Tarjeta_Regalo_Terceros...")
       with open("Sanity_013_log_Tarjeta_Regalo_Terceros", "rt") as log:
           content = log.read()
       if "Tarjeta_Regalo_Terceros_OK" in content:
           ST_013_perf_status="test-result-step-result-cell-ok"
           ST_013_perf_result="OK"
           print("ST_013 OK")
       else:
           ST_013_perf_status="test-result-step-result-cell-failure"
           print("ST_013 KO")
           ST_013_perf_result="KO"
           
          
    ## Sanity 014
    if (f=="Sanity_014_log_Gestor_Bonos"):
       print ("Analysing Sanity_014_log_Gestor_Bonos...")
       with open("Sanity_014_log_Gestor_Bonos", "rt") as log:
           content = log.read()
       if "ST_014_Gestor_bonos_OK" in content:
           ST_014_perf_status="test-result-step-result-cell-ok"
           ST_014_perf_result="OK"
           print("ST_014 OK")
       else:
           ST_014_perf_status="test-result-step-result-cell-failure"
           print("ST_014 KO")
           ST_014_perf_result="KO"

with open("results.html", "rt") as file:
    x = file.read()
		
    with open("results.html", "wt") as file:
        x = x.replace("test-result-step-result-cell-notperformed_INT_001_BAG",INT_001_BAG_perf_status)
        x = x.replace("INT_001_BAG_Result",INT_001_BAG_perf_result)
        
        x = x.replace("test-result-step-result-cell-notperformed_Sanity_001",ST_001_perf_status)
        x = x.replace("Sanity_001_Result",ST_001_perf_result)
        
        x = x.replace("test-result-step-result-cell-notperformed_Sanity_002",ST_002_perf_status)
        x = x.replace("Sanity_002_Result",ST_002_perf_result)
        
        x = x.replace("test-result-step-result-cell-notperformed_Sanity_003",ST_003_perf_status)
        x = x.replace("Sanity_003_Result",ST_003_perf_result)
        
        x = x.replace("test-result-step-result-cell-notperformed_Sanity_011",ST_011_perf_status)
        x = x.replace("Sanity_011_Result",ST_011_perf_result)
        
        x = x.replace("test-result-step-result-cell-notperformed_Sanity_012",ST_012_perf_status)
        x = x.replace("Sanity_012_Result",ST_012_perf_result)
        
        
        x = x.replace("test-result-step-result-cell-notperformed_Sanity_013",ST_013_perf_status)
        x = x.replace("Sanity_013_Result",ST_013_perf_result)
        
        x = x.replace("test-result-step-result-cell-notperformed_Sanity_014",ST_014_perf_status)
        x = x.replace("Sanity_014_Result",ST_014_perf_result)
        
        file.write(x)

