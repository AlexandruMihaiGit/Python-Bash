#!/bin/bash

echo "./autoNmapGoB <target_ip>"

if [ -z "$1" ]; then
    echo "Use $0 <target_ip>"
    exit 1
fi

target=$1
output_dir_nmap="nmap_results"
mkdir -p $output_dir_nmap

echo "Scanning $target..."
nmap -sC -sV -oN "$output_dir_nmap/$target.txt" $target
echo "Scanare Nmap completată. Rezultatele sunt salvate în $output_dir_nmap."

url="http://$target"
wordlist="/usr/share/dirbuster/wordlists/directory-list-2.3-small.txt"
output_dir_gobuster="gobuster_results"
mkdir -p $output_dir_gobuster

echo "Running Gobuster on $url..."
gobuster dir -u $url -w $wordlist -o "$output_dir_gobuster/$target.txt"

echo "Gobuster scan completată. Rezultatele sunt salvate în $output_dir_gobuster."