# Cloud Computing & Telco Cloud

## Checklist for today

- [ ] Understanding Cloud Computing 
- [ ] Brief overview of Telco Cloud
- [ ] Linux and Open source
- [ ] Open source in Telecom
- [ ] Overview of the lectures and course platform
- [ ] Using Git and Github
- [ ] Setting up your dev environment using a VM
- [ ] Linux hands on exercise

## What we are trying to achieve

![Target architecture](../assets/architecture-setup.drawio.png)


## Understanding Cloud Computing


### Definition of Cloud computing

Cloud computing is a model for enabling ubiquitous, convenient, on-demand network access to a shared
pool of configurable computing resources (e.g., networks, servers, storage, applications, and services) that
can be rapidly provisioned and released with minimal management effort or service provider interaction.
This cloud model is composed of five essential characteristics, three service models, and four deployment
models [1]

#### Essential Characteristics
- **On-demand self-service**. A consumer can unilaterally provision computing capabilities, such as server time and network storage, as needed automatically without requiring human interaction with each service provider.
- **Broad network access**. Capabilities are available over the network and accessed through standard mechanisms that promote use by heterogeneous thin or thick client platforms (e.g., mobile phones, tablets, laptops, and workstations).
- **Resource pooling**. The provider’s computing resources are pooled to serve multiple consumers using a multi-tenant model, with different physical and virtual resources dynamically assigned and reassigned according to consumer demand. There is a sense of location independence in that the customer generally has no control or knowledge over the exact location of the provided resources but may be able to specify location at a higher level of abstraction (e.g., country, state, or datacenter). Examples of resources include storage, processing, memory, and network bandwidth.
- **Rapid elasticity**. Capabilities can be elastically provisioned and released, in some cases automatically, to scale rapidly outward and inward commensurate with demand. To the consumer, the capabilities available for provisioning often appear to be unlimited and can be appropriated in any quantity at any time.
- **Measured service**. Cloud systems automatically control and optimize resource use by leveraging a metering capability1 at some level of abstraction appropriate to the type of service (e.g.,storage, processing, bandwidth, and active user accounts). Resource usage can be monitored, controlled, and reported, providing transparency for both the provider and consumer of the utilized service


#### Service Models

- **Software as a Service (SaaS)**. The capability provided to the consumer is to use the provider’s applications running on a cloud infrastructure2. The applications are accessible from various client devices through either a thin client interface, such as a web browser (e.g., web-based email), or a program interface. The consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, storage, or even individual application capabilities, with the possible exception of limited user-specific application configuration settings.
- **Platform as a Service (PaaS)**. The capability provided to the consumer is to deploy onto the cloud infrastructure consumer-created or acquired applications created using programming languages, libraries, services, and tools supported by the provider.3 The consumer does not manage or control the underlying cloud infrastructure including network, servers, operating systems, or storage, but has control over the deployed applications and possibly configuration settings for the application-hosting environment.

- **Infrastructure as a Service (IaaS)**. The capability provided to the consumer is to provision processing, storage, networks, and other fundamental computing resources where the consumer is able to deploy and run arbitrary software, which can include operating systems and applications. The consumer does not manage or control the underlying cloud infrastructure but has control over operating systems, storage, and deployed applications; and possibly limited control of select networking components (e.g., host firewalls).

#### Deployment Models

- **Private cloud**. The cloud infrastructure is provisioned for exclusive use by a single organization  comprising multiple consumers (e.g., business units). It may be owned, managed, and operated by the organization, a third party, or some combination of them, and it may exist
on or off premises. 

- **Community cloud**. The cloud infrastructure is provisioned for exclusive use by a specific community of consumers from organizations that have shared concerns (e.g., mission, security requirements, policy, and compliance considerations). It may be owned, managed, and operated by one or more of the organizations in the community, a third party, or some combination of them, and it may exist on or off premises.

- **Public cloud**. The cloud infrastructure is provisioned for open use by the general public. It may be owned, managed, and operated by a business, academic, or government organization, or some combination of them. It exists on the premises of the cloud provider.

- **Hybrid cloud**. The cloud infrastructure is a composition of two or more distinct cloud infrastructures (private, community, or public) that remain unique entities, but are bound together by standardized or proprietary technology that enables data and application
portability (e.g., cloud bursting for load balancing between clouds)


### Challenges and benefits for Cloud Computing


- References [1](https://nvlpubs.nist.gov/nistpubs/legacy/sp/nistspecialpublication800-145.pdf)


## Brief overview of Telco Cloud

### Telco Cloud Overview:
- Telco cloud empowers service providers to operate networks like a cloud.
- Facilitates agile and efficient creation and deployment of services.

### Architecture:
- Telco cloud architectures seamlessly connect public, private, and edge cloud infrastructure.
- Enables DevOps-managed environments for digital service providers.

### Foundation:
- Built on a network functions virtualization (NFV)–enabled platform.
- This platform, also known as telco cloud infrastructure, serves as the foundation.

### Abstraction Layer:
- Creates an abstraction layer for the telco network.
- Incorporates modern hardware resources.

### Network Functions:
- Supports modular cloud-native network functions (CNFs).
- Also accommodates virtualized network functions (VNFs).

### Software & Automation:
- Establishes a software foundation for creating and delivering next-generation services.
- This foundation requires automated orchestration to effectively manage CNFs and VNFs across all software-defined resources.
- Eliminates error-prone human activities, such as service provisioning.
- Reduces complexity and optimizes overall resource utilization.

### Orchestration & Intelligence

- Telco cloud automation oversees service life cycles across various clouds:
- Network cloud
- Hybrid cloud
- Edge cloud
- IT cloud (Software-Defined Data Center, or SDDC)
- Ensures integrated and consistent management.
- The last layer of a telco cloud is the intelligence layer.
- Focuses on service assurance and root-cause analysis.

### Quality of Service (QoS) Management:
- Telco cloud automation is responsible for instantiating and delivering services.
- It seamlessly meets different Quality of Service (QoS) requirements across network resources.
 


## Linux and Open source

### Introduction:
Linux, an open-source operating system kernel, has become synonymous with the broader ethos of open source software development. Developed by Linus Torvalds in 1991, Linux represents a collaborative and community-driven approach to software creation. This operating system has not only revolutionized the landscape of computing but has also become a symbol of the open-source movement.

### Key Opensource events

| Year | Achievements | Remarks |
|---|---|---|
| 1960s | Development of the Multics operating system | Multics laid the foundation for many of the concepts used in Unix, including the hierarchical file system, process forking, and inter-process communication. |
| 1970s | Creation of Unix by Ken Thompson and Dennis Ritchie at Bell Labs | Unix became the dominant operating system for workstations and servers in the 1980s and 1990s. |
| 1983 | Release of the GNU General Public License (GPL) by Richard Stallman | The GPL is a widely used open-source software license that requires all derivatives of the software to be released under the same license. |
| 1991 | Release of Linux by Linus Torvalds | Linux is a free and open-source operating system that has become the dominant operating system for web servers and embedded devices. |
| 1998 | Apache Software Foundation | The Apache Software Foundation is a non-profit organization that operates the development and maintenance of the open-source web server software Apache HTTP Server. |
| 2004 | Mozilla Foundation | The Mozilla Foundation is a non-profit organization that operates the development and maintenance of the open-source web browser Mozilla Firefox. |
| 2005 | Linux Foundation | The Linux Foundation is a non-profit organization that promotes and develops the Linux operating system. |
| 2008 | Open Source Initiative (OSI) | The Open Source Initiative is a non-profit organization that promotes and develops open-source software. |
| 2012 | Release of the first Android smartphone | Android is a free and open-source mobile operating system that is based on the Linux kernel. |
| 2014 | Release of the first smartwatch with Google Wear | Google Wear is a free and open-source operating system for smartwatches that is based on the Linux kernel. |
| 2016 | Release of the first Chromebook with Google Chrome OS | Chrome OS is a free and open-source operating system for Chromebooks that is based on the Linux kernel. |
| 2018 | Release of the first Raspberry Pi with a Linux operating system | The Raspberry Pi is a small, inexpensive computer that has been very popular for education and hobbyists. |

### Open Source Philosophy
At its core, the open-source philosophy emphasizes transparency, collaboration, and the free exchange of ideas. Unlike proprietary software, open-source software allows users to view, modify, and distribute the source code. This not only promotes innovation but also empowers a global community of developers to contribute to the improvement of software, fostering a culture of shared knowledge.

### Linux
Linux is an open-source operating system kernel that has played a transformative role in the world of computing. Originally created by Linus Torvalds in 1991, Linux has grown into a versatile and powerful platform known for its stability, security, and customization options. It is a Unix-like operating system, and its source code is freely available to the public, adhering to the principles of the open-source software development model.

The impact of Linux extends across various domains, from servers and embedded systems to desktop environments. Renowned for its stability, Linux is a preferred choice for mission-critical systems and servers. Its open nature allows users to view, modify, and distribute the source code, fostering a collaborative community of developers and contributors worldwide.

Linux has also influenced other projects and initiatives. The Linux Foundation, established in 2005, is a non-profit organization that promotes the development of the Linux operating system and provides support for open-source projects. Linux's kernel serves as the foundation for Android, the widely used mobile operating system, showcasing its adaptability.

For more detailed information, you can refer to the Wikipedia page on Linux, where you will find comprehensive insights into its history, development, features, and the broader ecosystem it has influenced.

### Key Features of Linux:

- Stability and Reliability: Linux is renowned for its stability, making it a preferred choice for servers and critical systems.
- Security: Open source allows for constant scrutiny, making Linux a secure platform with rapid responses to vulnerabilities.
- Customizability: Users can tailor Linux distributions to suit specific needs, from lightweight systems to robust server configurations.

### Community Collaboration:
The collaborative nature of open source is exemplified in the vast community of developers, contributors, and users working together to enhance Linux. Online forums, mailing lists, and collaborative platforms foster a sense of shared responsibility, where feedback and improvements come from a diverse pool of individuals.

### Impact on Computing:
Linux has permeated various domains, from servers and embedded systems to desktop environments. Android, a widely used mobile operating system, is built on the Linux kernel. Additionally, Linux powers a significant portion of internet servers, contributing to the robustness of the World Wide Web.



## Open source in Telecom

The telecommunications industry has witnessed a remarkable transformation in recent years, driven by the adoption of open-source technologies. This shift has brought about significant benefits, including increased flexibility, reduced costs, and enhanced interoperability. Open-source software has empowered telecom operators to break free from vendor lock-in and embrace a more collaborative approach to innovation.

### Key Open Source Projects in Telecom

Several open-source projects have played a pivotal role in shaping the telecom landscape. These projects have fostered a vibrant community of developers and contributors, leading to the development of robust and scalable solutions. Here are a few notable examples:

- **OPNFV (Open Platform for NFV)**: OPNFV is an open-source platform that facilitates the deployment and management of Network Functions Virtualization (NFV) solutions. It provides a standardized framework for orchestrating and managing virtual network functions (VNFs) and NFV infrastructure.

- **ONAP (Open Network Automation Platform)**: ONAP is an open-source platform that automates the lifecycle management of telecom networks. It covers a wide range of network functions, including service provisioning, configuration, and performance monitoring.

- **FRRouting (FRR)**: FRRouting is an open-source routing protocol suite that provides a comprehensive set of routing protocols for various network environments. It supports a wide range of routing technologies, including BGP, OSPF, and ISIS.

- **OpenDaylight (ODL)**: OpenDaylight is an open-source SDN (Software-Defined Networking) controller that provides a platform for managing network resources through software. It enables network operators to centrally manage and control their network infrastructure, improving agility and efficiency.

- **OpenRAN (Open Radio Access Network)**: OpenRAN is an open-source initiative that promotes the development and deployment of interoperable and open-source software for radio access networks (RANs). It aims to reduce vendor lock-in and foster innovation in the RAN segment.

### Impact of Open Source on Telecom

The adoption of open-source technologies has had a profound impact on the telecom industry. Here are some of the key benefits:

- Increased Flexibility and Agility: Open-source software allows telecom operators to customize and adapt solutions to their specific needs, without being constrained by vendor limitations. This flexibility enables them to respond quickly to changing market demands and technological advancements.
- Reduced Costs: Open-source software often comes with lower licensing fees or is entirely free to use, significantly reducing the capital expenditure (CAPEX) associated with software procurement. This cost-effectiveness is particularly important for telecom operators facing increasing cost pressures.
- Enhanced Interoperability: Open-source software promotes interoperability among different vendors and technologies, breaking down barriers to communication and enabling seamless integration of network components. This interoperability is crucial for building next-generation networks that can support diverse applications and services.
- Fostering Innovation: Open-source development fosters a collaborative environment where developers from different organizations can contribute to the improvement of software solutions. This collective effort accelerates innovation and leads to the creation of more advanced and feature-rich solutions.
- Strengthening Security: Open-source software undergoes rigorous community scrutiny, which helps identify and fix vulnerabilities quickly. This transparency enhances the overall security of open-source software solutions.


## Using Git and Github

## Setting up your dev environment using a VM


The purpose of this VM will be to serve as your development machine which you can use to work on your projects. As this is consistent for everyone in the project, we are going to use the same version of operating system as a virtual machine.



1. Download and install softwares using Chocolatey
2. Download and install VirtualBox
3. Download the [Ubuntu ISO Image](https://ubuntu.com/download/desktop/thank-you?version=22.04.3&architecture=amd64)
4. Install the virtual machine using VirtualBox
5. Start the virtual machine
6. Login to the VM

