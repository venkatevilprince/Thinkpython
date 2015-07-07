import os
import sys
import subprocess


def walk(dirname):
    """Finds the names of all files in dirname and its subdirectories.
    dirname: string name of directory
    """
    names = []
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        #print path
        if os.path.isfile(path):
            names.append(path)
        else:
            names.extend(walk(path))
    return names


def compute_checksum(filename):
    """Computes the MD5 checksum of the contents of a file.

    filename: string
    """
    cmd = 'md5sum ' + filename
    res, stat = pipe(cmd)
    checksum, _ = res.split()
    return checksum
    


def check_diff(name1, name2):
    """Computes the difference between the contents of two files.

    name1, name2: string filenames
    """
    cmd = 'diff %s %s' % (name1, name2)
    #print "checking diff"
    return pipe(cmd)


def pipe(cmd):
    """Runs a command in a subprocess.

    cmd: string Unix command

    Returns (res, stat), the output of the subprocess and the exit status.
    """
    fp = subprocess.Popen(cmd, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    res, stat = fp.communicate()
    #print res,stat
    assert stat is None
    return res, stat


def compute_checksums(dirname, suffix):
    """Computes checksums for all files with the given suffix.

    dirname: string name of directory to search
    suffix: string suffix to match

    Returns: map from checksum to list of files with that checksum
    """
    names = walk(dirname)

    d = {}
    for name in names:
        if name.endswith(suffix):
            checksum = compute_checksum(name)
            

            if checksum in d:
                d[checksum].append(name)
            else:
                d[checksum] = [name]

    return d


def check_pairs(names):
    """Checks whether any in a list of files differs from the others.

    names: list of string filenames
    """
    for name1 in names:
        for name2 in names:
            if name1 < name2:  #this statement is to reduce redundant checks
                res, stat = check_diff(name1, name2)
                if res:
                    return False
    return True


def print_duplicates(d):
    """Checks for duplicate files.

    Reports any files with the same checksum and checks whether they
    are, in fact, identical.

    d: map from checksum to list of files with that checksum
    """
    for key, names in d.iteritems():
        if len(names) > 1:
            print 'The following files have the same checksum:'
            for name in names:
                print name

            if check_pairs(names):
                print 'And they are identical.'


if __name__ == '__main__':
    """Program to display all the redundant files in a directory using md5 and diff checks"""
    d = compute_checksums(dirname='.', suffix = '.py')  #tested with .py files (i dont have mp3 files)
    print_duplicates(d)
    #print os.listdir('.')
    #print check_diff('same1.py','same2.py')
    #c1 = compute_checksum('same1.py')
    #c2 = compute_checksum('same2.py')
    #pro = subprocess.Popen("diff same1.py test_popen.py", stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    #print pro.communicate()
    #nam = walk('.')
    #print nam
