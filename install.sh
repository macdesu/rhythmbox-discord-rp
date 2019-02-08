#!/bin/sh

PLUGIN_PATH="$HOME/.local/share/rhythmbox/plugins/rbdrp"

mkdir -p $PLUGIN_PATH
cp *.py rbdrp.plugin -t $PLUGIN_PATH
