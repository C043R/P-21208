class colors:
    green = "\033[32m"
    cyan = "\033[36m"

with open('yourfile.txt', 'r') as f: 
    cont = f.read() # opening file and declaring its contents as "cont"

def convert(text):
    global whole_binary
    whole_binary = ''

    for i in range(len(cont)):  
        binary = ''
        ord_txt = ord(cont[i:i+1])  
 
        while ord_txt > 0: 

            var = ord_txt % 2  # Mod for 0 & 1 
            ord_txt = ord_txt // 2    # dividing without remainer 
            binary = str(var) + str(binary)  
        whole_binary += binary 

    print("[+] Binary output : "+colors.green+whole_binary) 

convert(cont) # calling the function to convert cont into binary 
    
def max_0(whole_binary):
    return max(map(len, whole_binary.split("1")))

print(colors.cyan+f"Maximum length of consecutive 0's : {max_0(whole_binary)}") # max 1 (splits 0's to find max sequence of 1's )

def max_1(whole_binary):
    return max(map(len, whole_binary.split("0")))

print(colors.cyan+f"Maximum length of consecutive 1's : {max_1(whole_binary)}") # max 0 ( splits 1's to find max sequence of 0's)
