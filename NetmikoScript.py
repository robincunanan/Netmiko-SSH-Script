from netmiko import ConnectHandler

iosv_l3 = { #Login information for Router 1
    'device_type': 'cisco_ios',
    'ip': '10.0.10.1',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l3)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
route = net_connect.send_command('show ip route')
print('THIS IS ROUTER 1')
print(route, output)

print('##########################################################################')

iosv_l2 = { #Login information for Router 2
    'device_type': 'cisco_ios',
    'ip': '10.0.0.254',
    'username': 'cisco',
    'password': 'cisco',
}

net_connect = ConnectHandler(**iosv_l2)
#net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
route = net_connect.send_command('show ip route')
print('THIS IS ROUTER 2')
print(route, output)

print('##########################################################################')

inputping = input('What device do you want to ping? ')
ping = net_connect.send_command('ping ' + inputping) #Pings ED1
print(ping)
