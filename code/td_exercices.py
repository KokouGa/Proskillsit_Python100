""" Un palindrome est un mot qui se lit de la même façon de 
gauche à droite et de droite à gauche."""

def est_un_palindrome(mot):
    """Retourne True si mot est un palindrome, False sinon."""
    # On peut inverser une chaîne de caractères en utilisant la syntaxe suivante :
    # mot_inverse = mot[::-1]
    # Par exemple, "bonjour"[::-1] retourne "ruojnob"
    mot_inverse = mot[::-1]
    
    if mot == mot_inverse:
        return True
    
    return False


mot1 = "Gawonou"
print(mot1[::-1])

