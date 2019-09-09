f = open("templates/onboard/form.js","r")
f1 = open("templates/onboard/temp.js","w+")
for x in f:
	if (x.strip()!="<br>" and x.strip()!="</br>"):
		f1.write(x)
