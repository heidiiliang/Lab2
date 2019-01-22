# File processing in Python
1. How do you ask if a file exists?
	```
	import os.path
	os.path.exists(file_path)
	```

2. How to you ask if a file is a directory?
	```
	import os.path
	os.path.isdir(file_path)
	```

3. How do you remove (delete) a file?
	```
	import os
	os.system("rm filepath")
	```

4. How do you get the size of a file?
	```
	import os
	os.path.getsize(file_path)
	```

5. How do you get all the file names matching a pattern?
	```
	import glob
	# Get all files with .xxx extension
	glob.glob('/my/path/*.xxx')
	```

6. How do you get all the file names matching a pattern recursively?
	```
	files=glob.iglob('directory/*/*file*')
	print(files)
	```

7. How do you get an iterator to all files matching a pattern, as opposed to returning a potentially huge list?
	```
	import glob
	glob.iglob(pathname)
	```

8. How do you open gzip-compressed files for reading and for writing?
	```
	#read a compressed file
	import gzip
	with gzip.open('filepath', 'rb') as f:
    	 file_content = f.read()
	#write a compressed file
	import gzip
	content = b"Lots of content here"
	with gzip.open('/home/joe/file.txt.gz', 'wb') as f:
    	f.write(content)
	```

# File processing in R
1. How do you ask if a file exists?
	```
	file.exists("filepath")
	```

2. How to you ask if a file is a directory?
	```
	dir.exists("filedirectory")
	```

3. How do you remove (delete) a file?
	```
	file.remove("filepath")
	```

4. How do you get the size of a file?
	```
	file.info("filepath")
	```
5. How do you get all the file names matching a pattern?
	```
	#all files with .xxx extension
	files <- list.files(pattern = "\\.xxx$")
	```

6. How do you get all the file names matching a pattern recursively?
	```
	files <- list.files(pattern = "\\.xxx$", recursive=T)
	```

8 How do you open gzip-compressed files for reading and for writing?
	```
	#write a compressed file
	write.table(tst.df,gzfile("test.dat.gz"))
	#read a compressed file
	read.table(gzfile("test.dat.gz"),row.names=1)
	```

updated answers-2
