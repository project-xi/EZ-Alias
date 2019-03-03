#!usr/bin/python3
import time 
import subprocess
Text="EZ BASH!!!\n"
# Print Into 
Intro = """

  sSSs   sdSSSSSSSbs         .S_SSSs     .S_SSSs      sSSs   .S    S.   
 dSSSP   YSSSSSSSS%S        .SS~SSSSS   .SS~SSSSS    dSSSP  .SS    SS.  
d%S'            S%S         S%S   SSSS  S%S   SSSS  d%S'    S%S d   S%S  
S%S            S&S          S%S    S%S  S%S    S%S  S%|     S%S    S%S  
S&S           S&S           S%S SSSS%P  S%S SSSS%S  S&S     S%S SSSS%S  
S&S_Ss        S&S           S&S  SSSY   S&S  SSS%S  Y&Ss    S&S  SSS&S  
S&S~SP       S&S            S&S    S&S  S&S    S&S  `S&&S   S&S    S&S  
S&S         S*S             S&S    S&S  S&S    S&S    `S*S  S&S    S&S  
S*b        S*S              S*S    S&S  S*S    S&S     l*S  S*S    S*S  
S*S.     .s*S               S*S    S*S  S*S    S*S    .S*P  S*S    S*S  
 SSSbs   sY*SSSSSSSP        S*S SSSSP   S*S    S*S  sSS*S   S*S    S*S  
  YSSP  sY*SSSSSSSSP        S*S  SSY    SSS    S*S  YSS'    SSS    S*S  
                            SP                 SP                  SP   
                            Y                  Y                   Y   
LyhourChhen (11-Project)                                                                                                                                                                                                                           
"""
print(Intro)
programStart=("Pls becareful to use this software! ")
def menuloading(loadText):
    "This function to provide an greeting style for most script...."
    loading=1
    for i in range(1,100):
        print("Loading :",loading,"%")
        time.sleep(0.1)
        loading +=1
        if loading==100:
            print(programStart)
            loadText=""
            for ii in loadText:
                print(ii,end="")
                time.sleep(0.1)              
menuloading("Program is starting...")
subprocess.call(['./EZ-Alias.sh'])