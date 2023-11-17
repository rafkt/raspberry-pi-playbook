#!/bin/bash
if [ "$1" = "tunnel" ]; then
	code tunnel
elif [ "$1" = "server" ]; then
	echo "Running self hosted code server at port 8082"
	code-server --auth none --user-data-dir ~/.vscode --bind-addr 0.0.0.0:8082
else
	echo "unknown commad, options to pass: tunnel | server. The fist is using the microsoft servers, whilst the latter the serlf-hosted option"
fi
