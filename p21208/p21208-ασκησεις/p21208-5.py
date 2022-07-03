from collections import Counter

class colors:
    green = "\033[32m"
    blue = "\033[34m"
    cyan = "\033[36m"

with open('yourfile.txt', 'r') as f:
    cont = f.read()
    peza = cont.lower() # lowering each word of file 
    print(colors.green+"[+] Text converted to lowercase .")
    split = peza.split()  
    Counter = Counter(split) 
    occurrences = Counter.most_common(10) # using collections counter 
    print(colors.blue+"[+] Top 10 most popular words:", occurrences) 

    cont_list = cont.replace('\n', '').split(".") # removing "" from cont_list 
    for i in range(len(cont_list)):
        cont_list[i] = cont_list[i].lower() # lowering every item in list 

    two_letters = [] 
    def most_common(two_letters):
        return max(set(two_letters), key=two_letters.count) # returning max 

    for item in cont_list:
        two_letters.append(item[:2]) # writing to list the first 2 letters  
        while("" in two_letters):
            two_letters.remove("") # removing "" from two_letters list 
            two_letters = two_letters[:2] # getting only the first 2 cells of list 
    print(colors.cyan+f"[+] 3 most common combination of the first 2 letters {two_letters}")

    three_letters = [] 

    def most_common(three_letters):
        return max(set(three_letters), key=three_letters.count)

    for item in cont_list:
        three_letters.append(item[:3]) # writing to list the first 3 letters 
        while("" in three_letters) :
            three_letters.remove("") # removing "" from three_letters list 
            three_letters = three_letters[:3] # getting only the first 3 cells of list 
    print(colors.cyan+f"[+] 3 most common combination of the first 3 letters {three_letters}") 


