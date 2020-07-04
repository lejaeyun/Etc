
def main() :
    filename = "[완결]이알-게이트_Er·gate_-409.txt"
    
    with open(filename, 'r', encoding = "utf-8") as f :
        result = ""
        Contents = ""
        for c in list(map(lambda x:x.rstrip(), f.readlines())) :
            if c != "" :
                Contents += c
        
        communicate = False
        commu = ["“", "”", "\"", "'"]
        en = [".", "?", "!"]
        number = "123456789"
        enter_count = 0
        str_count = 0
        for s in Contents :
            appendix = s
            str_count += 1
            
            if s in commu and communicate == False :
                communicate = True
            elif s in commu and communicate == True :
                communicate = False
                appendix += "\n"
                enter_count += 1
                
            if s in en and communicate == False and str_count > 5 and result[-1] not in number and result[-1] not in en :
                str_count = 0
                appendix += "\n"
                enter_count += 1
                
            if enter_count > 3 :
                enter_count = 0
                appendix += "\n"
                
            result = result + appendix
        
        with open(filename.split(".")[0] + "_reshape.txt", 'w', encoding = 'utf-8') as f :
            f.write(result)
        
        
        

main()
