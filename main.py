#THIS SCRIPT WAS TESTED ON THE PYTHON VERSION 3.13.1
#IT MAY NOT WORK ON VERSIONS LATER
#
#SET ENCCDING utf-8 (cp65001)
#
#PLEASE, INSTALL ALL PACKAGES
#    pip install uuid
#    pip install requests
#    pip install psutil
#    pip install gputil
#OR 
#    pip install uuid requests psutil gputil
#
#IF CODE DOESN'T WORK, PLEASE, WRITE TO ME: felibog@bk.ru

print("Loading. It can take 30+ seconds. \n\n")

#imports
import getpass
import os
import time
import platform
import socket
import requests
from uuid import getnode as getmac
import psutil
import json
import GPUtil
import signal

#functions
def correct_size(bts): #convert bytes
    size = 1024
    for item in ["b", "Kb", "Mb", "Gb", "Tb", "Pb"]:
        if bts < size:
            return f"{bts:.2f}{item}"
        bts /= size

def is_cnx_active(): #checking internet connection
    try:
        requests.head("https://google.com")
        return True
    except: 
        return False
a = "Waiting for internet connection..."
while True: #waiting for internet connection
    if is_cnx_active() is True:
        break
    else:
        a += '.'
        print(a)
        time.sleep(1)
        os.system("cls")

#system data
osinfo = platform.uname()
architecture = platform.architecture()
name = getpass.getuser()
host = osinfo.node
ip = socket.gethostbyname(host)
osname = osinfo.system
processor = osinfo.machine
release = osinfo.release
version = osinfo.version
mac = getmac()
processorfrq = psutil.cpu_freq()
timezone = psutil.boot_time()
ram = psutil.virtual_memory()
ipinfo = json.loads(requests.get('http://ipinfo.io/json').text)
phisical_cores = psutil.cpu_count(False)
logic_cores = psutil.cpu_count()
cpu_usage = psutil.cpu_percent()
gpus = GPUtil.getGPUs()
disks = psutil.disk_partitions()
disk_info = dict()
for i in disks:
    disk = list()
    disk.append(i.device)
    disk.append(i.fstype)
    size = psutil.disk_usage(i.device)
    total = size.total; disk.append(total)
    used = size.used; disk.append(used)
    free = size.free; disk.append(free)
    percent = size.percent; disk.append(percent)
    disk_info[i.device] = disk
battery = psutil.sensors_battery()
avaliable_os_signals_1 = (str(signal.valid_signals()).replace("{", "").replace("<", "").replace(">", "").replace("}", "").replace(" ", "").replace("Signals.", "").replace(":", " \t\t (")).split(",")
avaliable_os_signals = list()
for i in avaliable_os_signals_1: i+=")"; avaliable_os_signals.append(i)
active_users = psutil.users()

#full information of system
all = {
"OSname" : osname,
"OSrelease" : release,
"OS Version" : version,
"Avaliable Signals" : avaliable_os_signals,
"User" : name,
"Active Users" : active_users,
"Local IP" : ip,
"Public IP" : ipinfo["ip"],
"Host" : host,
"MAC" : mac,
"Country" : ipinfo["country"],
"Region" : ipinfo["region"],
"City" : ipinfo["city"],
"Postal code" : ipinfo["postal"],
"Timezone" : ipinfo["timezone"],
"Processor" : processor,
"Architecture" : architecture[0],
"CPU Usage %" : f"{cpu_usage}%",
"Current Processor Frequency" : processorfrq.current,
"Min Processor Frequency" : processorfrq.min,
"Max Processor Frequency" : processorfrq.max,
"Physical Cores" : phisical_cores,
"Logical Cores" : logic_cores,
"Threads By Core" : logic_cores//phisical_cores,
"RAM Total" : correct_size(ram.total),
"RAM Used" : correct_size(ram.used),
"RAM Free" : correct_size(ram.available),
"RAM Usage %" : f"{ram.percent}%",
"Battery" : battery
}

os.system("cls")

choice = str()
try:
    print(rf"""
                    __     __              ___                  ___
\      / |  |\  |  |  \   /  \  \      /  \___      \    /  |  |     \      /
 \    /  |  | \ |  |   |  |  |   \    /       |      \  /   |  |---   \    /
  \/\/   |  |  \|  |__/   \__/    \/\/     ___/       \/    |  |___    \/\/ by felibog
          
on Python {platform.python_version()}
""")
    getpass.getpass("Enter to continue, Ctrl+C to exit.")
except:
    raise SystemExit

os.system("cls")

#output to the console
print("Windows-View \nCopyright (c) 2025 Felix Bogomolov \nGitHub: https://github.com/FeliBog/Windows-View/ \n \nOS:")
print("\tOS:", all["OSname"], all["OSrelease"], f"({all['OS Version']})")
print("\tAvaliable Signals:")
for i in all["Avaliable Signals"]:
    print(f"\t\t "+ i)
print("Users:")
print("\tThis User:", all["User"])
print("\tActive Users (Loginned In):")
for i in all["Active Users"]:
    print(f"\t\t{i.name}")
print("Connections:")
print("\tLocal IP:", all["Local IP"])
print("\tPublic IP:", all["Public IP"])
print("\tHost:", all["Host"])
print("\tMAC:", all["MAC"])
print("Public IP Info:")
print("\tCountry:", all["Country"])
print("\tRegion:", all["Region"])
print("\tCity:", all["City"])
print("\tTimezone:", all["Timezone"])
print("Processor:")
print("\tProcessor:", all["Processor"])
print("\tArchitectre:", all["Architecture"])
print("\tUsage:", all["CPU Usage %"])
print("\tProcessor frequency:")
print("\t\tCurrent:", str((all["Current Processor Frequency"]/1000)) + " Ghz")
print("\t\tMin:", str(all["Min Processor Frequency"]/1000) + " Ghz")
print("\t\tMax:", str(all["Max Processor Frequency"]/1000) + " Ghz")
print("\tCores:")
print("\t\tPhysical:", all["Physical Cores"])
print("\t\tLogical:", all["Logical Cores"])
print("\t\tThreads by core:", all["Threads By Core"])
print("Virtual Memory (RAM):")
print("\tTotal:", all["RAM Total"])
print("\tUsed:", all["RAM Used"])
print("\tFree:", all["RAM Free"])
print("\tUsage (%):", all["RAM Usage %"])
print("GPUs:")
for gpu in gpus:
    print(f"\t{gpu.name} (id = {gpu.id})")
    print(f"\t\tGPU Load: {gpu.load*100}%")
    print(f"\t\tMemory:")
    print(f"\t\t\tTotal: {correct_size(gpu.memoryTotal*1024*1024)}")
    print(f"\t\t\tUsed: {correct_size(gpu.memoryUsed*1024*1024)}")
    print(f"\t\t\tFree: {correct_size(gpu.memoryFree*1024*1024)}")
    print(f"\t\tTemperature: {gpu.temperature} °C")
    print(f"\t\tUUID: {gpu.uuid}")
print("Disks:")
for i in disk_info:
    this_disk = disk_info[i]
    print(f"\t{i}")
    print(f"\t\tFile System: {this_disk[1]}")
    print(f"\t\tMemory:")
    print(f"\t\t\tTotal: {correct_size(this_disk[2])}")
    print(f"\t\t\tUsed: {correct_size(this_disk[3])}")
    print(f"\t\t\tFree: {correct_size(this_disk[4])}")
    print(f"\t\t\tPercent: {this_disk[5]}%")
print("Power (Battery):")
print("\tPercent:", str(all["Battery"].percent) + "%")
if all["Battery"].secsleft != psutil.POWER_TIME_UNLIMITED:
    if all["Battery"].secsleft/60 < 60: print("\tTime to discharge: ~" + str(all["Battery"].secsleft//60) + " min")
    else: print("\tTime to discharge: ~" + str(all["Battery"].secsleft//60//60) + " h")
if all["Battery"].power_plugged == True:
    print("\tBattery is charging.")
else:
    print("\tBattery is not charging.")
