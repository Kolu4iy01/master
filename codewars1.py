def normalize_url(url):
    x = 'https://'
    index = url.find('//')
    if index == -1:
        return x + url
    else:
        [x1, x2] = url.split('//')
        return x + x2



def who_is_this_house_to_starks(name):
    if name == 'Karstark' or name == 'Tully':
        return ('friend')
    elif name == 'Lannister' or name == 'Frey':
        return ('enemy')
    else :
        return ('neutral')

   
