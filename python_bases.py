# def my_div(a, b):
#     return a / b


# try:
#     print(my_div(6, 0))
#     print('15')
# => Attrape seulement exception de type zero division
# except ZeroDivisionError:
#     print('Erreur attrapée!')


# print('Partie du programme super importante')

class GeminiError(Exception):
    pass

def boite_a_erreurs(value):
    if type(value) == int:
        raise TypeError('Ceci est une type error personnalisée')

    if value == 'grok':
        raise ValueError("Grok c'est nul")

    if value == 'key':
        raise KeyError('Nice')

    if value == 'gemini':
        raise GeminiError('GEMINIIIII')

    

# boite_a_erreurs('grok')

# boite_a_erreurs('gemini')

# try:
#     boite_a_erreurs('gemini')
# except ValueError:
#     print('GROK STOP')
# except TypeError:
#     print('Pas le bon type')
# except GeminiError:
#     print('gemini flemme')
# except:
#     print('Erreur inconnue')

try:
    boite_a_erreurs('hello')
    print('ouverture fichier ex...')
except (TypeError, ValueError) as e:
    print(e)
    print('Nettoyage specifique à cette erreurs la')
except GeminiError as e:
    print(e)
    print("Nettoyage un peu plus car c'est GEMINI")
except Exception as e:
    print(e)
    print('Nettoyage AUTRE')


def demo_finally(string):
    try:
        boite_a_erreurs(string)
        print('ouverture fichier ex...')
        return 'Hello'
    except (TypeError, ValueError) as e:
        print(e)
        print('Nettoyage specifique à cette erreurs la')
        return 'erreur 1'
    except GeminiError as e:
        print(e)
        print("Nettoyage un peu plus car c'est GEMINI")
        return 'erreur 2'
    except Exception as e:
        print(e)
        print('Nettoyage AUTRE')
        return 'erreur 3'
    finally:
        print('fermeture du fichier')
    # print('fermeture du fichier') => Lui ne sera jamais executé sans finally

demo_finally('grok')
