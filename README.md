# _pctf_

## Get SSH Login Credentials
Example using in-class information:
```shell
python get_ssh.py -t 35.161.233.76 -u team1@example.com -p password
```

## Tools
* **manage_exploits.py** - [@kanak](https://cse545spring17.slack.com/team/kanak), [@eboderas](https://cse545spring17.slack.com/team/eboderas)
    * Manage custom written exploits and ensure that they are used to exploit their specific services against each host, each tick, and then submit the retrieved flags.
    * Exploits are dynamically loaded in from exploits.py, which is where our custom exploits are generically written given a remote_connection and flag_id to return a flag, possibly using features from **pwntools**.
* **monitor_flag_traffic.py** - [@rang1](https://cse545spring17.slack.com/team/rang1), [@tcrosenk](https://cse545spring17.slack.com/team/tcrosenk)
    * Watch network traffic, and log all tcp conversations in which a flag was sent out. 
    * Perform analysis on these conversations to identify those that are unique in order to quickly reverse engineer exploits sent at us.
* **analyze_service.py** - [@vc0622](https://cse545spring17.slack.com/team/vc0622), [@lzbaer](https://cse545spring17.slack.com/team/lzbaer)
    * Analyze a service for potential vulnerabilities both statically and dynamically. 
    * Statically report calls to unsafe system/library calls such as _printf_, _strcpy_, etc. 
    * Dynamically try to determine unsafe code paths using **angr** and report them.
    * Produce a hardened service, if possible.
* **get_ssh.py** - **DONE** [@kanak](https://cse545spring17.slack.com/team/kanak)
    * Conveniently generate bash scripts that allow us to ssh into our game vm.

## Related
* [angr](http://angr.io/) python framework for analyzing binaries
* [pwntools](https://github.com/Gallopsled/pwntools#readme) CTF framework and exploit development library
* [reverse shell](http://pentestmonkey.net/cheat-sheet/shells/reverse-shell-cheat-sheet) cheat sheet for possible command execution vulns
