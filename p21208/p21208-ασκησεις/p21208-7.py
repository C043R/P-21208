import json
from numpy import append

class colors:
    green = "\033[32m"
    cyan = "\033[36m"
    red = "\033[31m"

with open('dict.txt', 'r') as file:
    lines = [json.loads(i) for i in file.readlines()] # reads each line of the dict file
keys = lines[0].keys() # finds keys 

keys_list = []

for key in lines[0].keys():
    keys_list.append(key)
print(keys_list)  # append and prints all keys into key_list 

option = input(colors.green+"[+] Enter a key from the ones present above > ")

flag = False  # we use flags to check if the input value exists if not it exits 

for i in keys_list: 

    if i == option: 
        flag = True         

if flag == True:
    print(colors.cyan+"[!] Key exists , continuing ...") 
    second_list = [] 

    for i in lines: 
        second_list.append(i[option])
    maximum = max(second_list)   
    minimum = min(second_list)

    def most_frequent(second_list):
        return max(set(second_list), key = second_list.count)  # def to find max value of second_list 

    print("[+] Most popular value :" , most_frequent(second_list))
    print("[+] Minimum value :" , minimum)
    print("[+] Maximum value :" , maximum)
    # printing most popular , min , max 


else: 
    print(colors.red+"[!] Key does not exist , exiting ...")
    exit(0)



    

