def my_print(phrase):
    f = open("debug", 'w')
    print(phrase, file=f)
    f.close()
    
    
