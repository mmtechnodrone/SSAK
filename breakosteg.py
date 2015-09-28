#!/usr/bin/env python

import os, pwd, sys, re, time
from decimal import Decimal
from subprocess import Popen, PIPE

home = pwd.getpwuid(os.getuid()).pw_dir + '/SSAK/'
execdir = os.path.dirname(os.path.realpath(sys.argv[0]))
stegprog = 'java -jar ' + re.escape(execdir) + '/programs/noarch/openstego.jar'

passfile = sys.argv[1]
stegfile = sys.argv[2]
outdir = sys.argv[3]
count = 1
def file_len (passfile):
	with open(passfile) as f:
		for i, l in enumerate(f):
			pass
	return i + 1
i = file_len(passfile)
with open(passfile, "r") as f:
	for passwd in f:
		sys.stdout.write(passwd)
		cmd1 = stegprog + ' extract --algorithm=RandomLSB --stegofile=' + re.escape(stegfile) + ' --extractdir=' + outdir + ' --password=' + passwd
		proc1 = Popen(cmd1, shell=True, stderr=PIPE, stdout=PIPE)
		line1 = ''
		for append in proc1.stdout:
			line1 += append
		for append in proc1.stderr:
			line1 += append
		if "Extracted" in line1:
			print line1.rstrip() + " Algorithm=RandomLSB Password is: " + passwd
			break
		cmd2 = stegprog + ' extract --algorithm=LSB --stegofile=' + re.escape(stegfile) + ' --extractdir=' + re.escape(outdir) + ' --password=' + passwd
		proc2 = Popen(cmd2, shell=True, stderr=PIPE, stdout=PIPE)
		line2 = ''
		for append in proc2.stdout:
			line2 += append
		for append in proc2.stderr:
			line2 += append
		if "Extracted" in line2:
			print line2.rstrip() + " Algorithm=LSB Password is: " + passwd
			break
		dec = Decimal(count) / Decimal(i)
		perc = Decimal(dec) * Decimal(100)
		print "%0.02f" %perc + "% \n" 
		count += 1
