import sys
# AitJqT6V97gZae
#python decrypt output parolamea2021 input_recuperat.txt

fisier1, fisier2 = sys.argv[1:] 

def decriptare(text_input, text_output):
    for i in range(len(text_input)):
        text_input = (text_input[:i] + chr(ord(text_input[i]) ^ ord(text_output[i % len(text_output)])) + text_input[i + 1:])
    return text_input

file1 = open(fisier1,"rb")
file2 = open(fisier2, "r")

text = file1.read()
text_output = file2.read()

text = text.decode("utf-8")

file1.close()
file2.close()

cracked_pass = decriptare(text,text_output)

for i in range(10,15):
    if cracked_pass[0:i] == cracked_pass[i:i*2]:
        print(f"Parola este: {cracked_pass[0:i]}")
        break


