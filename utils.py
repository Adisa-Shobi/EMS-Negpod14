from tabulate import tabulate

welcome_message =\
'''                                                                                                  
I8,        8        ,8I              88                                                           
`8b       d8b       d8'              88                                                           
 "8,     ,8"8,     ,8"               88                                                           
  Y8     8P Y8     8P     ,adPPYba,  88   ,adPPYba,   ,adPPYba,   88,dPYba,,adPYba,    ,adPPYba,  
  `8b   d8' `8b   d8'    a8P_____88  88  a8"     ""  a8"     "8a  88P'   "88"    "8a  a8P_____88  
   `8a a8'   `8a a8'     8PP"""""""  88  8b          8b       d8  88      88      88  8PP"""""""  
    `8a8'     `8a8'      "8b,   ,aa  88  "8a,   ,aa  "8a,   ,a8"  88      88      88  "8b,   ,aa  
     `8'       `8'        `"Ybbd8"'  88   `"Ybbd8"'   `"YbbdP"'   88      88      88   `"Ybbd8"'  
                                                                                                  
                                                                                                  
'''
winner =\
'''oooooo   oooooo     oooo ooooo ooooo      ooo ooooo      ooo oooooooooooo ooooooooo.   
 `888.    `888.     .8'  `888' `888b.     `8' `888b.     `8' `888'     `8 `888   `Y88. 
  `888.   .8888.   .8'    888   8 `88b.    8   8 `88b.    8   888          888   .d88' 
   `888  .8'`888. .8'     888   8   `88b.  8   8   `88b.  8   888oooo8     888ooo88P'  
    `888.8'  `888.8'      888   8     `88b.8   8     `88b.8   888    "     888`88b.    
     `888'    `888'       888   8       `888   8       `888   888       o  888  `88b.  
      `8'      `8'       o888o o8o        `8  o8o        `8  o888ooooood8 o888o  o888o 
                                                                                       
                                                                                       
                                                                                       
'''
session_summary = "*" * 35 + "SESSION SUMMARY" + "*" * 35 + "\n"
session_summary_end = "*" * 85 + "\n"
successful_vote = \
"-------------------------------\n|                               |\n|                               |\n|       Vote Successful         |\n|                               |\n|                               |\n--------------------------------"

def print_boxed_text_with_spacing(text):
    border = "+" + "-" * (len(text) + 2) + "+"
    content = "| " + text + " |"
    
    # Add empty lines above and below the content
    empty_line = "|" + " " * (len(text) + 2) + "|"

    print(border)
    print(empty_line)
    print(content)
    print(empty_line)
    print(border)

def print_bar_chart(data):
    max_value = max(data.values())
    scale_factor = 40 / max_value  # Adjust this value for scaling

    print("Contestant results:")

    for label, value in data.items():
        scaled_value = int(value * scale_factor)
        bar = "#" * scaled_value
        print(f"{label:10}: {bar}")

def print_table(data, headers=None, tablefmt="grid"):
    if headers is not None:
        table = tabulate(data, headers=headers, tablefmt=tablefmt)
    else:
        table = tabulate(data, tablefmt=tablefmt)
    print(table)
