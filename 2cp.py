str=input()
new_str=list(str)
new_str.reverse()
str_join="".join(new_str)
if(str==str_join):
    print("Yes")
else:
    print("No")