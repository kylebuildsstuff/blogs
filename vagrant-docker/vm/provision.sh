#!/usr/bin/env bash

echo "Updating apt-get package manager..."
sudo apt-get update -y
echo "Installing and setting up Docker..."
sudo apt-get install linux-image-extra-$(uname -r) linux-image-extra-virtual -y
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] http://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get update -y
sudo apt-get install docker-ce
sudo apt install docker.io -y
echo "Configuring user..."
sudo usermod -aG docker ubuntu
sudo apt-get update -y
echo "Completed provisioning"
