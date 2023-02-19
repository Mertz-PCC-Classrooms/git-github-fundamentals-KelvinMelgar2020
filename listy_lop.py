

if __name__ == "__main__":
    
    food = ['rice', 'beans']
    
    food.append('broccoli ')
    print(food)
    
    food.extend(['bread', 'pizza']) 
    #~ ().extend) s used to add Multiple elements to a list.
    print(food)
    print(food[:2])
    print(food[-1]) #^ to print the last value in the list.
    
    breakfast = "egs, fruit, orangejuice".split(',')
    #^ to convert a string into a list I used the split() method
    print(breakfast)
    print(len(breakfast))
    
    
    # entry =[]
    # user_input = input('Enter a floating point value or stop: ')
    
   # I tried but I could not do it.
