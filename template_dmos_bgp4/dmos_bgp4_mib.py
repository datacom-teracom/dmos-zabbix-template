#!/usr/bin/env python3

''' Script to discovery DMOS-BGP-4-MIB objects in Zabbix '''

from subprocess import Popen, DEVNULL, PIPE
from json import dumps
from sys import argv
from time import sleep
from re import search
from ipaddress import ip_address


def convert_ipv6_snmp_hexa_decimal(ipv6_address):
    ''' Function to convert IPv6 returned from SNMP in Hexadecimal to Decimal '''

    # split ipv6 by colon character
    aux = ipv6_address.split(':')

    # convert to hexadecimal
    address = []
    for hexa in aux:
        address.append(int(hexa, 16))

    # adding dot separator
    ipv6 = ''
    index = 0
    for i in address:
        if index == 0:
            ipv6 = str(ipv6) + str(i)
        else:
            ipv6 = str(ipv6) + '.' + str(i)
        index += 1

    return ipv6


def convert_to_compress_ipv6(ipv6_address):
    ''' Function to convert IPv6 returned from SNMP in Hexadecimal to compress format '''

    # split ipv6 by colon character
    aux = ipv6_address.split(':')

    # grouping address
    address = ''
    for hexa in aux:
        address = str(address) + str(hexa)

    # adding colon in for each four hexadecimal characters from IPv6
    ipv6 = ''
    index = 0
    for i in address:
        if index == 4:
            ipv6 = str(ipv6) + ':' + str(i)
            index = 0
        else:
            ipv6 = str(ipv6) + str(i)
        index += 1

    # convert IPv6 to compress format
    ipv6 = str(ip_address(ipv6))

    return ipv6

def snmp_discovery_info(host, community, oid):
    ''' Return SNMP discovery info '''

    process = Popen(["snmpwalk", "-v", "2c", "-c", community, host, oid],
                    stdout=PIPE, stderr=DEVNULL, universal_newlines=True)

    snmp_info = []
    while True:
        sleep(1)
        return_code = process.poll()
        if return_code is not None:
            for output in process.stdout.readlines():
                snmp_info.append(output.strip())
            break
    return snmp_info


def main():
    ''' Main function '''

    host = argv[1]
    community = argv[2]
    oid = 'DMOS-BGP4-MIB::bgpPrefixCountersInPrefixes'

    snmp_info = snmp_discovery_info(host, community, oid)

    number_peers = len(snmp_info)
    jason_data = []
    for i in range(number_peers):
        regex = r'\.(ipv4|ipv6)\."(.*)".(.*)\.(unicast|mplsVpn)'
        output_regex = search(regex, snmp_info[i])

        if output_regex.group(1) == 'ipv6':
            ipv6_address_snmp = convert_ipv6_snmp_hexa_decimal(output_regex.group(2))
            ipv6_address = convert_to_compress_ipv6(output_regex.group(2))

            jason_data.append(
                {'{#IP_ADDRESS_TYPE}': output_regex.group(1),
                 '{#IP_ADDRESS_SIZE}': '16',
                 '{#IP_ADDRESS}': ipv6_address,
                 '{#IP_ADDRESS_SNMP}': ipv6_address_snmp,
                 '{#AFI}': output_regex.group(3),
                 '{#SAFI}': output_regex.group(4)})
        else:
            jason_data.append(
                {'{#IP_ADDRESS_TYPE}': output_regex.group(1),
                 '{#IP_ADDRESS_SIZE}': '4',
                 '{#IP_ADDRESS}': output_regex.group(2),
                 '{#IP_ADDRESS_SNMP}': output_regex.group(2),
                 '{#AFI}': output_regex.group(3),
                 '{#SAFI}': output_regex.group(4)})

    print(dumps({"data": jason_data}, indent=4))


main()
