"""
author : adel.beghdadi@edu.esiee.fr
"""

def ispalindrome(p):
    """
    Test si une chaîne de caractère est un palindrome ou non. 
    Renvoi vrai si c'est le cas, faux sinon. Test aussi les phrases complexes.

    Args:
        p: Chaîne de caractères

    Returns:
        ispalindrome(p): True or False 
    """
    p = p.lower()
    d = str.maketrans("âàäçéèêëeîïôöùûüÿ","aaaceeeeeiioouuuy"," '-_,;.?:/!%")
    p = p.translate(d)
    if p != p[::-1]:
        return False
    return True

def main():
    """
    Fonction principale qui va tester une liste de mot pour déterminer lesquels sont des palindromes

    Args: 

    Returns:
        main() : Null
    """
    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))

if __name__ == "__main__":
    main()
