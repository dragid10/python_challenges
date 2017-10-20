numDict = {0 : 'zero', 1 : 'one', 2 : 'two', 3 : 'three', 4 : 'four' ,
           5 : 'five', 6 : 'six', 7 : 'seven', 8 : 'eight', 9 : 'nine',
           10 : 'ten', 11 : 'eleven', 12 : 'twelve', 13 : 'thirteen',
           14 : 'fourteen', 15 : 'fifteen', 16 : 'sixteen', 17 : 'seventeen',
           18 : 'eighteen', 19 : 'nineteen', 20 : 'twenty', 30 : 'thirty',
           40 : 'forty', 50 : 'fifty', 60 : 'sixty', 70 : 'seventy',
           80 : 'eighty', 90 : 'ninety'}

def toWord(num, recurse = False):
    result = ''
    if num == 0 and not recurse:
        result = numDict[num]
    elif num >= 1 and num <= 19:
        result = numDict[num]
    elif num >= 20 and num <= 99:
        result = numDict[num // 10 * 10] + ' ' + toWord(num % 10, True)
    elif num >= 100 and num <= 999:
        result = numDict[num // 100] + ' hundred ' + toWord(num % 100, True)
    elif num >= 1000 and num <= 999999:
        result = toWord(num  // 1000) + ' thousand ' + toWord(num % 1000, True)
    elif num >= 1000000 and num <= 999999999:
        result = toWord(num // 1000000) + ' million ' + toWord(num % 1000000, True)
    elif num >= 1000000000 and num <= 999999999999:
        result = toWord(num // 1000000000) + ' billion ' +\
               toWord(num % 1000000000, True)
    elif num >= 1000000000000 and num <= 999999999999999:
        result = toWord(num // 1000000000000) + ' trillion ' +\
               toWord(num % 1000000000000, True)
    return result.strip()
    
def toMoney(num):
    cents = toWord(int(round(num % 1,2) // .01))
    if cents == 'one':
        cents += ' cent'
    else:
        cents += ' cents'
    
    dollars = toWord(int(num))
    if dollars == 'one':
        dollars += ' dollar and '
    else:
        dollars += ' dollars and '
    
    return dollars + cents
