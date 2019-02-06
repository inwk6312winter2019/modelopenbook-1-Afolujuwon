def acl():
	transit = []
	management = []
	globl = []
	file = open("running-config.cfg")
	for line in file:
		if("transit_access_in" in line):
			transit.append(line)
		if("global_access" in line):
			globl.append(line)
		if("fw-management_access_in" in line):
			management.append(line)
	print(transit)
	print(management)
	print(globl)

acl()
