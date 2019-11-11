import os

def get():
    devices = os.popen('ip neigh').read()

    for device in devices.split('\n'):
        ip = device.split('lladdr')[0].split()[0]
        macaddr = device.split('lladdr')[1].split()[0]
        if macaddr == 'b8:27:eb:43:26:90':
            return ip
    return ''
