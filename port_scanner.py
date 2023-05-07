#!/bin/python
"""
Python Port scanner_thread.py
Purpose: Python based TCP Port scanner
Auther: Basset benghina
date: 4/21/2023
version 0.1
initial build
"""


import socket
import argparse
import threading
def connection_scan(IP, port):
    try:
        connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connection.connect((IP, port))
        """" here what we need to do to request for banner or to add an option for banner grabbing to to add 
                    only one line which is connection_scann.send(b'Banner_query\r\n')
               """
        connection.send(b'Banner_query\r\n')
        results = connection.recv(100)
        ##and then we are going to capture the result or the banner response let's say in a variable called result
        print("[*] the port {} is open".format(port))
        print("[-] {}".format(results))
        return True

    except OSError:
        print("[*\] the port {} is closed".format(port))
        return False

    finally:
        connection.close()
def port_scanning(target, port_num):
    try:
        target_ip = socket.gethostbyname(target)
        print("[+] Scan Result for {}".format(target),"on port {}: ".format(port_num))
        connection_scan(target_ip, int(port_num))

    except OSError:
        print("[-] Cannot Resolve the host {}".format(target))
        return # Exit  Scan if the target is not resolved


def connection_argument():
    arguments = argparse.ArgumentParser(description="these are the options we cann use alongside with this program")
    arguments.add_argument("-t", "--host", nargs="?", help="triggers the host value")
    arguments.add_argument("-p", "--ports", nargs="?", help="triggers the port value")
    arguments.add_argument("-a", "--all", action="store_true" , help="an option to scann all the 65000 ports ")
    argument_vars = vars(arguments.parse_args()) # Convert argument namespace to dictionary

    return argument_vars


if __name__ == '__main__':
    try:
       user_args = connection_argument()
       host = user_args["host"]
       if user_args["all"]:
           port_list = range(1, 65000)
       else:
           port_list = user_args["ports"].split(",")# Make a list from port numbers
       for port in port_list:
           port_scanning(host, int(port))
    except AttributeError:
        print("Error. Please provide the command-line arguments before running.")
