def greet(lang):
    """This function is for printing a greeting in some
    selected languages: Spanish, Swedish, and German"""
    if lang == 'es':
        return 'Hola'
    elif lang == 'ge':
        return 'Hallo'
    elif lang == 'sv':
        return 'Halla'
    else:
        return 'Hello'


greet('sv')

help(greet)
