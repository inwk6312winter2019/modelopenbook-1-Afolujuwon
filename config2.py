def replace(file):
	file = open('running-config.cfg')
	file = file.readlines()
	file = [char.replace('192' or '172','10') for char in file] or [char.replace('255.255.255.0' or '255.255.0.0','255.0.0.0') for char in file]
	print(file)
		
replace('running-config.cfg')
