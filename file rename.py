
def main() :
    import os
    import re
    
    nowdir = os.getcwd()
    for filename in os.listdir(nowdir):
        target = nowdir + '/' + filename
        ckdir = os.path.isdir(target)
        if ckdir == True :
            imglist = os.listdir(target)
			
            for tmpimg in imglist :
                imgname, imgformat = tmpimg.split(".")
                
                count = re.findall("\d+",imgname)[0]
                count = count.zfill(5)
                
                oldname = target + '/' + imgname + '.' + imgformat
                newname = target + '/' + count + '.' + imgformat
                os.rename(oldname, newname)

main()
