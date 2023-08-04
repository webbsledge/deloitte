# reading files
f1 = open("/Users/sledge/Desktop/folder1.rtf", "r") 
f2 = open("/Users/sledge/Desktop/folder2.rtf", "r") 
 
f1_data = f1.readlines()
f2_data = f2.readlines()
 
i = 0
 
for line1 in f1_data:
    i += 1
     
    for line2 in f2_data:
         
        # matching line1 from both files
        if line1 == line2: 
            # print IDENTICAL if similar
            print("Line ", i, ": IDENTICAL")      
        else:
            print("Line ", i, ":")
            # else print that line from both files
            print("\tFile 1:", line1, end='')
            print("\tFile 2:", line2, end='')
        break
 
# closing files
f1.close()                                      
f2.close()   