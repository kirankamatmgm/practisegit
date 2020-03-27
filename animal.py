import sys

def default():
    print('hello kiran')

def dog():
    print('Bow Bow!!!')

def main():
    if sys.argv[1] == 'dog':
        dog()
    else:
        default()

if __name__=='__main__':
    main()
