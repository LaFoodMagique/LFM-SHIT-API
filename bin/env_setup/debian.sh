#!/usr/bin/env sh


distrib="Debian"
app="LFM-API"


#
#   Start / Finish
#

start() {
    echo "$distrib installation script for the '$app' start."
}


finish() {
    echo "$distrib installation script for the '$app' finish."
}


#
#   System update / upgrade
#

system_update() {
    echo "The script will now update your system."

    while true; do
        read -p "Do you want to upgrade your system? (recommended) [y/n]" y
        case $y in
            [YyYesyes]* ) sudo apt-get update -y; break;;
            * ) break;;
        esac
    done

    if [ $? -ne 0 ]
        then
        echo 'Error: The script has failed to update the system.'
        exit
    fi
}

system_upgrade() {
    echo "The script will now upgrade your system."

    while true; do
        read -p "Do you want to upgrade your system? (recommended) [y/n]" y
        case $y in
            [YyYesyes]* ) sudo apt-get upgrade -y; break;;
            * ) break;;
        esac
    done

    if [ $? -ne 0 ]
        then
        echo 'Error: The script has failed to upgrade the system.'
        exit
    fi
}


#
#   Packages installation
#

packages_installion() {
    echo "The script will now try to install the required packages."

    sudo apt-get install python3 python3-dev python3.4-venv

    if [ $? -ne 0 ]
        then
        echo 'Error: The script has failed to install the required packages.'
        exit
    fi
}


#
#   Env setup
#

env_setup() {
    echo "The script will now try to setup your environment."
}


#
#   Script start
#

start

system_update

system_upgrade

#packages_installion

#env_setup

finish
