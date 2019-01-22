import tarfile
tf = tarfile.open('/Users/HEIDI/Documents/19advinformatics/lab2/lab2data.tar.gz')
tf.extractall()

import glob
import re

input = glob.glob('/lab2data/data/*')
output = glob.glob('/lab2data/output/*')

f = lambda x: ''.join(re.findall('datafile\.(.*)\.(.*)\..*',x)[0])

data_input = map(f, input)
f = lambda x: ''.join(re.findall('outfile\.(.*)\.(.*)\..*',x)[0])
data_output = map(f, output)

missing = set(data_input).difference(data_output)

print(len(missing))

with open('missing.txt','w') as f:
 for x in missing:
  f.write('outfile.%s.%s.out\n' % (x[:-1],x[-1]))
 f.close()

