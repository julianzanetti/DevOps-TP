#!/bin/bash
echo "Adding apt-keys"
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo apt-key add -
echo deb https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list

echo "Updating apt-get"
sudo apt-get -qq update && sudo apt-get -qq upgrade

echo "Installing default-java"
sudo apt-get -y -q install openjdk-17-jre

echo "Installing jenkins 2.222"
sudo apt-get -y install jenkins
sudo service jenkins start

sleep 1m

echo "Installing Jenkins Plugins"
JENKINSPWD=$(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
echo $JENKINSPWD
