# _pctf_

## Get SSH Login Credentials
Example using in-class information:
```shell
python get_ssh.py -t 35.161.233.76 -u team1@example.com -p password
```

## Tools
Current and planned list of scripts:
+ **exploit.py** _offense_ automated exploitation tool
+ **patch.py** _defense_ binary-protection tool using angr framework for analysis
+ **patterns.py** _defense_ network-defense tool for exploit pattern scanning in packets
+ ~~**alter_flags.py** _defense_ prevent exfiltration of flags by other teams and whitelist gamebot~~
+ **get_ssh.py** _misc_ automate login process

Frameworks:
+ [angr](http://angr.io/) python framework for analyzing binaries
+ [pwntools](https://github.com/Gallopsled/pwntools#readme) CTF framework and exploit development library
+ [reverse shell](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) cheat sheet for possible command execution vulns
