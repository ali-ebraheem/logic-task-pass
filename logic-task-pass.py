
#Q1/Write a method that will remove any given character from a String?
str = "Engineering"
print ("Original string: " + str) 
result = str.replace('e', '') 
# removes all occurrences
print ("The string after removal of character: " + result) 
# Removing 1st occurrence
result = str.replace('e', '', 1) 
print ("The string after removal of character: " + result) 



#Q2/Write a program to find all prime numbers up to a given range of numbers?
lower_value = 1
upper_value = 8
for number in range (lower_value, upper_value + 1):  
    if number > 1:  
        for i in range (2, number):  
            if (number % i) == 0:  
                break  
        else:  
            print (number)
            
            

#Q3/write a function that count how many the given character repeated in a given string? 
def count_char(test_str,char):
    count = 0
    for i in test_str:
         if i == char:
             count = count + 1
    print(count)         
count_char("elee",'e')             
             