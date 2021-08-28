from netmiko import ConnectHandler

with open('R3.txt') as R3:
    commands_list = R3.read().splitlines()

print ('Connecting to device R3')
ios_device = {
        'device_type': 'cisco_ios',
        'ip': '10.110.161.24',
        'username': 'vishal',
        'password': 'vishal',
        'secret' : 'vishal'
}

net_connect = ConnectHandler(**ios_device)
net_connect.enable()
output = net_connect.send_config_set(commands_list)
print (output)