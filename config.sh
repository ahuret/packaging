#!/bin/bash

clear

BIN="alumet-local-agent"
FEATURE="local_x86"
VERSION="0.7"
ARCH="amd64"

URL="https://github.com/alumet-dev/alumet/archive/refs/heads/main.zip"
FILE="src.zip"

check_perm() {
    if [ "$#" -eq 0 ]; then
        echo "Not a command"
        exit 1
    elif ! sudo -n true 2>/dev/null; then
        echo "Root permissions are needed"
        exit 1
    fi

    sudo "$@"
}

download_src(){
    clear
    echo -e "[ SOURCES DOWNLOADING ]\n"

    cd build/
    echo -e "\n<< Downloading 'alumet' project ressources... >>"
    wget "$URL" -O "$FILE" || { echo "ERROR : File not downloaded"; exit 1; }
    sync
    echo -e "\n<< Unzip 'alumet' project archive ressources... >>"
    unzip "$FILE" || { echo "ERROR : Unzipped file"; exit 1; }
    sync
    rm "$FILE"
    cd ..
}

compile_src(){
    clear
    echo -e "[ SOURCES COMPILATION ]\n"

    cd build/alumet-main
    cargo build --release --bin "$BIN" --features="$FEATURE"
    sync
    cd ../../
}

compile_pkg(){
    clear
    echo -e "[ PACKAGING COMPILATION ]\n"

    cp build/alumet-main/target/release/"$BIN" alumet/usr/lib/alumet/"$BIN"
    check_perm dpkg --build alumet alumet_"$VERSION"_"$ARCH".deb
    rm -rf build/alumet-main
}

check_perm apt install wget unzip
download_src
compile_src
compile_pkg
