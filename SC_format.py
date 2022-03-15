
import base64
import os
import sys

#The commented one is bash script to convert shellcode into raw binary formate. 
#You just need to change the input file and then run second command to convert into binary form.
#This script will run on linux distributions.
#Commented script will convert C format shellcode into raw form and if you want to convert C# shellcode into raw just follow two simple steps.
#STEP1 ----> Replace '0x' with ''
#STEP2 ----> Replace ',' with ''
#Now Run just second command.....................
"""
#!/bin/bash
echo "[>] Parsing Input File"
cat $INPUT |grep '"' |tr -d " " |tr -d "\n" |sed 's/[\"x.;(){}]//g' >> Parsed.txt
echo "[>] Pipe output to xxd"
xxd -r -p Parsed.txt Converted.bin
echo "[>] Clean up"
echo "[>] Done!!"

"""
#Now this part of code will convert raw form of shellcode into C,C#,Base64 form. 
#Just run the code and give binary file as an input.


INPUT_FILE = sys.argv[1]
try:
    with open(INPUT_FILE, 'rb') as shellcode:
         shell_D = shellcode.read()
except:
     print("File argument needed! %s <raw payload file>" % sys.argv[0])

shell_coded = ''
for byte in shell_D:
    shell_coded += "\\x" + hex(byte)[2:].zfill(2)

C_Sharp = "0" + ",0".join(shell_coded.split("\\")[1:])

encode = base64.b64encode(C_Sharp.encode())

with open('All_TYEPES_SHELLCODES.txt', 'w') as format_out:
    format_out.write("\n\nC shellcode format:\n\n")
    format_out.write(shell_coded)
    format_out.write("\n\nC# format shellcode:\n\n")
    format_out.write(C_Sharp)
    format_out.write("\n\nBase64 Encoded shellcode:\n\n")
    format_out.write(encode.decode('ascii'))
    format_out.write("\n")