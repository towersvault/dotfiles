#!/usr/bin/env bash

echo Sleeping for 5 seconds before doing a WiFi scan..
sleep 5s
echo Slept, performing WiFi scan..
python3 /home/clifford/.config/networkmanager/AutoWifiConnect.py
echo WiFi scan complete