import os
import time

dev = os.popen("adb devices")
a = dev.read()
list = a.split('\n')
device_list = []

for temp in list:
    if len(temp.split()) > 1:
        if temp.split()[1] == 'device':
            device_list.append(temp.split()[0])
command = ""
print('scan %s android dev' % len(device_list))
for device_name in device_list:
    print(device_name)
for device in device_list:
    print("prepare %s dev scrcpy" % device)
    command = "scrcpy -s "+device
    os.popen(command)
    time.sleep(2)
