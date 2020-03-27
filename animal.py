import sys

def cat():
    print('meow!!!')

def default():
    print('hello kiran')

def dog():
    print('Bow Bow!!!')

def main():
    if sys.argv[1]==' ':
        default()
    elif sys.argv[1]=='cat':
        cat()
    elif sys.argv[1] == 'dog':
        dog()
    else:
        default()

if __name__=='__main__':
    main()
