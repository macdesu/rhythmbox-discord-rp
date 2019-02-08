#!/usr/bin/python
import os, time
from pypresence import Presence

client_id = "543459024390324245"
RPC = Presence(client_id)
RPC.connect()

while True:
	time.sleep(1)
	artist = os.popen("rhythmbox-client --print-playing-format=\"%ta\"").read()
	title = os.popen("rhythmbox-client --print-playing-format=\"%tt\"").read()
	start = os.popen("rhythmbox-client --print-playing-format=\"%te\"").read()
	end = os.popen("rhythmbox-client --print-playing-format=\"%td\"").read()
	RPC.update(details=artist, state=title)
