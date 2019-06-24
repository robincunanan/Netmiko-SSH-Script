# Netmiko SSH Script

This Python script will demonstrate SSH management to multiple network devices such as, ‘show ip int brief’, ‘show ip route’, and ‘ping’ using the Netmiko module. 

## Getting Started

These instructions will perform configuration and show commands on your local machine and network devices for experimentation and to simplify workflow. 

### Prerequisites

The following software is required:
1. [Python 3.5.3+](https://www.python.org/downloads/)
2. [PyCharm 2019.1.1+](https://www.jetbrains.com/pycharm/download/#section=windows)
3. [Netmiko](https://pypi.org/project/netmiko/)
4. [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html)

The following network platforms that is tested with Netmiko can be found on [Pynet](https://pynet.twb-tech.com/blog/automation/netmiko.html).

## Running

1. Setup network topology between local machines and network devices.
2. Setup SSH on network platforms with PuTTY. Guide by [NHGainesville](https://youtu.be/3v3Iw87vEQ8).
3. Verify devices can ping each other and if you're able to SSH through network device. Turn off firewall if necessary. 
4. Once installed you can run the program with the following command:

```
NetmikoScript.py
```

## Thanks
Thank you to Pynet and NHGainesville on help running this script. 
