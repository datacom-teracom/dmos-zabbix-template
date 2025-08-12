# dmos-zabbix-template

Zabbix templates for DmOS Datacom network equipments.

These templates are tested in Zabbix 7.2.0 version and are supported in newer versions.

To discovery process works it is necessary the MIB files in Zabbix. Please copy the MIB files
from the equipment using the DmOS command named "copy mibs" and upload for your Zabbix server.

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
- {#IFPHYSADDRESS} - Interface physical address

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
server in external scripts directory located on Ubuntu at "/usr/lib/zabbix/externalscripts/", also
it is necessary the MIB file DMOS-BGP4-MIB.mib. Please copy the MIB file from the equipment using
the DmOS command named "copy mibs" and upload for your Zabbix server.

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

## Template DmOS GPON

Used for GPON-ONU-IF-MIB - (ONU status, ONU statistics, ONU power, ONU uptime ).

By default the template has ONU statistics disabled. If you need to monitor, enable on demand.

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

##### Zabbix Discovery Macros:

- {#ONUIFDESCR} -ONU description
- {#ONUIFNAME} - ONU name

## Template Grafana

DATACOM provides a Grafana JSON template where it is possible to validate some information:
 - Sum of ONUs per PON port
 - Sum of all ONUs on the Chassis
 - Sum of all DOWN and UP ONUs per PON port and Chassis
 - CPU; Memory; GPON interfaces
 - Ethernet interface traffic

 For more details visit the link:
 https://www.datacom.com.br/pt/blog/98/monitoramento-dos-equipamentos-dmos-via-zabbix-e-grafana

## Template DmOS GPON COUNTING

Used for DATACOM DMOS-ONU-COUNTING-MIB for ONUs counting by ponlink and total.

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

##### Zabbix Discovery Macros:

- {#PONIFDESCR} -PON description

## Template DmOS-TRANSCEIVERS-MIB

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

##### Zabbix Discovery Script Macros:

- {#SNMPINDEX} Interface index

- {#TCN_SN} Transceiver serial number

- {#IFALIAS} This object is an 'alias' name for the interface as specified by a network manager,
and provides a non-volatile 'handle' for the interface.

- {#IFDESCR} A textual string containing information about the interface. This string should
include the name of the manufacturer, the product name and the version of the interface
hardware/software.

## Template ICMP Probe

##### Zabbix Macros:

- {$SNMP_COMMUNITY} - SNMP community

##### Zabbix Discovery Macros:

- {#ICMP_PROBE_TARGET} This object indicates the type of address stored in the corresponding
pingResultsIpTargetAddress object.

- {#ICMP_PROBE_RESULTS_SENT} The value of this object reflects the number of probes sent for the
corresponding pingCtlEntry and pingResultsEntry.

- {#ICMP_PROBE_LAST_GOOD} Date and time when the last response was received for a probe.
