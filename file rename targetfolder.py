
def main() :
    import os
    import re
    
    target = os.getcwd()
    imglist = os.listdir(target)
    
    cnt = 95
    for tmpimg in imglist :
        imgname, imgformat = tmpimg.split(".")
        if imgformat == "py" : continue
		
        count = str(cnt).zfill(5)
        
        oldname = target + '/' + imgname + '.' + imgformat
        newname = target + '/' + str(count) + '.' + imgformat
        os.rename(oldname, newname)
        cnt = cnt + 1

main()
