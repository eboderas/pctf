# _pctf_

## Get SSH Login Credentials
Example using in-class information:
```shell
python get_ssh.py -t 35.161.233.76 -u team1@example.com -p password
```

## Tools
Current and planned list of scripts:
+ **exploit.py** _offense_ generic exploit template with remote_connection and flag_id - [@kanak](https://cse545spring17.slack.com/team/kanak), [@eboderas](https://cse545spring17.slack.com/team/eboderas)
+ **manage_exploits.py** _offense_ automated exploitation tool using pwntools framework - [@kanak](https://cse545spring17.slack.com/team/kanak), [@eboderas](https://cse545spring17.slack.com/team/eboderas)
+ **analyze_service.py** _defense_ binary-protection tool using angr framework for analysis - [@vc0622](https://cse545spring17.slack.com/team/vc0622), [@lzbaer](https://cse545spring17.slack.com/team/lzbaer)
+ **monitor_flag_traffic.py** _defense_ identify unique payloads to reverse engineer exploits - [@rang1](https://cse545spring17.slack.com/team/rang1), [@tcrosenk](https://cse545spring17.slack.com/team/tcrosenk)
+ **get_ssh.py** _misc_ automate login process - [@mohseenrm](https://cse545spring17.slack.com/team/mohseen)

_add yourself where interested_

## Related
+ [angr](http://angr.io/) python framework for analyzing binaries
+ [pwntools](https://github.com/Gallopsled/pwntools#readme) CTF framework and exploit development library
+ [reverse shell](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) cheat sheet for possible command execution vulns
