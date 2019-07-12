list1 = []                                      #declare input list
list2 = []                                      #declare output list
num = int(input("Input number of elements: "))  #user input to declare number of elements

#loop to develop input list

for i in range(0, num):
    elem = int(input("Element: "))              #user input elements to the list
    list1.append(elem)

print("Final list: ", list1)                    #display final input list

#nested loops to perform the comparisons of the condition

for i in range(len(list1)):
    for j in range(i, len(list1)):
        if ((list1[i]*list1[j]) % 2 == 0) and ((list1[i]+list1[j]) % 2 == 1):
            list2.append((list1[i], list1[j]))

print("Output the computed list: ",list2)        #output the list of pairs

