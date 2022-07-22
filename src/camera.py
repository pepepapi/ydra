#  camera.py - take snapshots of pygame frames to form animated gifs

import sarg

class Camera :
    def __init__ (self, pg) :
        self.maxpics   = sarg.Int("maxpics",0)
        self.prefix    = sarg.Str("prefix")
        self.gif       = sarg.Int("gif",0)
        self.skip      = sarg.Int("skip",0)
        self.picsTaken= 0
        self.armed = False
        if self.gif > 1 : self.maxpics = self.gif    # short cut
        self.pg    = pg

    def takePicture(self, screen) :
        #print "Camera:", self.picsTaken, "of", self.maxpics, self.armed, self.prefix
        if self.picsTaken>=self.maxpics or not self.armed or not self.prefix :
            return False
        self.picsTaken += 1
        file = "%s_%03d.png" % (self.prefix, self.picsTaken)
        if self.skip <= self.picsTaken :  
            self.pg.image.save(screen, file)
            print( "Just captured frame: %d, %s"%(self.picsTaken, file))
        self.armed = False
        return True

    def makeGif(self, loop=1, delay=50) :
        import os
        if not self.picsTaken or not self.gif : return
        prefix = self.prefix
        print ("Making GIF")
        cmd = "convert -delay %d -loop %d %s_*.png %s.gif"
        cmd = cmd % (delay, loop, prefix,prefix)
        print (cmd)  # print the imageMagick convert command
        # create the .gif file with ImageMagick
        print( "%s.gif has %d frames" % (prefix,self.picsTaken))
        os.system(cmd)
        if not sarg.Int("keep_pngs", 0) :
            os.system("rm %s_*.png" % prefix)
