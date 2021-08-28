from netmiko import ConnectHandler
import random
import threading

def part5(ip):
    new1=ip
    Router = {
        'device_type': 'cisco_ios',
        'ip': new1,
        'password': 'vishal',
        'secret': 'vishal',
        'username': 'vishal',
    }
    net_connect = ConnectHandler(**Router)
    output2 = net_connect.send_command('show ip int brief | include down')
    out34 = net_connect.send_command('show ip int brief | include down', use_textfsm=True )
    print(output2)
    #To get the index value of the down interface
    intdown = set()
    while len(intdown) < 2:
        intdown.add(random.randint(0,  len(out34)- 1))
    #Sending commands to the down interface to make it up
    j = 0
    for i in intdown:
        name = out34[i]['intf']
        IPlist = ['ip address 192.168.1.1 255.255.255.0',
                  'ip address 192.168.2.1 255.255.255.0',
                  'ip address 192.168.3.1 255.255.255.0',
                  'ip address 192.168.4.1 255.255.255.0']
        print('Making interface' + name + ' up')
        commands = ['int ' + name,
                    IPlist[j],
                    'no shut']
        j = j+1
        net_connect.enable()
        net_connect.send_config_set(commands)
    #Printing all the up interfaces
    print("Printing all the up interfaces:" + '\n')
    output3 = net_connect.send_command('show ip int brief | include up')

    #Printing the ECMP routes using logic that ecmp routes network will be dislpayed together.
    print("Printing only ECMP routes present in the routers" + '\n')
    output4 = net_connect.send_command('show ip route', use_textfsm=True)
    for j in range(len(output4) - 1):
        name2 = output4[j]['network']
        name3 = output4[j + 1]['network']
        if name2 == name3:
            ecmp1 = output4[j]
            ecmp2 = output4[j+1]
            print(output4[j])
            print(output4[j + 1])

    #Saving all the file in the interfaces.txt file
    save_file = open("interfaces.txt", "a")
    save_file.write("Connecting to Router IP:" + str(new1) +'\n')
    save_file.write('Printing the interface which are down in the routers' + '\n')
    save_file.write(output2 + '\n')
    save_file.write('Printing the interface which are up in the routers' + '\n')
    save_file.write(output3 + '\n')
    save_file.write("Printing only ECMP routes present in the routers" + '\n')
    save_file.write(str(ecmp1) +'\n')
    save_file.write(str(ecmp2) + '\n' +'\n')
    save_file.close()
    net_connect.disconnect()
    return

#Reading the IPs of the routers
with open('devices_file') as device:
    devices_list = device.read().splitlines()

#Multithreading
thread_list = []
for ip in devices_list:
    thread_list.append(threading.Thread(target = part5, args=(ip,)))
for config_thread in thread_list:
    config_thread.start()
for config_thread in thread_list:
    config_thread.join()


