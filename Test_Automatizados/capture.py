import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



# ClassDef:This class is used to capture screen and others

class capture():
  

    def capture_screen(driver, test_dir,test_name):
       
       current_datetime = datetime.datetime.now()
       year=str(current_datetime)[0:4]
       month=str(current_datetime)[5:7]
       day=str(current_datetime)[8:10]

       hour=str(current_datetime)[11:13]
       minute=str(current_datetime)[14:16]
       seconds=str(current_datetime)[17:19]

       datetime_str=year+month+day+"_"+hour+"_"+minute+"_"+seconds

       path=test_dir+"/"+datetime_str+"_"+test_name+".png"
       sleep(1)

       driver.find_element(By.TAG_NAME, value='body').screenshot(path)



