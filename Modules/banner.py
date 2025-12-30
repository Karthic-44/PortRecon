def banner():
    RED = "\33[91m"
    RESET = "\033[0m"

    text = f"""
            {RED}        
            _               __                       
            |_) _  ._ _|_   (_   _  _. ._  ._   _  ._ 
            |  (_) |   |_   __) (_ (_| | | | | (/_ |       

            {RESET}                               
            """
    
    print(text + "\n\n")