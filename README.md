# dmos-zabbix-template

Zabbix templates for DmOS Datacom network equipments

## Template DmOS

Used for General DmOS MIBs (SNMP System, CPU, Memory, FAN and Temperature).

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

## Template Datacom IF-MIB

Used for all Datacom platforms and other vendors.

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

##### Zabbix Discovery Macros:

- {#IFOPERSTATUS} - Interface Operational Status
- {#IFADMINSTATUS} - Interface Administrative Status
- {#IFALIAS} - Interface description
- {#IFDESCR} - Interface name

To discovery process works it is necessary the MIB file IF-MIB.mib. Please copy the MIB file from
the equipment using the DmOS command named "copy mibs" and upload for your Zabbix server.

## Template DmOS-BGP4-MIB

- Auto-discovering
- Supports IPv4 and IPv6 BGP sessions
- Supports IPv4 Unicast, IPv6 Unicast and MPLS VPN objects
- Supports SNMPv1 and SNMPv2c
- Supports BGP4-MIB standard MIB and DmOS-BGP4-MIB proprietary MIB

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

##### Zabbix Discovery Script Macros:

- {#IP_ADDRESS_TYPE} - IP address type (e.g., IPv4, IPv6)
- {#IP_ADDRESS_SIZE} - IP address size (e.g., 4 for IPv4, 16 for IPv6)
- {#IP_ADDRESS} - IP address in friendly format (e.g., 1.1.1.1 for IPv4 address or 2001:2:a80:218::2
  for IPv6 address)
- {#IP_ADDRESS_SNMP} - IP address used by SNMP to get OIDs
(e.g., 1.1.1.1 for IPv4 or 32.1.0.2.10.128.2.24.0.0.0.0.0.0.0.2 for 2001:2:a80:218::2 IPv6 address)
- {#AFI} - (AFI) Address Family Identifiers (e.g., IPv4, IPv6)
- {#SAFI} - (SAFI) Subsequent Address Family Identifiers (e.g., unicast , mplsVpn)

To discovery process works it is necessary upload the script file "dmos_bgp4_mib.py" to your Zabbix
server in external scripts directory, also it is necessary the MIB file DMOS-BGP4-MIB.mib. Please
copy the MIB file from the equipment using the DmOS command named "copy mibs" and upload for your
Zabbix server.

## Template DmOS-EAPS-MIB

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

##### Zabbix Discovery Macros:

- {#EAPS_ID} - EAPS Domain ID
- {#EAPS_NAME} - EAPS Domain Name

## Template DmOS-ERPS-MIB

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

##### Zabbix Discovery Macros:

- {#ERPS_RING_ID} - ERPS Ring ID
