from sys import argv
input=open(argv[1])
output=open(argv[2], 'w')
output.write(input.read())
output.close()
input.close()