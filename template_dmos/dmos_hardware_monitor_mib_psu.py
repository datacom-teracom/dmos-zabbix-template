#!/usr/bin/env python3

""" Script to discovery DmOS PSU objects in Zabbix """

from subprocess import run
from json import dumps
from sys import argv
from re import search, I


def snmp_discovery_info(host, community, oid):
    """ Return SNMP discovery info """

    cmd = f"snmpbulkwalk -v 2c -c {community} {host} {oid}"
    process = run(cmd, shell=True, capture_output=True, text=True, timeout=30)

    snmp_info = []
    snmp_error = ''
    while True:
        return_code = process.returncode
        if return_code is not None:
            for output in process.stdout.rstrip().split('\n'):
                if search(r'no such', output, I):
                    snmp_error = output.strip()
                    break
                else:
                    snmp_error = process.stderr.strip()
                snmp_info.append(output.strip())
            break

    return snmp_info, snmp_error

def convert_snmp_value_string_to_decimal(snmp_value):
    """ Return object size and dotted decimal for use in SNMP get """

    snmp_value_dec = ''

    snmp_value_size = len(snmp_value)

    for index in range(snmp_value_size):
        char_decimal = int(''.join(str(ord(snmp_value[index]))))

        if index == snmp_value_size-1:
            snmp_value_dec += str(char_decimal)
        else:
            snmp_value_dec += str(char_decimal) + '.'

    return snmp_value_size, snmp_value_dec

def main():
    """ Main function """

    host = argv[1]
    community = argv[2]

    oid = 'DMOS-HW-MONITOR-MIB::psuStatus'
    snmp_info = snmp_discovery_info(host, community, oid)

    number_snmp_info = len(snmp_info[0])
    json_data = []

    ret_error = snmp_info[1]
    snmp_info = snmp_info[0]

    if ret_error != '':
        print(ret_error)
        exit(1)

    for i in range(number_snmp_info):
        object = {}

        regex = r'%s\.\'\.([a-zA-Z0-9\/]{1,50})\'\s.*\s(.*)$' % oid
        output_regex = search(regex, snmp_info[i])

        object['{#PSU_SLOT_NAME}'] = output_regex.group(1)

        snmp_value_decimal = convert_snmp_value_string_to_decimal(output_regex.group(1))
        object['{#PSU_SLOT_NAME_LEN}'] = snmp_value_decimal[0]
        object['{#PSU_SLOT_NAME_DEC}'] = snmp_value_decimal[1]

        json_data.append(object)

    print(dumps({"data": json_data}, indent=4))


main()
