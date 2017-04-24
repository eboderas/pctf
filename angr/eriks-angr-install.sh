#! /bin/bash

# This scripts assumes your using bash for your shell

#The ANGR team highly recommends using a python virtual environment #because several of the required libraries use native code that are #forked from the originals and you wouldn’t want to overwrite the #original with the ones ANGR users.

if [ "$EUID" -ne 0 ]
  then printf "\033[31m Please run as root\033[0m\n "
  exit 224
fi

pip install virtualenvwrapper

if [ -z "$WORKON_HOME" ] ; then
	printf "# ========== [ Adding for virtualEnvWrapper ] =========\n" >> ~/.bashrc
	echo "export WORKON_HOME=~/Envs" >> ~/.bashrc
	export WORKON_HOME=~/Envs

	printf "using default WORKON_HOME, where the virtual envs live\n"
	echo "export PROJECT_HOME=~/ws" >> ~/.bashrc
	export PROJECT_HOME=~/ws

	printf "using default PROJECT_HOME, where your development projects live\n"
	echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc
	source /usr/local/bin/virtualenvwrapper.sh
	printf "# ========== [ END for virtualEnvWrapper ] =========\n" >> ~/.bashrc

	mkdir $WORKON_HOME
fi

if [ -z "$(workon)" ]; then
	mkvirtualenv angr # creates angr environment
fi

source $WORKON_HOME/angr/bin/activate #we are now in the angr virtual environment

printf " You are now in virtual env -[$VIRTUAL_ENV]-\n"

if [ -z "$VIRTUAL_ENV" ] ; then
	printf "\033[31mVIRTUAL_ENV=[$VIRTUAL_ENV]\n" 
	printf "\n\033[31m ERROR: virtual env is blank, stopping script.\033[0m\n"
	exit 201
fi

# NOW start loading ANGR items
apt-get install python-dev libffi-dev build-essential

if [[ $VIRTUAL_ENV == *"angr"* ]] ; then
	printf "\033[32m ***********************************************\033[0m\n"
	printf "\033[32m Starting ANGR installation on angr virtual env.\033[0m\n"
	printf "\033[32m ***********************************************\033[0m\n\n"
	pip install angr
	printf "\nCOMMAND:\033[32m workon angr \033[0m -- will enable the angr environment\n"
	printf "COMMAND:\033[32m deactivate \033[0m -- disables the angr environment\n\n"
else
	printf "\033[31mVIRTUAL_ENV=[$VIRTUAL_ENV]\n" 
	printf "ERROR: not connected to angr virtual env, stopping script.\033[0m\n"
fi




