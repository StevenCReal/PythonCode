week = {
    'm': 'Monday',
    'f': 'Friday',
    't': {
        'u': 'Tuesday',
        'h': 'Thursday'
    },
    's': {
        'a': 'Saturday',
        'u': 'Sunday'
    }
}
a = week[input('Enter first character:').lower()]
if a == week['t'] or a == week['s']:
    print(a[input('Enter second character:').lower()])
else:
    print(a)
