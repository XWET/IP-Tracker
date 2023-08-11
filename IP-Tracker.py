#!/usr/bin/python3
import requests
import json
import sys
import time
from colorama import init, Fore
import os

os.system('cls' if os.name == 'nt' else 'clear')


#colors
init()
GREEN = Fore.GREEN
RED = Fore.RED
LIGHT = Fore.LIGHTBLUE_EX
WHITE = Fore.WHITE


print(f"""\n{LIGHT}{WHITE}
      
    ██╗██████╗     ████████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗ 
    ██║██╔══██╗    ╚══██╔══╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
    ██║██████╔╝       ██║   ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
    ██║██╔═══╝        ██║   ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
    ██║██║            ██║   ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
    ╚═╝╚═╝            ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                 
""")


def progres_bar(part, total, length=30):
    frac = part / total
    completed = int(frac * length)
    missing = length - completed
    bar = f"{'#'* completed}{'-'* missing}{frac: .2%}"
    return bar

n = 30

print(f"""
{WHITE}Telegram :{RED}  @AimFov
{WHITE} Github  :{RED}  XWET - Amaru

{RED}
1 {WHITE} : START
{RED}99 {WHITE}: Exit
""")


exit = int(input(f"{GREEN}Enter : "))

url = "http://ip-api.com/json/"

def main():
    try:
        ip = input("\nEnter your target IP : ")

        req = requests.get(url+ip)

        data = req.text

        value = json.loads(data)

        if value['status'] == "success":
            print("\n")
            for i in range(n + 1):
                time.sleep(0.1)
                print(progres_bar(i, n, 50), end="\r")
            print("\n")
            print(f"""
                {WHITE}IP :         {GREEN}  {value['query']}
                {WHITE}ISP :        {GREEN}  {value['isp']}
                {WHITE}Country :     {GREEN} {value['country']}
                {WHITE}County code : {GREEN} {value['countryCode']}
                {WHITE}Region :      {GREEN} {value['region']}
                {WHITE}City :        {GREEN} {value['city']}
                {WHITE}Region Name : {GREEN} {value['regionName']}
              {WHITE}  AS :         {GREEN}  {str(value['as'])}
                {WHITE}Time Zone :  {GREEN}  {value["timezone"]}
                {WHITE}Latitude :  {GREEN}   {str(value['lat'])}
               {WHITE} Longitude :  {GREEN}  {str(value['lon'])}
                
            """)
        else:
            print("Your ip address is invaild ")
    except:
        print("Make sure you have internet connection")
              

if __name__ == "__main__":
    if exit == 1:
        main()
    elif exit == 99:
        print (f" {RED} see more tools in telegram {WHITE} @Aimfov {RED} :) ")
        sys.exit()
