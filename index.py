print('Welcome to this simple converter: ')

celcius = int(input('Celsius: '))

def conv(c):
    # Tu código aquí:
    return 9/5*c+32

fahrenheit = conv(celcius)
print('Fahrenheit: ', fahrenheit)
