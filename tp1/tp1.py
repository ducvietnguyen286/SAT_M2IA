import sys
def readfile(file):
	filename = file
	if not os.path.isfile(filename):
    	print('File does not exist.')
	else:
	with open(filename) as f:
    	content = f.read().splitlines()
    for line in content:
    	print(line)
    	
