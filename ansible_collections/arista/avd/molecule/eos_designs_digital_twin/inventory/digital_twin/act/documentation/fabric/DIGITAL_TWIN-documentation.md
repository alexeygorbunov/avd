# DIGITAL_TWIN

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| DIGITAL_TWIN | l3leaf | dc1-leaf1a | 172.16.1.101/24 | veos | Provisioned | - |
| DIGITAL_TWIN | l3leaf | dc1-leaf1b | 172.16.1.102/24 | veos | Provisioned | - |
| DIGITAL_TWIN | l2leaf | dc1-leaf1c | 172.16.1.151/24 | cloudeos | Provisioned | - |
| DIGITAL_TWIN | spine | dc1-spine1 | 172.16.1.11/24 | veos | Provisioned | - |
| DIGITAL_TWIN | spine | dc1-spine2 | 172.16.1.12/24 | veos | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | dc1-leaf1a | Ethernet1 | spine | dc1-spine1 | Ethernet1 |
| l3leaf | dc1-leaf1a | Ethernet2 | spine | dc1-spine2 | Ethernet1 |
| l3leaf | dc1-leaf1a | Ethernet8 | l2leaf | dc1-leaf1c | Ethernet1 |
| l3leaf | dc1-leaf1a | Ethernet9 | mlag_peer | dc1-leaf1b | Ethernet9 |
| l3leaf | dc1-leaf1a | Ethernet10 | mlag_peer | dc1-leaf1b | Ethernet10 |
| l3leaf | dc1-leaf1b | Ethernet1 | spine | dc1-spine1 | Ethernet2 |
| l3leaf | dc1-leaf1b | Ethernet2 | spine | dc1-spine2 | Ethernet2 |
| l3leaf | dc1-leaf1b | Ethernet8 | l2leaf | dc1-leaf1c | Ethernet2 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 10.255.255.0/26 | 64 | 8 | 12.5 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| dc1-leaf1a | Ethernet1 | 10.255.255.1/31 | dc1-spine1 | Ethernet1 | 10.255.255.0/31 |
| dc1-leaf1a | Ethernet2 | 10.255.255.3/31 | dc1-spine2 | Ethernet1 | 10.255.255.2/31 |
| dc1-leaf1b | Ethernet1 | 10.255.255.5/31 | dc1-spine1 | Ethernet2 | 10.255.255.4/31 |
| dc1-leaf1b | Ethernet2 | 10.255.255.7/31 | dc1-spine2 | Ethernet2 | 10.255.255.6/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 10.255.0.0/27 | 32 | 4 | 12.5 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| DIGITAL_TWIN | dc1-leaf1a | 10.255.0.3/32 |
| DIGITAL_TWIN | dc1-leaf1b | 10.255.0.4/32 |
| DIGITAL_TWIN | dc1-spine1 | 10.255.0.1/32 |
| DIGITAL_TWIN | dc1-spine2 | 10.255.0.2/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 10.255.1.0/27 | 32 | 2 | 6.25 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| DIGITAL_TWIN | dc1-leaf1a | 10.255.1.3/32 |
| DIGITAL_TWIN | dc1-leaf1b | 10.255.1.3/32 |
