def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    middle = len(aStr) // 2
    if len(aStr) != 0:
        if (aStr) == 1:
            return char == aStr
        else:
            if char == aStr[middle]:
               return True
            elif char > aStr[middle]:
                return isIn(char, aStr[middle + 1:])
            else:
                return isIn(char, aStr[:middle])
    else:
        return False

Str = "abcdefgh"
print(isIn('z', Str))

