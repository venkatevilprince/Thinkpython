class kangaroo(object):



    def __init__(self, contents = None):
        #print "init running",contents
        if contents == None:
            contents = []
        self.pouch_contents = contents
        
    def put_in_pouch(self,value):
        print "before",self.name, self.pouch_contents
        self.pouch_contents.append(value)
        print "after",self.name, self.pouch_contents

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = []
        for obj in self.pouch_contents:
            s = '' + str(obj)  #converts object into string
            #print s
            t.append(s)   
        return '\n'.join(t)

kanga = kangaroo()
roo = kangaroo()
kanga.name="kanga"
roo.name= "roo"
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
roo.put_in_pouch('roo')
#kanga.put_in_pouch(roo)

print kanga.pouch_contents is roo.pouch_contents
#print kanga
#print kanga.pouch_contents[2].pouch_contents
#print roo

#kanga.put_in_pouch(roo)
#print kanga
