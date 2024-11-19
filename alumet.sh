#!/bin/bash

DEFAULT_ALUMET_CONFIG_FILE="/var/lib/alumet/alumet-config.toml"

alumet_bin_name=$(basename "$0")
path_to_bin=$(temp=$( realpath "$0"  ) && dirname "$temp")
LIB_ALUMET="${path_to_bin}/../lib/${alumet_bin_name}_bin"
if [[ -x "$LIB_ALUMET" ]]; then
    $LIB_ALUMET --config "$DEFAULT_ALUMET_CONFIG_FILE"
else
    echo "Error: $LIB_ALUMET not found or not executable."
    exit 1
fi

