from netmiko import ConnectHandler

with open('R4.txt') as R4:
    commands_list = R4.read().splitlines()

print ('Connecting to device R4')
ios_device = {
        'device_type': 'cisco_ios',
        'ip': '10.110.161.26',
        'username': 'vishal',
        'password': 'vishal',
        'secret' : 'vishal'
}

net_connect = ConnectHandler(**ios_device)
net_connect.enable()
output = net_connect.send_config_set(commands_list)
print (output)