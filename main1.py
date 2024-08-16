# #   Ex1 - String 
# # Enter text and display it one by one
# text = input("Enter text: ")
# for i in text:
#     print(i)


text = "454639"
odd=0
even=0
for i in range(len(text)):
    if int(text[i]) % 2 == 0:
        even += 1
    elif int(text[i]) % 2 ==1:
        odd += 1
print( even)
print( odd)
















