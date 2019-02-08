#!/bin/sh

PLUGIN_PATH="$HOME/.local/share/rhythmbox/plugins/rbdrp"

mkdir -p $PLUGIN_PATH
cp rbdrp.py rbdrp.plugin -t $PLUGIN_PATH
