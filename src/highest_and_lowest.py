def high_and_low(numbers):
    hilo = [int(n) for n in numbers.split(' ')]
    return str(max(hilo)) + ' ' + str(min(hilo))
