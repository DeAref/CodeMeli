code=input("enter code meli \n")
code = str(code)
if len(code)==8:
    code="00"+code
    print(code)

if len(code)==9:
    code="0"+code
    print(code)
if len(code)==10:
    x=[int(code[0])*10,int(code[1])*9,int(code[2])*8,int(code[3])*7,int(code[4])*6,int(code[5])*5,int(code[6])*4,int(code[7])*3,int(code[8])*2]
    end=(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7]+x[8])%11
    if (end == int(code[9])) or ((11-end) == int(code[-1])):
        print("code meli motabar ast")
    else:
        print("code meli is not correct...")
        
        # ArefSS https://t.me/DeAref
