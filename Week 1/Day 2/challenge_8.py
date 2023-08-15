the_string = 'jrfndklhgfndjkjlkgperfijfhdknsadcvjhiiohjfkledsopiuhgtyujwsdxcvhgfdjhiopiwquhejkdsoiufghedjwshi'

letter = ''
for i in range(1,len(the_string)):
    letter = the_string[-i]               
    if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        print(letter)
        break;
