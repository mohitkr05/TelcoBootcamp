# Virtualization 
***Virtualization is the creation of substitutes for real resources.***

## Understanding Virtualization

### Definition

A system or approach for partitioning the resources of computer hardware into multiple execution environments, which is achieved through the application of various concepts or technologies. This includes but is not limited to hardware and software partitioning, time-sharing, partial or complete machine simulation, emulation, quality of service, and numerous other methodologies.


### Virtualization

Virtualization is a technology that enables the creation and management of virtual instances of computing resources, such as servers, storage, and networks. It allows multiple operating systems (OS) and applications to run on a single physical machine, known as the host, thereby optimizing resource utilization, improving efficiency, and providing flexibility in managing IT infrastructure. Here are some key notes on virtualization:


### Types of Virtualization

- Server Virtualization: Involves dividing a physical server into multiple virtual servers, each running its own OS.
- Desktop Virtualization: Enables running multiple desktop instances on a single physical machine or in a centralized server.
- Network Virtualization: Abstracts network resources, allowing the creation of virtual networks that operate independently of the underlying physical network.

## Benefits

- *Consolidation & Resource Optimization*:
  -  Efficiently utilize hardware resources by running multiple virtual instances on a single physical server.
  - Increase server utilization
  - Simplify legacy software migration
  - Host mixed operating systems per physical platform
  - Streamline test and development environments

- *Isolation*: 
  - Isolate applications and operating systems, preventing issues in one virtual machine from affecting others.
  - Isolate software faults
  - Reallocate existing partitions
  - Create dedicated or as-needed failover partitions

- *Cost Savings*: Reduce hardware and maintenance costs by consolidating multiple servers onto a single physical machine.

- *Flexibility*: Easily scale up or down, allocate resources dynamically, and migrate virtual machines between hosts.
 
## Hypervisor

Also known as a Virtual Machine Monitor (VMM), it is a software or firmware that creates and runs virtual machines on the host system.

Two types: Type 1 (bare-metal) runs directly on the hardware, while Type 2 (hosted) runs on top of an existing operating system.

### Virtual Machine (VM)
A software-based emulation of a physical computer, running an operating system and applications independently of the host system.
VMs share the underlying physical resources but operate in isolated environments.

## Virtual Machine Terminology

### Snapshot
A point-in-time image of a virtual machine's state, allowing for easy backup, recovery, and rollback to a specific configuration.

### Containerization
A lightweight form of virtualization that encapsulates applications and their dependencies, allowing them to run consistently across different environments.

### Cloud Computing and Virtualization
Virtualization is a fundamental technology in cloud computing, enabling the efficient allocation of resources and rapid deployment of services.

### Challenges

- Resource Overhead: Virtualization introduces some overhead due to the need for the hypervisor to manage virtual instances.
- Security Concerns: Isolating virtual machines is critical to prevent security breaches and unauthorized access.
- Complexity: Managing a virtualized environment can be complex, requiring skills in both virtualization technologies and underlying systems.



## NFV and NFVi

## DPDK
[DPDK](DPDK.md)