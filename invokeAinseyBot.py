#!/usr/bin/python3
import socket
import sys
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read ('config/config.ini')

Server = config.get("BotConnectionParams","Server")
Channel = config.get("BotConnectionParams","Channel")
Nick = config.get("BotConnectionParams","Nick")
AdminName = config.get("BotConnectionParams","AdminName")
ExitMessage = config.get("BotConnectionParams","ExitMessage")
Debug = True #config.get("BotDebugParams","EnableDebug")
DebugChannel = config.get("BotDebugParams","DebugChannel")
if Debug == True:
    ConnectChan = DebugChannel
elif Debug == False:
   ConnectChan = Channel

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.recv (4096)
irc.connect((Server,6667))
irc.send("USER" + Nick + Nick + Nick + ":AinseyBot\n")
irc.send("NICK" + Nick +"\n")
irc.send("JOIN" + ConnectChan +"\n")
irc.send("PRIVMSG" + ConnectChan + ":Hello! I am a bot! \r\n")

