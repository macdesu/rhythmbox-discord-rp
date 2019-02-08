#!/usr/bin/python
import os, time
from pypresence import Presence
# from gi.repository import GObject, RB, Peas

def discord():
	old_timestamp = ''
	client_id = "543459024390324245"
	RPC = Presence(client_id)
	RPC.connect()

	while True:
		time.sleep(1)
		artist = os.popen("rhythmbox-client --print-playing-format=\"%ta\"").read()
		title = os.popen("rhythmbox-client --print-playing-format=\"%tt\"").read()
		timestamp = os.popen("rhythmbox-client --print-playing-format=\"(%te / %td)\"").read()
		if timestamp != old_timestamp:
			old_timestamp = timestamp
			small_image = "play-circle"
		else:
			small_image = "pause-circle"
			timestamp = " (Paused)"
		RPC.update(details=artist, state=title + timestamp, large_image="rhythmbox", small_image=small_image)

discord()
