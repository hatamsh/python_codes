#!/bin/python

"""
Python script for automating backups of Cisco devices.
    1. Scripts connect to a device over SSH.
    2. Disables paging.
    3. Executes show run command.
    4. Saves the output to a file.
Successfully tested on IOS, IOS-XE, IOS-XR, and ASA software.
"""

# Importing paramiko and time modules
import paramiko
import time

# Username and passwords for a backup user
username = "backup"
password = "backup"

"""
Device IPs are stored in the list.
In future new IP can be added to the list and for loop will grab it.
"""

router_IPs = ["192.168.99.254"]
asa_IPs = ["192.168.99.253"]

# Taking the SSHClient
ssh_conn_paramiko = paramiko.SSHClient()

# Auto accept SSH host keys.
ssh_conn_paramiko.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Used to disable paging
def disable_paging_ios_iosxr_iosxe(command="terminal length 0\n", delay=2):
    cli_interaction.send("\n")
    cli_interaction.send(command)
    time.sleep(delay)


def disable_paging_asa(command="terminal pager 0\n", delay=2):
    cli_interaction.send("\n")
    cli_interaction.send(command)
    time.sleep(delay)


for each in router_IPs:
    backup_file = open("/home/hshukur/Config_Backup/Config_{}.txt".format(each), "w")
    backup_file.write("*" * 32 + "{}".format(each) + "*" * 32 + "\n")
    ssh_conn_paramiko.connect(each, username=username, password=password)
    # ssh_conn_paramiko.connect(each, username=username, password=password, look_for_keys=False, allow_agent=False)
    cli_interaction = ssh_conn_paramiko.invoke_shell()
    disable_paging_ios_iosxr_iosxe()
    time.sleep(3)
    cli_output = cli_interaction.recv(500)
    cli_interaction.send("\nshow run\n")
    time.sleep(30)
    cli_output = cli_interaction.recv(65535)
    backup_file.write(cli_output)
    backup_file.write("\n")
    backup_file.close()
    ssh_conn_paramiko.close()


for each in asa_IPs:
    backup_file = open("/home/hshukur/Config_Backup/Config_{}.txt".format(each), "w")
    backup_file.write("*" * 32 + "{}".format(each) + "*" * 32 + "\n")
    ssh_conn_paramiko.connect(each, username=username, password=password)
    # ssh_conn_paramiko.connect(each, username=username, password=password, look_for_keys=False, allow_agent=False)
    cli_interaction = ssh_conn_paramiko.invoke_shell()
    disable_paging_asa()
    time.sleep(3)
    cli_output = cli_interaction.recv(500)
    cli_interaction.send("\nshow run\n")
    time.sleep(30)
    cli_output = cli_interaction.recv(65535)
    backup_file.write(cli_output)
    backup_file.write("\n")
    backup_file.close()
    ssh_conn_paramiko.close()
