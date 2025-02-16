import math

def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n))+1):
            if n%i == 0:
                return False
        else:
            return True

def find(string, letter):
    count = 0
    for i in string:
        if i == letter:
            return count
        else:
            count += 1
    else:
        return None

def encrypt(text, shift, row):
    # 62 + shift must be a prime
    
    charset = "*"*shift + "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.,:;'!-?# "
    prime = shift + 62
    
    if is_prime(prime) == False or row >= prime:
        return "Error"
    
    charset_modified = list("$"*prime)
    
    for i in range(prime):
        new_index = (i*row) % prime
        charset_modified[new_index] = charset[i]
        
    charset_modified = str(charset_modified)
    encrypted_text = [shift, row]
    
    for letter in text:
        if letter == "\n":
            encrypted_text.append(find(charset_modified, "#"))
        else:
            encrypted_text.append(find(charset_modified, letter))
        
    return encrypted_text

def decrypt(encrypted_text):
    shift = encrypted_text[0]
    row = encrypted_text[1]
    
    charset = "*"*shift + "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz.,:;‘!-?# "
    prime = shift + 62
    
    if is_prime(prime) == False:
        return "Error"
    
    charset_modified = list("$"*len(charset))
    
    for i in range(len(charset)):
        new_index = i*row % prime
        charset_modified[new_index] = charset[i]
        
    charset_modified = str(charset_modified)
    
    decrypted_text = ""
    
    for i in range(2, len(encrypted_text)):
        index = encrypted_text[i]
        if charset_modified[index] == "#":
            print(decrypted_text)
            decrypted_text = ""
        else:
            decrypted_text += charset_modified[index]
    
    if decrypted_text != "":
        print(decrypted_text)
