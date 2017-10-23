def my_print(phrase):
    f = open("debug", 'a')
    print(phrase, file=f)
    f.close()
    
    
