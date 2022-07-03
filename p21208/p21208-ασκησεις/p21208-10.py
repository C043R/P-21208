class colors:
    cyan = "\033[36m"

with open('yourfile.txt', 'r') as f:
    cont = f.read()

def convert(text):
    global whole_binary
    whole_binary = ''

    for i in range(len(cont)):  
        binary = ''
        ord_txt = ord(cont[i:i+1])  
 
        while ord_txt > 0: 

            var = ord_txt % 2  # MOD 
            ord_txt = ord_txt // 2 # no remainer   
            binary = str(var) + str(binary)  
        whole_binary += binary 

    global split
    n = 7 # after we convert txt to binary we set length 7 
    split = [whole_binary[i:i+n] for i in range(0, len(whole_binary), n)] 
    
convert(cont)

def firstTwoLastTwo(split):
    return [(x[:2], x[-2:]) for x in split] # extract first and last 2 digits from split list 

def add(split):
    return [(x[:2]+x[-2:]) for x in split] # adds the first and last 2  

four_bit = add(split)
sixteen_bit = [''.join(x) for x in zip(four_bit[::4], four_bit[1::4], four_bit[2::4], four_bit[3::3])] # combining all 4 bit values to 16 bit values in cells of sixteen_bit list . 


count_two = 0
count_three = 0 
count_five = 0 
count_seven = 0 
# counter variables 

for i in range(len(sixteen_bit)):
    sixteen_bit[i] = (int(sixteen_bit[i],2))

for i in range(len(sixteen_bit)): # looping through every cell of the list to find percentages with counter
    if sixteen_bit[i] % 2 == 0:
        count_two+=1
    if sixteen_bit[i] % 3 == 0:
        count_three +=1
    if sixteen_bit[i] % 5 == 0:
        count_five +=1
    if sixteen_bit[i] % 7 == 0:
       count_seven +=1

# printing percentages 

percentage = count_two / len(sixteen_bit)
print(colors.cyan+f"[+] Ποσοστό που διαρείται με το 2: {percentage*100} %")  

percentage = count_three / len(sixteen_bit)
print(colors.cyan+f"[+] Ποσοστό που διαρείται με το 3 : {percentage*100} %")

percentage = count_five / len(sixteen_bit)
print(colors.cyan+f"[+] Ποσοστό που διαρείται με το 5 : {percentage*100} %")

percentage = count_seven / len(sixteen_bit)
print(colors.cyan+f"[+] Ποσοστό που διαρείται με το 7 : {percentage*100} %")
