from netmiko import ConnectHandler

def part1(IP):
    R1 = {
        'device_type': 'cisco_ios',
        'ip': IP,
        'username': 'vishal',
        'password': 'vishal',
    }

    net_connect = ConnectHandler(**R1)
    print("OUTPUT: Show ip int brief in R1" + '\n')
    output = net_connect.send_command('show ip int brief' + '\n')
    print(output + '\n')
    print("OUTPUT: Show version in R1" + '\n')
    output1 = net_connect.send_command('show version') #veriosn, devicename and up are included in show version command
    print(output1)
    return

R1 = '10.110.161.20'
part1(R1)