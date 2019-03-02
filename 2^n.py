import sys
# print (sys.argv[0])
# for i in range(1, len(sys.argv)):
#     # print ("Parameter", sys.argv[i])
#     print ("Result:", 2**int(sys.argv[i]))


for i in range(1, len(sys.argv)):
    result = 1
    for j in range (0, int(sys.argv[i])):
        result = result * 2
    print ("Result:", result)
        
