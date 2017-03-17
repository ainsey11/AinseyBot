#!/usr/bin/python3
import socket
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read ('config/config.ini')

Server = config.get("BotConnectionParams","Server")
Port = config.get("BotConnectionParams","Port")
Nick = config.get("BotConnectionParams","Nick")
AdminName = config.get("BotConnectionParams","AdminName")
ExitMessage = config.get("BotConnectionParams","ExitMessage")
