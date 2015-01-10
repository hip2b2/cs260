#!/usr/bin/python
# CS 260 Programming Examples
# wyu@ateneo.edu

import paramiko

# load SSH client
ssh = paramiko.SSHClient()

# automatically accept host key for first time logins
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# disable other types of authentication outside of username/password
ssh.connect('127.0.0.1', username='test', password='test',
  allow_agent=False,look_for_keys=False)

# execute uptime command and direct all output to tuple streams
stdin, stdout, stderr = ssh.exec_command("uptime")
type(stdin)

# display output of stdout stream
print stdout.readlines()
