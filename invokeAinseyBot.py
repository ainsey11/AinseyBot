#!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket
import sys
import time
import urllib2
import re
from ConfigParser import SafeConfigParser
from BeautifulSoup import BeautifulSoup

config = SafeConfigParser()
config.read ('config/config.ini')

Server = config.get("BotConnectionParams","Server")
Channel = config.get("BotConnectionParams","Channel")
Nick = config.get("BotConnectionParams","Nick")
IdentifyPassword = config.get("BotConnectionParams","IdentifyPassword")
AdminName = config.get("BotConnectionParams","AdminName")
ExitMessage = config.get("BotConnectionParams","ExitMessage")
Debug = bool(config.get("BotDebugParams","EnableDebug"))
DebugChannel = config.get("BotDebugParams","DebugChannel")
WaveActivator = config.get("BotActivators","WaveActivator")
EnableURLPlugin = bool(config.get("BotPlugins","EnableURLPlugin"))

print ("Starting " + Nick + " up! I'm firin mah lazah!")

if Debug == True:
	ConnectChan = DebugChannel
	print "Debug is Enabled, console will be spammed with junk shortly, good luck captain"
	print ("Connecting to : " + ConnectChan + " for my channel")
	print ("DEBUG: Using " + Nick + " and the identifer password " + IdentifyPassword + " to connect to " + Server)
	if EnableURLPlugin == True:	
		print ("DEBUG: EnableURLPlugin is Enabled")
	elif  EnableURLPlugin == False:
		print ("DEBUG: EnableURLPlugin is Disabled")

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
	if data.find('PING') != -1:
		irc.send('PONG ' + data.split()[1] + '\r\n') 
	if data.find(':'+WaveActivator) !=-1:
		irc.send('PRIVMSG ' + ConnectChan + ' :' + Nick + ' waves hello' '\r\n')
	if EnableURLPlugin == True:
		if data.find(':http') !=-1:
			
			
