import os
def walk1(dirname):
    """prints the all the files in the directory and subdirectories"""
    for name in os.listdir(dirname):
        path=os.path.join(dirname,name)

        if os.path.isfile(path):
           print path

        else:
           walk1(path)
def walk2(dirname):
    """prints the all the files in the directory and subdirectories"""
    count=0
    for root, dir, files in os.walk(dirname):
        #print root, dir, files,count;count += 1
        for filename in files:
            print os.path.join(root, filename)

print "walk 1"
walk1('.')
print "walk 2"
walk2('.')
#print os.walk('.')
cwd = os.getcwd()
print cwd
print "absolute path ", os.path.abspath('a')
print "isdir test ", os.path.isdir('a')
print "isfile test ", os.path.isfile('a')
