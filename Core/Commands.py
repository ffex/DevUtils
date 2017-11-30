import os

#format:
#"n,a,d,q,v"
def isCommandOK(cformat,command):
    result=False
	acceptedCom=cformat.Split(',')
	if (len(command)==1 or (len(command)>=2 and command[1]==',')):
	    for x in acceptedCom:
		    if command[0]==x:
			    result=True
	else:
	    result=False
	return result

def isLink(URL):
    result=False
	if URL.startswith('http://'):
	    result=True
	if URL.startswith('https://'):
	    result=True
	if URL.startswith('www'):
	    result==True
	return result
	
def isDirectory(dirname):
    result=False
	if dirname.startswith('/'):
	    result=True
	if dirname.startswith('$'):
	    result=True
	return result