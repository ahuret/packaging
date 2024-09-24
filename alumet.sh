#!/bin/bash

DEFAULT_ALUMET_CONFIG_FILE="/etc/alumet/alumet-config.toml"

if [ -f "$DEFAULT_ALUMET_CONFIG_FILE" ]; then
    # Config file exists
    echo "The config file already exists"
else
    # Config file doesn't exist
    echo "The config file does not exist yet"
fi

alumet_bin_name=$(basename "$0")
path_to_bin=$(temp=$( realpath "$0"  ) && dirname "$temp")

if [[ -x "$path_to_bin/alumet/$alumet_bin_name" ]]; then
    $path_to_bin/alumet/$alumet_bin_name --config "$DEFAULT_ALUMET_CONFIG_FILE"
else
    echo "Error: $path_to_bin/alumet/$alumet_bin_name not found or not executable."
    exit 1
fi

