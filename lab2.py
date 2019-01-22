#unzip file
import tarfile
tf = tarfile.open('/Users/HEIDI/Documents/19advinformatics/lab2/lab2data.tar.gz')
tf.extractall()

#make lists for input and output
import glob
input = glob.glob('/lab2data/data/*')
output = glob.glob('/lab2data/output/*')

#select out the variable that distinguishes each file (.# and .a/b)
#join the # and a or b together 
import re
f = lambda x: ''.join(re.findall('datafile\.(.*)\.(.*)\..*',x)[0])
data_input = map(f, input)
f = lambda x: ''.join(re.findall('outfile\.(.*)\.(.*)\..*',x)[0])
data_output = map(f, output)

#find out those missing in the output folder
missing = set(data_input).difference(data_output)

#number of missing files
print(len(missing))

#write out the names of the missing files in "missing.txt"
with open('missing.txt','w') as f:
 for x in missing:
  f.write('outfile.%s.%s.out\n' % (x[:-1],x[-1]))
 f.close()

