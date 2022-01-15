import penguinbullet, colorama
print(colorama.Back.WHITE+colorama.Fore.BLACK+"""
  _____                       _                                         
 |  __ \                     (_)                                        
 | |__) |__ _ __   __ _ _   _ _ _ __                                    
 |  ___/ _ \ '_ \ / _` | | | | | '_ \                                   
 | |  |  __/ | | | (_| | |_| | | | | |                                  
 |_|   \___|_| |_|\__, |\__,_|_|_| |_|                                  
  ____        _ _  __/ |                                                
 |  _ \      | | ||___/ |                                               
 | |_) |_   _| | | ___| |_                                              
 |  _ <| | | | | |/ _ \ __|                                             
 | |_) | |_| | | |  __/ |_                                              
 |____/ \__,_|_|_|\___|\__|                                             
                                                                        """
+colorama.Fore.BLUE+
"""
 +--^----------,--------,-----,--------^-,                              
 | |||||||||   `--------'     |          O                              
 `+---------------------------^----------|                              
   `\_,---------,---------,--------------'                              
     / XXXXXX /'|       /'                                              
    / XXXXXX /  `\    /'                                                
   / XXXXXX /`-------'                                                  
  / XXXXXX /                                                            
 / XXXXXX /                                                             
(________(                                                              
 `------'                                                               """)
print(colorama.Style.RESET_ALL)
while True:
    text = input(">>> ")
    if text == "clear":
        penguinbullet.clear()
    else:
        res, err = penguinbullet.run("<stdin>", text)
        if err: print(err.as_string())
        else: print(res)