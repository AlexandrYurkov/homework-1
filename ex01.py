def domain_name(url):
    if '/' in url:
        tmp = (''.join(url.split('/')[2]))
        if 'w' in (''.join(tmp.split('.')[0])):
            result = (''.join(tmp.split('.')[1]))
        else:
            result = (''.join(tmp.split('.')[0]))
    else:
        tmp = (''.join(url.split('.')[1]))
        if 'w' in (''.join(tmp.split('.')[0])):
            result = (''.join(tmp.split('.')[1]))
        else:
            result = (''.join(tmp.split('.')[0]))
    return result
