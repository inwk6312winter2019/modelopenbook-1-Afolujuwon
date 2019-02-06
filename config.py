#configuration = open('running-config.cfg')
#print (configuration.readlines())

def list_ifname_ip(configuration):
	
	configuration = open('running-config.cfg')
	list1 = []
	list2 = []
	list3 = []
	list4 = []
	list5 = []
	list6 = []
	list7 = []
	dict = {}
	for line in configuration:
		line = line.strip()
		for word in line.split():
			list1.append(word)
	for i in range(len(list1)):
		if list1[i] == 'interface':
			list2.append(list1[i+1])
		elif list1[i]=='nameif' or list1[i] == 'no' and list1[i+1] == 'nameif':
					
			if list1[i] == 'no' and list1[i+1] == 'nameif':
				list3.append('no name')
				list4.append('no vlan')
				list5.append('no ip address')
				list6.append('no mask')

			elif list1[i-1]!='no' and list1[i] ==  'nameif':
				list3.append(list1[i+1])
				list5.append(list1[i+6])
			list6.append(list1[i+7])
		if list1[i-1] == 'management-only':
			list4.append('no vlan')
		else:
			list4.append(list1[i-2] + list1[i-1])
			
	for i in range (len(list2)):
		list7= []
		list7.append(list3[i])
		list7.append(list4[i])
		list7.append(list5[i])
		list7.append(list5[i])
		dict [list2[i]] = list7
	print(dict)


list_ifname_ip('running-configuration.cfg')






