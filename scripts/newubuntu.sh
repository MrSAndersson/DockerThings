#!/bin/bash

VERSION="$(lsb_release -c -s)"
RELEASE="$(lsb_release -r -s)"
PACKAGES=""

echo "$RELEASE: $VERSION"

read -p "Are you sure you want to install for this version? y/n: " -n 1 -r
echo    # (optional) move to a new line
if [[ ! $REPLY =~ ^[Yy]$ ]]
then
    [[ "$0" = "$BASH_SOURCE" ]] && exit 1 || return 1 # handle exits from shell or function but don't exit interactive shell
fi

# Install apt-transport-https

sudo apt-get update
sudo apt-get install apt-transport-https curl software-properties-common ca-certificates

#echo "Adding docker-ce repo"
#curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $VERSION stable"
#PACKAGES+="docker-ce docker-compose "

echo "Adding VSCode repo"

curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg
sudo install -o root -g root -m 644 microsoft.gpg /etc/apt/trusted.gpg.d/
sudo sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" > /etc/apt/sources.list.d/vscode.list'
PACKAGES+="code "

#echo "Adding GCloud repo"
#export CLOUD_SDK_REPO="cloud-sdk-$(lsb_release -c -s)"
#echo "deb http://packages.cloud.google.com/apt $CLOUD_SDK_REPO main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
#curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
#PACKAGES+="google-cloud-sdk "

echo "Adding Kubectl repo"
curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo touch /etc/apt/sources.list.d/kubernetes.list
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list.d/kubernetes.list
PACKAGES+="kubectl "

#echo "Adding .net core SDK repo"
#wget -q https://packages.microsoft.com/config/ubuntu/$RELEASE/packages-microsoft-prod.deb
#sudo dpkg -i packages-microsoft-prod.deb
#rm packages-microsoft-prod.deb
#PACKAGES+="dotnet-sdk-2.1 "

echo "Adding GCSFuse repo"
export GCSFUSE_REPO=gcsfuse-`lsb_release -c -s`
echo "deb http://packages.cloud.google.com/apt $GCSFUSE_REPO main" | sudo tee /etc/apt/sources.list.d/gcsfuse.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
PACKAGES1="gcsfuse "

echo "Adding Papirus Icon theme repo"
sudo add-apt-repository ppa:papirus/papirus
PACKAGES+="papirus-icon-theme "

echo "Adding Flatpak package repo"
sudo add-apt-repository ppa:alexlarsson/flatpak
PACKAGES+="flatpak gnome-software-plugin-flatpak "

#echo "Adding Puppet repo"
#wget https://apt.puppetlabs.com/puppet5-release-$VERSION.deb
#sudo dpkg -i puppet5-release-$VERSION.deb
#rm puppet5-release-$VERSION.deb
#PACKAGES+="puppet-agent "

echo "Update package cache"

sudo apt-get update

echo  "Install packages"

PACKAGES+="arc-theme gnome-tweaks git gnome-session gnome-shell-pomodoro tilix vim "

sudo apt-get install -y $PACKAGES


echo "Installing Google Chrome"
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb 
sudo dpkg -i google-chrome-stable_current_amd64.deb 
rm google-chrome-stable_current_amd64.deb

#echo "Installing Teamviewer"
#wget https://download.teamviewer.com/download/linux/teamviewer_amd64.deb



echo  "Enable Kubectl autocompletion"
echo "source <(kubectl completion bash)" >> ~/.bashrc

echo "Add FlatHub as a flatpak Repo"
flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

echo  "To update the login screen: 'sudo update-alternatives --config gdm3.css'"