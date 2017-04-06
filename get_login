#!/usr/bin/env python2.7

#########################
## Connor Nelson, 2017 ##
#########################

import os
import argparse

from ictf import iCTF

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required=True)
    parser.add_argument('-p', '--password', required=True)
    parser.add_argument('-r', '--root-key-path', required=True)
    parser.add_argument('-c', '--ctf-key-path', required=True)
    args = vars(parser.parse_args())

    client = iCTF('http://35.161.233.76/')

    team = client.login(args['username'], args['password'])
    keys = team.get_ssh_keys()

    root_key_path = args['root_key_path']
    root_key = open(root_key_path, 'w')
    root_key.write(keys['root_key'])
    os.chmod(root_key_path, 0600)

    ctf_key_path = args['ctf_key_path']
    ctf_key = open(ctf_key_path, 'w')
    ctf_key.write(keys['ctf_key'])
    os.chmod(ctf_key_path, 0600)

    print 'your team id is: %d' % (keys['team_id'],)
    print 'connect to root with:'
    print 'ssh -i %s root@%s -p %s' % (root_key_path, keys['ip'], keys['port'])
    print 'connect to ctf with:'
    print 'ssh -i %s ctf@%s -p %s' % (ctf_key_path, keys['ip'], keys['port'])

if __name__ == '__main__':
    main()
    
