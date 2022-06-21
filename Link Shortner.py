import pyshorteners

def short():
    link = input("\nEnter your link : ")
    y = ['http:', 'www.', 'https:']
    if any(z in link for z in y):
        try:
            shorts = pyshorteners.Shortener()
            x = shorts.tinyurl.short(link)
        except:
            return False
        else:
            print("\nShorted link is : " + x)
    else:
        return False


while short() is False:
    print('Try again:')
