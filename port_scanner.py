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

def connection_scan(target_ip, target_port):
    ###Attempt to create a socket connection with a given target ip
    #### if successful, the port is open. if not the port is closed
    try:
        connect_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connect_socket.connect((target_ip, target_port))
        connect_socket.send(b'Banner_query\r\n')
        print("[+]{}/TCP open ".format(target_port))
    except OSError:
        print("[-]{}/TCP closed".format(target_port))
    finally:
        connect_socket.close() # Ensures the connection is closed

def Port_Scan(t_ip, t_port):
    """"
    Scan the indicated ports for status.
    First, it attempts to resolve the IP address of a provided hostname, then enumerates through the ports.
    """
    try:
        target_ip  = socket.gethostbyname(t_ip)
        print("[*] Scan Results for: {}".format(t_ip))
        connection_scan(t_ip, int(t_port))
    except OSError:
        print("[*] Cannot resove {}: Unkown Host".format(t_ip))
        return # Exits scan if tatget ip is not resolved
def scan_arg():
        """"
         to Allow us to add some arguments for our scan

        """
        arg = argparse.ArgumentParser(description="TCp port Scanner. Accepts a hostname/IP addess and list of ports to "
                                                  "scan. Attempts to identify the service running on a port.")
        arg.add_argument("-t", "--host", nargs="?", help="Host IP address ")
        arg.add_argument("-p", "--ports", nargs="?",help="comma separated port list, such as '20,21,22'")
        var_args = vars(arg.parse_args()) # Covnert argument into a dictionary
        return var_args
if __name__ == "__main__" :
    try:
        user_args = scan_arg()
        host = user_args["host"]
        port_list = user_args["ports"].split(",") # Make a list from port numbers
        for port in port_list:
            Port_Scan(host, port)
    except AttributeError:
        print("Error. Please provide the command-line arguments before running.")




