from netmiko import ConnectHandler
def part2(ip,config):
    print('Connecting to device" ' + ip)
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip,
        'username': 'vishal',
        'password': 'vishal',
        'secret': 'vishal'
    }
    net_connect = ConnectHandler(**ios_device)
    net_connect.enable()
    output = net_connect.send_config_set(config)
    print(output + '\n')
    return

with open('R1.txt') as R1:
    commands_list_R1 = R1.read().splitlines()
with open('R2.txt') as R2:
    commands_list_R2 = R2.read().splitlines()

with open('devices_file.txt') as devices:
    devices_list = devices.read().splitlines()

part2(devices_list[0], commands_list_R1)
part2(devices_list[1], commands_list_R2)