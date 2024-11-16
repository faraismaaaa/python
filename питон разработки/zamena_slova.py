# замена слова с помощью word if word 
list_A = ['hello', 'world', 'goodbye']
list_B = [word if word != 'world' else 'friend' for word in list_A]
print(list_A)
print(list_B)
