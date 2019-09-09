import xml.etree.ElementTree as et
from collections import OrderedDict
kfield = []
ofield= []
prooffield=set()
def field():
	tree = et.parse('xml_to_html/xml_file/field.xml')
	root = tree.getroot()
	for policy in root.find('policy-name'):
		if policy[1].text == "primary":
			kfield.append(policy[0].text)
			for t in policy.iter():
				if t.tag == "attachments":
					prooffield.add(t.text)

		else:
			ofield.append(policy[0].text)
			for t in policy.iter():
				if t.tag == "attachments":
					prooffield.add(t.text)
	return kfield,ofield,prooffield
