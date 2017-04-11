# _pctf_

## Get SSH Login Credentials
Example using in-class information:
```shell
python get_ssh.py -t 35.161.233.76 -u team1@example.com -p password
```

## Tools
Current and planned list of scripts:
+ **exploit.py** _offense_ automated exploitation tool using pwntools framework - [@kanak](https://cse545spring17.slack.com/team/kanak), [@eboderas](https://cse545spring17.slack.com/team/eboderas)
+ **patch.py** _defense_ binary-protection tool using angr framework for analysis - [@vc0622](https://cse545spring17.slack.com/team/vc0622), [@lzbaer](https://cse545spring17.slack.com/team/lzbaer)
+ **patterns.py** _defense_ network-defense tool for exploit pattern scanning in packets - [@rang1](https://cse545spring17.slack.com/team/rang1), [@tcrosenk](https://cse545spring17.slack.com/team/tcrosenk)
+ **reflector.py** _offense_ defense-turned-offense tool that attacks teams with their own exploits - [@eboderas](https://cse545spring17.slack.com/team/eboderas), [@mohseenrm](https://cse545spring17.slack.com/team/mohseen)
+ **alter_flags.py** _defense_ prevent exfiltration of flags by other teams and whitelist gamebot - [@kanak](https://cse545spring17.slack.com/team/kanak),[@tcrosenk](https://cse545spring17.slack.com/team/tcrosenk)
+ **get_ssh.py** _misc_ automate login process [@mohseenrm](https://cse545spring17.slack.com/team/mohseen)

_add yourself where interested_

## Related
+ [angr](http://angr.io/) python framework for analyzing binaries
+ [pwntools](https://github.com/Gallopsled/pwntools#readme) CTF framework and exploit development library
+ [reverse shell](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) cheat sheet for possible command execution vulns
