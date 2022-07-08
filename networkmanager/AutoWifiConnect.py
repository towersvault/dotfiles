#!/usr/bin/python3

# This script automatically switches the WiFi connection to the AP with
# the strongest signal (chosen from APs known to NetworkManager).
# Uses 'nmcli', see https://wiki.archlinux.org/title/NetworkManager
# Thank you u/sqrt7744, https://www.reddit.com/r/linux/comments/bbzm9t/automatically_switch_to_the_strongest_wifi_signal/

import subprocess

# Set the switching threshold. Signal strength returned by NetworkManager
# is on a scale of 0 to 100.
MIN_SIGNAL_STRENGTH_DIFF = 12  # Minimum signal difference between APs required for switching

active_connection = ''
potential_access_points = list()

# Returns the signal strength from a scan result
def signal_strength(available_network):
    return available_network.split(':')[1]  # Signal strength in 2nd column

# Get a list of networks in range
networks_scan = subprocess.run(
    [
        '/usr/bin/nmcli',
        '-t',  # Tabular format, with ':' as separator
        '-f',  # Filter columns
        'ssid,signal,rate,in-use',
        'dev',
        'wifi',
        'list'
    ],
    stdout=subprocess.PIPE,
    universal_newlines=True
)

# Store scan results in a list
scan_results = networks_scan.stdout.splitlines()

# Get a list of known networks to this system
networks_known = subprocess.run(
    [
        '/usr/bin/nmcli',
        '-t',
        '-f',
        'name',
        'connection',
        'show'
    ],
    stdout=subprocess.PIPE,
    universal_newlines=True
)

# Store SSIDs of known networks
known_results = networks_known.stdout.splitlines()

# Compile list of common SSIDs between scan and known results,
# in addition to flagging if system is connected or not
for network in scan_results:
    # print('Scanned network: %s' % network)
    network_info = network.split(':')
    ssid = network_info[0]
    connected = False

    if network_info[3] == '*':  # 4th column stores '*' if connected to it
        connected = True
        active_connection = network
    
    if ssid in known_results:
        if connected == False:
            potential_access_points.append(network)

# Sort the list by weakest to strongest signals (if not empty)
if len(potential_access_points) >= 1:
    print('Multiple known networks detected..')

    potential_access_points.sort(key=signal_strength)

    # print(potential_access_points)

    # Switch to network with best signal strength
    strongest_available_ap = str(potential_access_points[0]).split(':')
    
    strongest_ssid = strongest_available_ap[0]
    strongest_signal = strongest_available_ap[1]

    print('Strongest known network: %s (%s)' % (strongest_ssid, strongest_signal))

    # If there is an active connection, get the signal strength, else 0
    if active_connection:
        current_signal = active_connection.split(':')[1]

        print('Currently connected network: %s (%s)' % (active_connection.split(':')[0], current_signal))
    else:
        current_signal = 0
        print('Not connected to a network')
    
    # If there's a stronger AP, switch to it
    if int(strongest_signal) > int(current_signal) + MIN_SIGNAL_STRENGTH_DIFF:
        print('Stronger network found, connecting to it..')

        subprocess.run(
            [
                '/usr/bin/nmcli',
                'device',
                'wifi',
                'connect',
                strongest_ssid
            ]
        )
    else:
        print('Already connected to the strongest network!')
