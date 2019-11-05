#!/bin/bash

remove_old_version(){

echo "Old version of node will be removed..."
sudo apt-get purge node nodejs node.js -y
sudo apt-get autoremove

}

install_node(){

if uname -m != "x86_64"
then
echo "Es ist ein Armv6"
sudo su
cd /opt
wget https://nodejs.org/dist/v6.9.5/node-v6.9.5-linux-armv6l.tar.gz -O - | tar -xz
mv node-v6.9.5-linux-armv6l nodejs
apt-get update && apt-get upgrade
apt-get install build-essential
ln -s /opt/nodejs/bin/node /usr/bin/node
ln -s /opt/nodejs/bin/node /usr/bin/nodejs
ln -s /opt/nodejs/bin/npm /usr/bin/npm
exit
export PATH=$PATH:/opt/nodejs/bin/

else
echo "Es ist ein anderer."
curl -sL https://deb.nodesource.com/setup_6.x | sudo -E bash -
sudo apt-get update -y && sudo apt-get upgrade -y
sudo apt-get install build-essential nodejs -y
fi

node --version
npm -v

}

install_blynk(){

sudo npm install blynk-library -g
sudo npm install onoff -g

}


install_git(){

cd /home/dominic
git init

}

#FUNKTIONSAUFRUFE
#remove_old_version
#install_node
#install_blynk
install_git
