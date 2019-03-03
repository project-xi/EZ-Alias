#!/usr/bin/env bash
# Author : Lyhour Chhen
# Script : Ez Alias :D

USER=whoami
location=~/.bashrc

#Ask for Softcut
echo "Enter the Commend u want to change:" && read commend

#Ask For Commend
echo "Enter the shortcut u want to define :"
read softcut

# if [[ softcut="" ]]; then
#     echo "Your string is empty !" && exit
# fi

#Ask for Decription for the commend
echo "Enter any Decription"
read Decription

echo "----------------------"
echo "Your new commends"
echo "$commend ===> $softcut"
echo "----------------------"
echo "Decription ==> $Decription"

echo "=========================="
echo "alias $softcut='$commend'">>$location

# Function to handle error in this script


echo "Execute the alias has been successfully :P"
source ~/.bashrc
echo "Exit the program"
