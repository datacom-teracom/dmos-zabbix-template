#!/usr/bin/env python3

""" Script to discovery DmOS Transceivers objects in Zabbix """

from subprocess import run
from json import dumps
from sys import argv
from re import search


def snmp_discovery_info(host, community, oid):
    """ Return SNMP discovery info """

    cmd = f"snmpbulkwalk -v 2c -c {community} {host} {oid}"
    process = run(cmd, shell=True, capture_output=True, text=True, timeout=30)

    snmp_info = []
    while True:
        return_code = process.returncode
        if return_code is not None:
            for output in process.stdout.rstrip().split('\n'):
                snmp_info.append(output.strip())
            break

    return snmp_info

def snmp_get_info(host, community, oid, index):
    """ Return SNMP get info """

    cmd = f"snmpget -v 2c -c {community} {host} {oid}.{index}"
    process = run(cmd, shell=True, capture_output=True, text=True, timeout=30)

    while True:
        return_code = process.returncode
        if return_code is not None:
            for output in process.stdout.rstrip().split('\n'):
                regex = r'%s\.([0-9]{1,30})\s=\s[a-zA-Z0-9]{1,50}:(\s(.*))?$' % oid
                output_regex = search(regex, output)

                if output_regex.group(3) is None:
                    snmp_info = ""
                else:
                    snmp_info = output_regex.group(3)
            break

    return snmp_info

def main():
    """ Main function """

    host = argv[1]
    community = argv[2]

    oid = 'DMOS-TRANSCEIVER-MIB::laneCount'
    snmp_info = snmp_discovery_info(host, community, oid)

    number_snmp_info = len(snmp_info)
    json_data = []

    if number_snmp_info == 1:
        print('The equipment does not return SNMP objects')
        exit(0)

    for i in range(number_snmp_info):
        object = {}

        regex = r'%s\.([0-9]{1,10})\s.*\s(.*)$' % oid
        output_regex = search(regex, snmp_info[i])

        object['{#SNMPINDEX}'] = output_regex.group(1)

        snmp_get_oid = "DMOS-INVENTORY-MIB::transceiverInventoryInfoVendorSn"
        snmp_get_ret = snmp_get_info(host, community, snmp_get_oid, output_regex.group(1))
        object['{#TCN_SN}'] = snmp_get_ret

        snmp_get_oid = "IF-MIB::ifAlias"
        snmp_get_ret = snmp_get_info(host, community, snmp_get_oid, output_regex.group(1))
        object['{#IFALIAS}'] = snmp_get_ret

        snmp_get_oid = "IF-MIB::ifDescr"
        snmp_get_ret = snmp_get_info(host, community, snmp_get_oid, output_regex.group(1))
        object['{#IFDESCR}'] = snmp_get_ret

        json_data.append(object)

    print(dumps({"data": json_data}, indent=4))


main()
