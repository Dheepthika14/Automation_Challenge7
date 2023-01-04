Str1 = "adcedf"
Str2 = "edf"

Str1_Len = len(Str1)
Str2_Len = len(Str2)

Match = False

if Str2_Len > Str1_Len:
    print("String 2 length is greater than String 1, so will not be able to convert")
else:
    for i in range(0, Str1_Len):
        prefixstr = Str1[i:i + Str2_Len]
        if prefixstr == Str2 and (Str1.index(prefixstr) == 0):
            Match = True
            print("Yes can be converted by removing : " + Str1[Str2_Len:] + ", to get : " + Str2)
        elif prefixstr == Str2 and (Str1.index(prefixstr) == Str1_Len - Str2_Len):
            Match = True
            print("Yes can be converted by removing : " + Str1[:Str1.index(prefixstr)] + ", to get : " + Str2)

    if Match is False:
        print("No, cannot be converted")
