class kangaroo(object):



    def __init__(self, contents = None):
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def put_in_pouch(self,value):
        self.pouch_contents.append(value)

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = []
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)   
        return '\n'.join(t)




kanga = kangaroo()
roo = kangaroo()

kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)
roo.put_in_pouch('roo')
print kanga
print roo

#kanga.put_in_pouch(roo)
#print kanga
