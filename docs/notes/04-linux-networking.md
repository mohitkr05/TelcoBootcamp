# Linux networking explained

## Network Interface Cards (NICs)

- NICs are physical components that allow a Linux system to connect to a network.
- Each NIC has a unique MAC address, which is used for network identification.
- Common NIC types include Ethernet, Wi-Fi, and fiber optics.

### How to check NICs in Linux
- `ifconfig`

```
enp0s3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.2.15  netmask 255.255.255.0  broadcast 10.0.2.255
        inet6 xxxx::xxxxx:xxxx:xxxx:3xxx  prefixlen 64  scopeid 0x20<link>
        ether xx:xx:xx:xx:xx:xx  txqueuelen 1000  (Ethernet)
        RX packets 93930  bytes 136962512 (136.9 MB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 16935  bytes 1228243 (1.2 MB)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

In the above outpuit the following details are captured

- `enp0s3`: NIC name
- `flags=4163<UP,BROADCAST,RUNNING,MULTICAST>`: NIC flags
- `mtu 1500`: Maximum transmission unit
- `inet 10.0.2.15`: IP address
- `netmask 255.255.255.0`: Subnet mask
-  `inet6 xxxx::xx:xxxx:xxxx:xxxx` - IPv6 Address
- `xxxx::xx:xxxx:xxxx:xxxx` - IPv6 link-local address .
- `prefixlen 64` - The prefix length for the IPv6 address is 64 bits, which is a common configuration for local networks.
- `scopeid 0x20<link>` - Scope ID: This indicates the scope of the address, which is link-local (only valid in the local network segment).
- `MAC Address: ether 02:d2:x6:x7:xd:x7` - The hardware MAC address of the network interface
- `txqueuelen 1000`: The transmit queue length is set to 1000.
- RX (Recieve) Statistics:
    - RX packets 93930: The number of received packets is 93,930.
    - bytes 136962512 (136.9 MB): The total size of received data is approximately 136.9 MB.
    - RX errors 0: No receive errors.
    - dropped 0: No dropped packets.
    - overruns 0: No overruns.
    - frame 0: No frame errors.
- TX (Transmit) Statistics:
    - TX packets 16935: The number of transmitted packets is 16,935.
    - bytes 1228243 (1.2 MB): The total size of transmitted data is approximately 1.2 MB.
    - TX errors 0: No transmit errors.
    - dropped 0: No dropped packets.
    - overruns 0: No overruns.
    - carrier 0: No carrier errors.
    - collisions 0: No collisions.


### Validate arps

The ip to mac resolution is handled by the layer two broadcast protocol arp. The arp table
can be displayed with the arp tool. The screenshot below shows the list of computers that
this computer recently communicated with

```
# arp
Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.2.3                 ether   ----:--:--:--:--:--   C                     enp0s3
_gateway                 ether   ----:--:--:--:--:--   C                     enp0s3
```

## Validate the routes

View the route table with `netstat -r` or `route`

```
# route
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
default         _gateway        0.0.0.0         UG    100    0        0 enp0s3
10.0.2.0        0.0.0.0         255.255.255.0   U     100    0        0 enp0s3
_gateway        0.0.0.0         255.255.255.255 UH    100    0        0 enp0s3
10.0.2.3        0.0.0.0         255.255.255.255 UH    100    0        0 enp0s3
192.168.56.0    0.0.0.0         255.255.255.0   U     0      0        0 enp0s8

```



2. TCP/IP Protocol Stack

    TCP/IP is the standard networking protocol suite used in Linux systems.
    It consists of a layered model, with each layer responsible for specific tasks.
    Key layers include the Link Layer, Internet Layer, Transport Layer, and Application Layer.

3. IP Addressing

    IP addresses are unique identifiers assigned to devices on a network.
    IPv4 addresses are 32-bit numbers, while IPv6 addresses are 128-bit numbers.
    IP addresses are used to route data packets between devices on the network.

4. Subnetting

    Subnetting is the process of dividing a network into smaller subnets.
    Subnets are created by dividing the IP address into a network portion and a host portion.
    Subnetting improves network performance and security.

5. Network Routing

    Routing is the process of directing data packets to their intended destinations.
    Routers are devices that forward data packets based on their IP addresses.
    Linux systems can act as routers, forwarding traffic between networks.

6. Network Services

    Linux systems can provide a variety of network services, such as web servers, email servers, and file servers.
    These services allow Linux systems to share resources and communicate with other devices on the network.

7. Network Security

    Network security is essential for protecting Linux systems from unauthorized access and attacks.
    Firewalls, intrusion detection systems (IDS), and encryption are common security measures.
    Linux systems offer various security tools and configurations to protect against network threats.

8. Network Troubleshooting

    Network troubleshooting involves identifying and resolving network problems.
    Common troubleshooting tools include ping, netstat, and ifconfig.
    Understanding network protocols and concepts is crucial for effective troubleshooting.

9. Network Configuration

    Network configuration involves setting up and managing network settings on Linux systems.
    This includes configuring IP addresses, network interfaces, and routing tables.
    Network configuration tools vary depending on the Linux distribution.

10. Network Monitoring

    Network monitoring involves tracking and analyzing network performance and health.
    Monitoring tools provide insights into network traffic, resource utilization, and potential issues.
    Continuous network monitoring helps maintain network stability and identify potential problems early on.

11. Sockets

- Sockets are fundamental building blocks of network communication in Linux, providing a standardized way for processes to exchange data across a network. 
- They act as endpoints for communication, allowing processes to send and receive data over a network connection. 
- Sockets are essential for implementing various network applications, such as web servers, file transfer clients, and chat programs.

Linux supports two primary types of sockets:

- Stream sockets: These sockets provide a reliable, byte-oriented, and ordered data transmission. They maintain a connection between the communicating parties and ensure data delivery in the correct sequence. Stream sockets are commonly used for protocols like TCP, which is the foundation for many network applications like web browsing and file transfers.

- Datagram sockets: These sockets provide an unreliable, message-oriented, and unordered data transmission. They send data as individual packets, without maintaining a connection between the communicating parties. Datagram sockets are suitable for protocols like UDP, which is often used for applications where speed and low overhead are prioritized over reliable delivery, such as real-time streaming or gaming.

- Socket Addressing: Every socket has a unique address that identifies it on the network. This address consists of two components:
    - IP address: The IP address identifies the network node where the socket resides. It's a 32-bit or 128-bit number for IPv4 and IPv6, respectively.
    - Port number: The port number identifies a specific service or application associated with the socket. Port numbers are 16-bit integers ranging from 0 to 65535. Well-known services, such as web servers and email servers, have standardized port numbers assigned to them.

- Socket Operations: Sockets provide various operations for managing communication, including:
    - Creating a socket: The ``socket()` system call creates a socket and assigns it a unique descriptor.
    - Binding a socket: The `bind()` system call associates a socket with a specific IP address and port number.
    - Connecting a socket: The `connect()` system call establishes a connection with a remote socket identified by its IP address and port number.
    - Sending data: The `send()` system call sends data from the local socket to the connected remote socket.
    - Receiving data: The `recv()` system call receives data from the connected remote socket into the local socket buffer
    - Closing a socket: The `close()` system call terminates the connection and releases the socket resources.
