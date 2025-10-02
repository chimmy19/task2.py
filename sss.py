
temp = int(input('What is the temperature today: '))

if temp >= 30:
    print('Its a hot day, stay hydrated...')
elif 20 <= temp <= 29:
    print('Its a warm day, enjoy your day')
elif 10 <= temp <= 19:
    print('Its a cool day, wear a jacket')
else:
    print('Its a cold day, stay warm')
