#!/usr/bin/python

import os

podir = os.path.join(os.path.realpath("."), "po")
cfg_dir = os.path.join(os.path.realpath("."), "src/config")

if os.path.isdir(cfg_dir):
    print "Creating devicemanager.conf"
    cfg_file = os.path.join(cfg_dir, "devicemanager.conf")
    with open(cfg_file, "w") as f:
        # Check StartOS version
        if os.popen('lsb_release --release').readline().strip().split('.')[0] == '5':
            f.write('URI="http://pkg.startos.org/startos/5.0"')
        else:
            f.write('URI="http://pkg.startos.org/startos/6.0/devicemanager"')

if os.path.isdir (podir):
	buildcmd = "msgfmt -o src/share/locale/%s/LC_MESSAGES/%s.mo po/%s.po"
	
	for name in os.listdir (podir):		
		if name.endswith('.po'):
			dname = name.split('-')[1].split('.')[0]
			name = name[:-3]
			
			print 'Creating language Binary for : ' + name
			if not os.path.isdir ("src/share/locale/%s/LC_MESSAGES" % dname):
				os.makedirs ("src/share/locale/%s/LC_MESSAGES" % dname)
			os.system (buildcmd % (dname,name.replace('-'+dname,''), name))
