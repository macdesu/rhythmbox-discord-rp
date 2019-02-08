#!/usr/bin/python
import os, time
from pypresence import Presence

old_timestamp = '0:00'
client_id = "543459024390324245"
RPC = Presence(client_id)
RPC.connect()

while True:
	time.sleep(1)
	artist = os.popen("rhythmbox-client --print-playing-format=\"%ta\"").read()
	title = os.popen("rhythmbox-client --print-playing-format=\"%tt\"").read()
	timestamp = os.popen("rhythmbox-client --print-playing-format=\"(%te / %td)\"").read()

	# play / pause
	if timestamp != old_timestamp:
		old_timestamp = timestamp
		small_image = "play-circle"
	else:
		small_image = "pause-circle"
		timestamp = " (Paused)"

	# prevent crash when stopped
	if len(artist) < 2:
		artist = "   "
	if len(title) < 2:
		title = "IDLE"

	RPC.update(details=artist, state=title + timestamp, large_image="rhythmbox", small_image=small_image)
