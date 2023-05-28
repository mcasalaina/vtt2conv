#If the first argument is not specified, throw an error saying it needs a filename
import sys
if len(sys.argv) < 2:
    print('Usage: vtt2conv.py filename')
    sys.exit(1)

#Open the file specified by the first argument for reading
f = open(sys.argv[1], 'r')

#Open the file specified by the second argument for writing - if the second argument is not specified, use the name of the first argument with .txt appended
if len(sys.argv) > 2:
    g = open(sys.argv[2], 'w')
else:
    g = open(sys.argv[1] + '.txt', 'w')

#Run through each line of the file f, if the line matches the regex "<v (.*)>([^<]*)</v>", replace it with $1: $2 and write it to the output file g, otherwise do not write the line to the output file
import re
for line in f:
    if re.match('<v (.*)>([^<]*)</v>', line):
        g.write(re.sub('<v (.*)>([^<]*)</v>', r'\1: \2', line))

#Close the files
f.close()
g.close()