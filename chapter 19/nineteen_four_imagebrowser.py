import os, sys
from swampy.Gui import *
from PIL import Image     
import ImageTk
class ImageBrowser(Gui):
    """An image browser that scans the files in a given directory and
    displays any images that can be read by PIL.
    """
    def __init__(self):
        Gui.__init__(self)

        # clicking on the image breaks out of mainloop
        self.button = self.bu(command=self.quit, relief="flat")

    def image_loop(self, dirname='.'):
        """loop through the files in (dirname), displaying
        images and skipping files PIL can't read.
        """
        files = os.listdir(dirname)
        i = -1
        print len(files)
        while (i <= len(files)):
            i += 1
            print i
            try:
                print "trying"
                self.show_image(files[i])
                print files[i]
                self.mainloop()
            except IOError:
                continue
            except:
                break
            if i == len(files)-1:
                i = -1
                print "happens"
            

    def show_image(self, filename):
        """Use PIL to read the file and ImageTk to convert
        to a PhotoImage, which Tk can display.
        """
        image = Image.open(filename)
        self.tkpi = ImageTk.PhotoImage(image)
        self.button.config(image=self.tkpi)

def main(script, dirname='.'):
    g = ImageBrowser()
    g.image_loop(dirname)
    #g.show_image("aE3uhPPr.jpg")
    g.mainloop()
    g.destroy()
    
if __name__ == '__main__':
    main(*sys.argv)
