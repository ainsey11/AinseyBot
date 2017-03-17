#!/usr/bin/python3
import socket
import sys
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read ('config/config.ini')

Server = config.get("BotConnectionParams","Server")
Port = config.get("BotConnectionParams","Port")
Channel = config.get("BotConnectionParams","Channel")
Nick = config.get("BotConnectionParams","Nick")
AdminName = config.get("BotConnectionParams","AdminName")
ExitMessage = config.get("BotConnectionParams","ExitMessage")

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((server,port))
irc.send("USER "+Nick+" "+Nick+" "+Nick+" :AinseyBot\n")
irc.send("NICK "+Nick+"\n")
irc.send("JOIN "+Channel+"\n")

