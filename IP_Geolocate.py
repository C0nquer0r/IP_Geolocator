import os
import json
import sys


Banner = """
\-/-\-\-/-\-\-/-\-\-/-\-\-/-\-\-/-\-\-/-\-\-
    .--'';'-.
  ,'   <_-,- .`.       IP-Geolocation Finder
 /)   ,---,__>\_\      Created By: C0nquer0r
|' . (  IP *  \_ |
|_    `--.     / |     < Have Fun Finding! >
 \`-. ,  ;   _(>/
  `.(     \_/ ,'  ['exit' or ctrl-c to quit]
    `-.:;...-'
/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-/-\-
"""

print(Banner)

def Geolocate(IP):
    URL = "http://ip-api.com/json/"+str(IP)
    data = str(os.popen("curl -s "+URL).read())
    obj = json.loads(data)
    for item in obj:
        print(str(item)+" : "+str(obj[item]))

def Interactive():
    while True:
        IN = input("\nIP: ").rstrip()
        if (IN == "exit"):
            break
        elif (IN == ""):
            print("No IP Given... Using Host IP")
            Geolocate("")
        else:
            try:
                Geolocate(IN)
            except Exception: pass;

if len(sys.argv) == 2:
    Geolocate(sys.argv[1])
else:
    Interactive()
