#########################
## Connor Nelson, 2017 ##
#########################

import os
import argparse

from ictf import iCTF

ROOT_KEY_PATH = 'root.key'
CTF_KEY_PATH = 'ctf.key'
ROOT_SCRIPT_PATH = 'connect_root'
CTF_SCRIPT_PATH = 'connect_ctf'

SCRIPT = \
"""
#!/bin/bash

ssh -i %s -p %d %s@%s
"""

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--team-interface', required=True)    
    parser.add_argument('-u', '--username', required=True)
    parser.add_argument('-p', '--password', required=True)
    args = vars(parser.parse_args())

    team_interface = 'http://' + args['team_interface'] + '/'
    client = iCTF(team_interface)

    team = client.login(args['username'], args['password'])
    keys = team.get_ssh_keys()

    with open(ROOT_KEY_PATH, 'wb') as root_key:
        root_key.write(keys['root_key'])
    os.chmod(ROOT_KEY_PATH, 0600)

    with open(CTF_KEY_PATH, 'wb') as ctf_key:
        ctf_key.write(keys['ctf_key'])
    os.chmod(CTF_KEY_PATH, 0600)

    with open(ROOT_SCRIPT_PATH, 'w') as root_script:
        connect_root = SCRIPT % (ROOT_KEY_PATH, keys['port'], 'root', keys['ip'])
        root_script.write(connect_root)
    os.chmod(ROOT_SCRIPT_PATH, 0700)

    with open(CTF_SCRIPT_PATH, 'w') as ctf_script:
        connect_ctf = SCRIPT % (CTF_KEY_PATH, keys['port'], 'ctf', keys['ip'])
        ctf_script.write(connect_ctf)
    os.chmod(CTF_SCRIPT_PATH, 0700)

    print 'Successfully found SSH keys'
    print 'Team ID: %d' % (keys['team_id'],)
    print 'IP Address: %s' % (keys['ip'],)
    print 'Port: %d' % (keys['port'],)
    print 'Connect to root with: ./%s' % (ROOT_SCRIPT_PATH,)
    print 'Connect to ctf with: ./%s' % (CTF_SCRIPT_PATH,)


if __name__ == '__main__':
    main()
