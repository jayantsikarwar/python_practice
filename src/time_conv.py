def time_conv(t):
    if 'H' in t and 'M' in t :
        y=int(t.split('PT')[1].split('H')[0])*60 + int(t.split('PT')[1].split('H')[1].split('M')[0])
    elif 'H' in t :
        y=int(t.split('PT')[1].split('H')[0])*60
    elif 'M' in t :
        y=int(t.split('PT')[1].split('H')[0].split('M')[0])
    else :
        y=0
    return y