
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

f = open('../../tmp/workfile', 'w')
f.write("aoligei")

with open('workfile') as f:
    read_data = f.read()
    print(read_data)

print(f.closed)
