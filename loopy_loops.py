if __name__ == "__main__":
    
    pokemon = ('pikachu', 'charmander', 'bulbasaur')
    print(pokemon[1])
    print('script complete')
    
    starter1, starter2, starter3 = pokemon
    
    my_name = (tuple('Kelvin'))
    print('i' in my_name)
    print('script complete')
    
    for i in range(2,11):
        print(i)
    print('script complete')    
    i = 2
    while i <= 10:
        print(i)
        i += 1
    print('script complete')
    
    for k in("This is a  simple string"):
        print(k)
    print('script complete')
    
    again_again =('This ', 'is ', 'a ', 'simple ', 'set')
    for words in again_again:
        for i in range(3):
            print(words)
    print('script complete')