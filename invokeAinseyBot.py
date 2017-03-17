#!/usr/bin/python3
import socket
import sys
import time
from ConfigParser import SafeConfigParser

config = SafeConfigParser()
config.read ('config/config.ini')

Server = config.get("BotConnectionParams","Server")
Channel = config.get("BotConnectionParams","Channel")
Nick = config.get("BotConnectionParams","Nick")
IdentifyPassword = config.get("BotConnectionParams","IdentifyPassword")
AdminName = config.get("BotConnectionParams","AdminName")
ExitMessage = config.get("BotConnectionParams","ExitMessage")
Debug = False 
DebugChannel = config.get("BotDebugParams","DebugChannel")

print ("Starting " + Nick + " up! I'm firin mah lazah!")

if Debug == True:
	ConnectChan = DebugChannel
	print "Debug is Enabled, console will be spammed with junk shortly, good luck captain"
	print ("Connecting to : " + ConnectChan + " for my channel")
	print ("DEBUG: Using " + Nick + " and the identifer password " + IdentifyPassword + " to connect to " + Server)
elif Debug == False:
	ConnectChan = Channel
	print "I see you don't wanna debug, that means I'm stable, woooooo! *pops pills*"
	print ( "Connecting to : " + ConnectChan + " for my channel")

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((Server,6667))
irc.recv (4096)
irc.send('USER AinseyBot AinseyBot AinseyBot :AinseyBot IRC\r\n')
irc.send('NICK ' + Nick + '\r\n')
time.sleep(2)
irc.send("PRIVMSG" + " NICKSERV :identify " + IdentifyPassword +"\n")
irc.send('JOIN ' + ConnectChan + '\r\n')
irc.send('PRIVMSG ' + ConnectChan + ' :All rise, the bot has joined the channel\r\n')

while True:
	data = irc.recv (4096)
	print data
	
	if data.find(':hi') !=-1:
		t = data.split(':hi')
		to = t[1].strip()
		irc.send('PRIVMSG ' + ConnectChan + ' :' + Nick + ' waves hello' '\r\n')
