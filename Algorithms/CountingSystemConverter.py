def convert_dec_to_base(number: int, base: int):
    """
    The function uses Horner's scheme to convert numbers in Decimal counting system to a counting system of a given base
    (up to hexadecimal)
    :param number: the given integer
    :param base: the base to convert given integer to
    :return: a number of given base
    """
    remainders = []
    hex_dict = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    while number > 0:
        tail = number % base
        if 10 < base <= 16:
            if tail > 9:
                tail = hex_dict[tail]
        remainders.append(str(tail))
        number //= base
    if number > 0:
        remainders.append(str(number))
    result = ''.join(remainders[::-1])
    return result


def convert_base_to_dec(number, base: int) -> int:
    """
    The function converts numbers in given counting system (up to hexadecimal) to Decimal counting system
    :param number: the given number
    :param base: the base of given integer
    :return: an integer of Decimal base
    """
    number_reversed_list = list(str(number))[::-1]
    result = 0
    hex_dict = {'A': '10', 'B': '11', 'C': '12', 'D': '13', 'E': '14', 'F': '15'}
    for position, num in enumerate(number_reversed_list):
        try:
            num = int(num)
        except ValueError:
            num = int(hex_dict[num])
        result += int(num) * base ** position
    return result


print(convert_dec_to_base(44415, 16))
print(convert_dec_to_base(194, 5))
print(convert_base_to_dec(11001, 2))
print(convert_dec_to_base(convert_base_to_dec(25, 8), 2))
