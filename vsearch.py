
def search4vowels(phrase:str)->set:
    """dispalying vowels found in a supplied phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

#prompt = input('enter any word to search for vowels: ')
#print(search4vowels(prompt))


def search4letter(phrase:str, letters:str='aeiou')->set:
    """displaying a set of supplied letter from a supplied phrase"""
    return set(letters).intersection(set(phrase))
