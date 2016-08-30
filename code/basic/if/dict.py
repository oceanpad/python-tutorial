d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}

try:
    print(d['Michael'])
    print(d.get('Thomas')) # key not exsit, 
    print(d['xxxxxxx'])
except KeyError:
    print('Error: Key is not exsit')

for k,v in d.items() :
    print (k ,':', v)
