import sys
import os
import shutil

shutil.copy2('calendar_flx_template.html', 'calendar_flx.html')
shutil.copy2('calendar_bag_template.html', 'calendar_bag.html')

ANC_FLX_status=[]
ANC_BAG_status=[]

for x in range(1, 32):
    ANC_FLX_status.append("NE")
    ANC_BAG_status.append("NE")

# no log -> not performed
dircontent = os.listdir('.')

for f in dircontent:
    
    ## Integrity 001
    if ("INT_001_log_" in f):
    
       ANC_FLX_status=[]
       ANC_BAG_status=[]

       for x in range(1, 32):
           ANC_FLX_status.append("NE")
           ANC_BAG_status.append("NE")
        
       print ("Analysing ..."+f)
       print("corresponding to date "+f[12:])
       year=f[12:16]
       month=f[16:18]
       day=f[18:20]
       
       #print(year+"/"+month+"/"+day)
       
       with open(f, "rt") as log:
           content = log.read()

       # FLX Status
       if "ANC_FLX_OK" in content:
           ANC_FLX_status[int(day)]="OK"
           print("the day "+day+" FLX was OK")
       else:
          ANC_FLX_status[int(day)]="KO"
          print("the day "+day+" FLX was KO")
   
       # BAG Status
       if "ANC_BAG_OK" in content:
           ANC_BAG_status[int(day)]="OK"
           print("the day "+day+" BAG was OK")
       else:
           ANC_BAG_status[int(day)]="KO"
           print("the day "+day+" BAG was KO")


       if(month=="04"):
           with open("calendar_flx.html", "rt") as file:
               rep = file.read()
               with open("calendar_flx.html", "wt") as file:
                   for x in range(0, 31):
                       if((ANC_FLX_status[x]=="OK")):
                           rep = rep.replace('<Aprne>'+str(x)+'</Aprne>','<ok>'+str(x)+'</ok>')
                           #file.write(rep)
                       elif(ANC_FLX_status[x]=="KO"):
                           rep = rep.replace('<Aprne>'+str(x)+'</Aprne>','<ko>'+str(x)+'</ko>')
                   file.write(rep)
            
           with open("calendar_bag.html", "rt") as file:
               rep = file.read()
               with open("calendar_bag.html", "wt") as file:
                   for x in range(0, 31):
                       if((ANC_BAG_status[x]=="OK")):
                           print("Setting BAG OK for "+str(x))
                      
                           rep = rep.replace('<td>  <div class="despNO_apr"> <center> '+str(x)+'  </center> </div>  </td>','<td>  <div class="despOK"> <center> '+str(x)+'  </center> </div>  </td>')
                    
                           
                       elif(ANC_BAG_status[x]=="KO"):
                           print("Setting BAG KO for "+str(x))
                           rep = rep.replace('<td>  <div class="despNO_apr"> <center> '+str(x)+'  </center> </div>  </td>','<td>  <div class="despKO"> <center> '+str(x)+'  </center> </div>  </td>')
                   file.write(rep)
                   
                   
       if(month=="05"):
           with open("calendar_flx.html", "rt") as file:
               rep = file.read()
               with open("calendar_flx.html", "wt") as file:
                   for x in range(0, 31):
                       if((ANC_FLX_status[x]=="OK")):
                           #print(rep)
                           rep = rep.replace('<Mayne>'+str(x)+'</Mayne>','<ok>'+str(x)+'</ok>')
                           #file.write(rep)
                       elif(ANC_FLX_status[x]=="KO"):
                           rep = rep.replace('<Mayne>'+str(x)+'</Mayne>','<ko>'+str(x)+'</ko>')
                   file.write(rep)
      
           with open("calendar_bag.html", "rt") as file:
               rep = file.read()
               with open("calendar_bag.html", "wt") as file:
                   for x in range(0, 31):
                       if((ANC_BAG_status[x]=="OK")):
                           rep = rep.replace('<Mayne>'+str(x)+'</Mayne>','<ok>'+str(x)+'</ok>')
                           #file.write(rep)
                       elif(ANC_BAG_status[x]=="KO"):
                           rep = rep.replace('<Mayne>'+str(x)+'</Mayne>','<ko>'+str(x)+'</ko>')
                   file.write(rep)               

        

