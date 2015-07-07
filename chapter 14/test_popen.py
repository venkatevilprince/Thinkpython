import sys, string, os
import subprocess
#b = os.popen('C:\Program Files (x86)\7-Zip\7zFM.exe')
#print b

os.chdir( r'C:\Program Files (x86)\Notepad++' )
print os.getcwd()
#os.startfile( "notepad++.exe" )
#process = subprocess.Popen("notepad++.exe", shell=True, stdout=subprocess.PIPE)
os.chdir( r'C:\Users\venkateshwaran.s\Desktop\learn python\Thinkpython\chapter 14' )
print os.getcwd()
#os.startfile( "fourteen_one.py" )
#subprocess.call(["fourteen_one.py"])

p = subprocess.Popen(['python','fourteen_two.py'],stdout=subprocess.PIPE,shell = False)#, shell=True)

#print subprocess.Popen.stdout
#proc = subprocess.Popen(['echo', '"Hello world!"'],shell=True,stdout=subprocess.PIPE)
#print proc.communicate()[0]
#subprocess.check_output('echo "hello world"', shell=True)
