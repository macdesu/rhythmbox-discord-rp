#!/usr/bin/python
from pypresence import Presence
import time
import os

client_id = "543459024390324245"
now_playing = os.popen("rhythmbox-client --print-playing").read()

RPC = Presence(client_id)
RPC.connect()
RPC.update(state=now_playing)
while True:
    time.sleep(15)
