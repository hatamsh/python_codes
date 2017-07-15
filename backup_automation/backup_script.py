# Importing necessary modules
import paramiko
import time
import os

# Username and passwords for backup user
username = "backup"
password = "backup"

# Device IPs are stored in the config files.

# Taking the SSHClient
ssh_conn_paramiko = paramiko.SSHClient()

# Auto accept SSH host keys.
ssh_conn_paramiko.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Folder to save backups
backup_folder = "/home/hshukur/Config_Backup/"

# Used to disable paging on Cisco routers and switches
def disable_paging_ios_iosxr_iosxe_nxos(command="terminal length 0\n", delay=1):
    cli_interaction.send("\n")
    cli_interaction.send(command)
    time.sleep(delay)


# Used to disable paging on Cisco ASA
def disable_paging_asa(command="terminal pager 0\n", delay=1):
    cli_interaction.send("\n")
    cli_interaction.send(command)
    time.sleep(delay)


# Opening file with router IPs
ios_iosxr_iosxe_nxos_IPs = open("/home/hshukur/backup_automation_script/ios_iosxr_iosxe_nxos_IPs.cfg", "r")

# Taking config backups
for each in ios_iosxr_iosxe_nxos_IPs:
    response = os.system("ping -c 1 {}".format(each))
    if response == 0:
        each = each.rstrip()
        backup_file = open(backup_folder + "Cisco/Config_{}.txt".format(each), "w")
        backup_file.write("*" * 32 + "{}".format(each) + "*" * 32 + "\n")
        ssh_conn_paramiko.connect(each, username=username, password=password)
        cli_interaction = ssh_conn_paramiko.invoke_shell()
        disable_paging_ios_iosxr_iosxe_nxos()
        time.sleep(2)
        cli_output = cli_interaction.recv(1000)
        cli_interaction.send("\nshow run\n")
        time.sleep(7)
        cli_output = cli_interaction.recv(655350)
        backup_file.write(cli_output)
        backup_file.write("\n")
        backup_file.close()
        ssh_conn_paramiko.close()
    else:
        continue

# Closing the file with router IPs
ios_iosxr_iosxe_nxos_IPs.close()

# Opening file with ASA IPs
asa_IPs = open("/home/hshukur/backup_automation_script/asa_IPs.cfg", "r")

# Taking config backups
for each in asa_IPs:
    response = os.system("ping -c 1 {}".format(each))
    if response == 0:
        each = each.rstrip()
        backup_file = open(backup_folder + "Cisco/Config_{}.txt".format(each), "w")
        backup_file.write("*" * 32 + "{}".format(each) + "*" * 32 + "\n")
        ssh_conn_paramiko.connect(each, username=username, password=password)
        cli_interaction = ssh_conn_paramiko.invoke_shell()
        disable_paging_asa()
        time.sleep(2)
        cli_output = cli_interaction.recv(1000)
        cli_interaction.send("\nshow run\n")
        time.sleep(7)
        cli_output = cli_interaction.recv(655350)
        backup_file.write(cli_output)
        backup_file.write("\n")
        backup_file.close()
        ssh_conn_paramiko.close()
    else:
        continue

# Closing the file with ASA IPs
asa_IPs.close()

# Opening file with Juniper Junos IPs
juniper_junos_IPs = open("/home/hshukur/backup_automation_script/juniper_junos_IPs.cfg", "r")

# Taking config backups
for each in juniper_junos_IPs:
    response = os.system("ping -c 1 {}".format(each))
    if response == 0:
        each = each.rstrip()
        backup_file = open(backup_folder + "Juniper/Config_{}.txt".format(each), "w")
        backup_file.write("*" * 32 + "{}".format(each) + "*" * 32 + "\n")
        ssh_conn_paramiko.connect(each, username=username, password=password)
        cli_interaction = ssh_conn_paramiko.invoke_shell()
        cli_interaction.send("\nshow configuration | display set | no-more\n")
        time.sleep(7)
        cli_output = cli_interaction.recv(655350)
        backup_file.write(cli_output)
        backup_file.write("\n")
        backup_file.close()
        ssh_conn_paramiko.close()
    else:
        continue

# Closing the file with Juniper Junos IPs
juniper_junos_IPs.close()

# Opening file with Juniper ScreenOS IPs
juniper_screenos_IPs = open("/home/hshukur/backup_automation_script/juniper_screenos_IPs.cfg", "r")

# Taking config backups
for each in juniper_screenos_IPs:
    response = os.system("ping -c 1 {}".format(each))
    if response == 0:
        each = each.rstrip()
        backup_file = open(backup_folder + "Juniper/Config_{}.txt".format(each), "w")
        backup_file.write("*" * 32 + "{}".format(each) + "*" * 32 + "\n")
        ssh_conn_paramiko.connect(each, username=username, password=password)
        cli_interaction = ssh_conn_paramiko.invoke_shell()
        cli_interaction.send("\nset console page 0\n")
        cli_interaction.send("\nget config\n")
        time.sleep(120)
        cli_output = cli_interaction.recv(655350)
        cli_interaction.send("\nset console page 20\n")
        backup_file.write(cli_output)
        backup_file.write("\n")
        backup_file.close()
        ssh_conn_paramiko.close()
    else:
        continue

# Closing the file with Juniper ScreenOS IPs
juniper_screenos_IPs.close()

# Opening file with Huawei IPs
huawei_IPs = open("/home/hshukur/backup_automation_script/huawei_IPs.cfg", "r")

# Taking config backups
for each in huawei_IPs:
    response = os.system("ping -c 1 {}".format(each))
    if response == 0:
        each = each.rstrip()
        backup_file = open(backup_folder + "Huawei/Config_{}.txt".format(each), "w")
        backup_file.write("*" * 32 + "{}".format(each) + "*" * 32 + "\n")
        ssh_conn_paramiko.connect(each, username=username, password=password)
        cli_interaction = ssh_conn_paramiko.invoke_shell()
        cli_interaction.send("system-view\n")
        cli_interaction.send("user-interface vty 0 4\n")
        cli_interaction.send("screen-length 0\n")
        cli_interaction.send("return\n")
        time.sleep(10)
        cli_output = cli_interaction.recv(2000)
        cli_interaction.send("\ndisplay current-configuration\n")
        time.sleep(60)
        cli_output = cli_interaction.recv(655350)
        cli_interaction.send("system-view\n")
        cli_interaction.send("user-interface vty 0 4\n")
        cli_interaction.send("undo screen-length\n")
        cli_interaction.send("return\n")
        time.sleep(10)
        backup_file.write(cli_output)
        backup_file.write("\n")
        backup_file.close()
        ssh_conn_paramiko.close()
    else:
        continue

# Closing the file with Huawei IPs
huawei_IPs.close()
