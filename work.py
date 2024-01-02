file_handler = open('file1.txt','+r')
filename = file_handler.read()
encrypted_text = ""
#encrypted text should save in this given empty string


for i in filename:
        num_value = ord(i) - 96
        encrypted_text += str(num_value)+ ' '
print('TOP SECRET INFORMATION: CODE RED')
print(f"encrypted result:{encrypted_text}")
#iterate each character from text to i
#make the character to corresponding numeric value by substract ascii value of each character by grave accent
#add that value to empty encrypted text by using str to covert numbers to string


value = encrypted_text.split()
descrypted_text = ""
#discrypted text should save in this given empty string
for j in value:
    char_value = chr(int(j) +96)
    descrypted_text += char_value
print(f"descrypted result:{descrypted_text}")
#iterate each character from encrypted_text to j
#descrypte by adding that encrypted characted with grave accent and convert that numerics to character by using chr function
#add that value to empty descrypted text.



secret_code = "12 15 16 19 9 3 20 9 15 14 1 18 5 12 20 9 15 14 6 18 15 14 20 7 18 1 13 5 19 1 20 5 20 5 14 20 9 14 6 9 20 9 15 14 19 21 9 19 3 15 13 9 14 7 5 14 20 18 1 9 12 12 9 14 7 3 8 5 13 9 3 8 1 13 13 5 14 20 4 5 19 3 15 13 16 12 1 13 1 20 9 15 14 19 1 20 18 5 4"
secret_code_split = secret_code.split()
descrypted_code_of_secret_info = ""

for k in secret_code_split:
    char_value = chr(int(k)+96)
    descrypted_code_of_secret_info += char_value
    
print(f"descript code for secret_info: {descrypted_code_of_secret_info}")