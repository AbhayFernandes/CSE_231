import unittest
from proj09 import fill_completions, find_completions, read_file

class MasterTest(unittest.TestCase):
    def test_fill_completions(self):
        print("Testing using melody.txt.")
        words = {'tom', 'such', 'sun', 'tow', 'toot', 'suit', 'son', 'sofa', 'too', 'soffit', 'town', 'to'}

        instructorD = {(0, 't'): {'too', 'to', 'town', 'tow', 'toot', 'tom'}, (1, 'o'): {'too', 'sofa', 'to', 'soffit', 'town', 'tow', 'son', 'toot', 'tom'}, (2, 'o'): {'too', 'toot'}, (0, 's'): {'sofa', 'soffit', 'son', 'such', 'suit', 'sun'}, (2, 'f'): {'soffit', 'sofa'}, (3, 'a'): {'sofa'}, (3, 'f'): {'soffit'}, (4, 'i'): {'soffit'}, (5, 't'): {'soffit'}, (2, 'w'): {'town', 'tow'}, (3, 'n'): {'town'}, (2, 'n'): {'son', 'sun'}, (1, 'u'): {'such', 'suit', 'sun'}, (2, 'c'): {'such'}, (3, 'h'): {'such'}, (2, 'i'): {'suit'}, (3, 't'): {'toot', 'suit'}, (2, 'm'): {'tom'}}
        studentD = fill_completions(words)

        print("Instructor:")
        print(instructorD)
        print("Student:")
        print(studentD)
        assert studentD == instructorD

        print("-"*20)
        print("Testing using Indila.txt.")
        words= {'importance', 'et', 'dernière', 'recommence', 'avec', 'peur', 'trimer', \
                    'souffrance', 'pour', 'une', 'tu', 'cette', 'un', 'oh', 'ce', 'être', 'bruit', \
                        'jour', 'vie', 'douce', 'sur', 'décor', 'dans', 'oublier', 'toutes', 'du', \
                            'je', 'vent', 'recommences', 'revient', 'cours', 'la', 'immense', 'écoute', \
                                'remue', 'ciel', 'miel', 'veux', 'vide', 'ma', 'comme', 'en', 'ton', \
                                    'paris', 'chemin', 'tour', 'pluie', 'pourquoi', 'qui', 'le', \
                                        'offenses', 'métro', 'tout', 'douleur', 'danse', 'de', 'paro', \
                                            'indila', 'nuit', 'déambule', 'vole', 'seule', 'sens', 'monde', \
                                                'peu', 'sans', 'brille', 'cœur', 'les', 'que', 'lui', 'mon', \
                                                    'brin', 'toi', 'absence', 'enfant', 'suis', 'dont', 'est', 
                                                    'beau', 'peine', 'payé'}
            
        instructorD = {(0, 'i'): {'immense', 'indila', 'importance'}, (1, 'm'): {'immense', 'importance'}, (2, 'p'): {'importance'}, (3, 'o'): {'recommences', 'importance', 'recommence', 'décor', 'paro'}, (4, 'r'): {'décor', 'importance'}, (5, 't'): {'enfant', 'importance'}, (6, 'a'): {'souffrance', 'importance'}, (7, 'n'): {'souffrance', 'recommences', 'importance', 'recommence'}, (8, 'c'): {'souffrance', 'recommences', 'importance', 'recommence'}, (9, 'e'): {'souffrance', 'recommences', 'importance', 'recommence'}, (0, 'e'): {'enfant', 'et', 'est', 'en'}, (1, 't'): {'et', 'être'}, (0, 'd'): {'dont', 'danse', 'dernière', 'du', 'de', 'douce', 'décor', 'dans', 'déambule', 'douleur'}, (1, 'e'): {'recommence', 'dernière', 'seule', 'sens', 'peur', 'peu', 'je', 'vent', 'recommences', 'le', 'revient', 'les', 'cette', 'de', 'remue', 'ce', 'veux', 'beau', 'peine'}, (2, 'r'): {'dernière', 'sur', 'être', 'paro', 'paris'}, (3, 'n'): {'peine', 'dernière', 'brin'}, (4, 'i'): {'chemin', 'oublier', 'dernière'}, (5, 'è'): {'dernière'}, (6, 'r'): {'oublier', 'dernière', 'douleur'}, (7, 'e'): {'déambule', 'dernière'}, (0, 'r'): {'revient', 'recommences', 'remue', 'recommence'}, (2, 'c'): {'décor', 'recommences', 'recommence'}, (4, 'm'): {'recommences', 'recommence'}, (5, 'm'): {'recommences', 'recommence'}, (6, 'e'): {'immense', 'recommences', 'recommence', 'absence', 'offenses'}, (0, 'a'): {'avec', 'absence'}, (1, 'v'): {'avec'}, (2, 'e'): {'avec', 'miel', 'ciel', 'vie', 'que', 'une', 'chemin'}, (3, 'c'): {'avec', 'douce'}, (0, 'p'): {'peur', 'peu', 'pluie', 'peine', 'payé', 'paro', 'pour', 'paris', 'pourquoi'}, (2, 'u'): {'bruit', 'tout', 'douleur', 'seule', 'cœur', 'jour', 'peur', 'cours', 'peu', 'pluie', 'douce', 'souffrance', 'toutes', 'veux', 'pour', 'pourquoi', 'tour'}, (3, 'r'): {'cœur', 'cours', 'peur', 'jour', 'métro', 'pour', 'pourquoi', 'tour'}, (0, 't'): {'tout', 'toi', 'tu', 'trimer', 'toutes', 'ton', 'tour'}, (1, 'r'): {'brille', 'bruit', 'trimer', 'brin'}, (2, 'i'): {'toi', 'nuit', 'trimer', 'lui', 'peine', 'suis', 'brille', 'qui', 'brin'}, (3, 'm'): {'comme', 'déambule', 'chemin', 'trimer'}, (4, 'e'): {'danse', 'seule', 'revient', 'monde', 'remue', 'trimer', 'douce', 'pluie', 'cette', 'toutes', 'peine', 'comme', 'douleur'}, (5, 'r'): {'souffrance', 'trimer'}, (0, 's'): {'seule', 'sens', 'sur', 'souffrance', 'sans', 'suis'}, (1, 'o'): {'dont', 'vole', 'tout', 'douleur', 'jour', 'cours', 'monde', 'toi', 'douce', 'souffrance', 'toutes', 'comme', 'mon', 'pour', 'ton', 'pourquoi', 'tour'}, (3, 'f'): {'souffrance'}, (4, 'f'): {'souffrance'}, (0, 'u'): {'une', 'un'}, (1, 'n'): {'indila', 'un', 'enfant', 'en', 'une'}, (1, 'u'): {'du', 'nuit', 'tu', 'sur', 'suis', 'oublier', 'que', 'lui', 'qui'}, (0, 'c'): {'cœur', 'cours', 'ciel', 'cette', 'ce', 'comme', 'chemin'}, (2, 't'): {'est', 'cette', 'métro'}, (3, 't'): {'dont', 'nuit', 'vent', 'cette', 'toutes', 'tout'}, (0, 'o'): {'oublier', 'offenses', 'oh'}, (1, 'h'): {'oh', 'chemin'}, (0, 'ê'): {'être'}, (3, 'e'): {'immense', 'vole', 'absence', 'offenses', 'vide', 'être'}, (0, 'b'): {'brille', 'bruit', 'beau', 'brin'}, (3, 'i'): {'indila', 'bruit', 'revient', 'pluie', 'paris'}, (4, 't'): {'écoute', 'bruit'}, (0, 'j'): {'jour', 'je'}, (0, 'v'): {'vole', 'vie', 'vent', 'vide', 'veux'}, (1, 'i'): {'miel', 'vide', 'ciel', 'vie'}, (1, 'é'): {'décor', 'déambule', 'métro'}, (1, 'a'): {'danse', 'la', 'sans', 'dans', 'ma', 'payé', 'paro', 'paris'}, (2, 'n'): {'dont', 'danse', 'sens', 'monde', 'sans', 'dans', 'vent', 'mon', 'ton'}, (3, 's'): {'danse', 'sens', 'sans', 'dans', 'suis'}, (2, 'b'): {'oublier'}, (3, 'l'): {'seule', 'miel', 'ciel', 'oublier', 'brille', 'douleur'}, (5, 'e'): {'écoute', 'brille', 'oublier'}, (5, 's'): {'immense', 'offenses', 'toutes'}, (10, 's'): {'recommences'}, (2, 'v'): {'revient'}, (5, 'n'): {'revient', 'chemin'}, (6, 't'): {'revient'}, (4, 's'): {'cours', 'paris'}, (0, 'l'): {'la', 'les', 'lui', 'le'}, (2, 'm'): {'immense', 'comme', 'remue'}, (4, 'n'): {'immense', 'enfant', 'offenses', 'absence'}, (0, 'é'): {'écoute'}, (1, 'c'): {'écoute'}, (2, 'o'): {'écoute'}, (3, 'u'): {'écoute', 'beau', 'remue'}, (0, 'm'): {'monde', 'miel', 'métro', 'ma', 'mon'}, (3, 'x'): {'veux'}, (2, 'd'): {'indila', 'vide'}, (1, 'l'): {'pluie'}, (0, 'q'): {'que', 'qui'}, (4, 'q'): {'pourquoi'}, (5, 'u'): {'déambule', 'pourquoi', 'douleur'}, (6, 'o'): {'pourquoi'}, (7, 'i'): {'pourquoi'}, (1, 'f'): {'offenses'}, (2, 'f'): {'enfant', 'offenses'}, (7, 's'): {'offenses'}, (4, 'o'): {'métro'}, (4, 'l'): {'indila', 'brille'}, (5, 'a'): {'indila'}, (0, 'n'): {'nuit'}, (2, 'a'): {'déambule', 'beau'}, (4, 'b'): {'déambule'}, (6, 'l'): {'déambule'}, (2, 'l'): {'vole'}, (3, 'd'): {'monde'}, (1, 'œ'): {'cœur'}, (2, 's'): {'les', 'absence'}, (1, 'b'): {'absence'}, (5, 'c'): {'absence'}, (3, 'a'): {'enfant'}, (1, 's'): {'est'}, (2, 'y'): {'payé'}, (3, 'é'): {'payé'}}
            
        studentD = fill_completions(words)

        print("Instructor:")
        print(instructorD)
        print("Student:")
        print(studentD)
        assert studentD == instructorD

    def test_find_completions(self):
        word_dic = {(0, 't'): {'too', 'to', 'town', 'tow', 'toot', 'tom'}, (1, 'o'): {'too', 'sofa', 'to', 'soffit', 'town', 'tow', 'son', 'toot', 'tom'}, (2, 'o'): {'too', 'toot'}, (0, 's'): {'sofa', 'soffit', 'son', 'such', 'suit', 'sun'}, (2, 'f'): {'soffit', 'sofa'}, (3, 'a'): {'sofa'}, (3, 'f'): {'soffit'}, (4, 'i'): {'soffit'}, (5, 't'): {'soffit'}, (2, 'w'): {'town', 'tow'}, (3, 'n'): {'town'}, (2, 'n'): {'son', 'sun'}, (1, 'u'): {'such', 'suit', 'sun'}, (2, 'c'): {'such'}, (3, 'h'): {'such'}, (2, 'i'): {'suit'}, (3, 't'): {'toot', 'suit'}, (2, 'm'): {'tom'}}
        print("word_dic:")
        print(word_dic)
        print("-"*30)

        prefix = "so"
        print("prefix:",prefix)
        instructorSet = {'son', 'soffit', 'sofa'}
        studentSet = find_completions(prefix,word_dic)
        print("Instructor:")
        print(instructorSet)
        print("Student:")
        print(studentSet)

        assert studentSet == instructorSet

        print("-"*30)
        prefix = "too"
        print("prefix:",prefix)
        instructorSet = {'too', 'toot'}
        studentSet = find_completions(prefix,word_dic)
        print("Instructor:")
        print(instructorSet)
        print("Student:")
        print(studentSet)

        assert studentSet == instructorSet

        print("-"*30)
        prefix = "s"
        print("prefix:",prefix)
        instructorSet = {'sofa', 'soffit', 'son', 'such', 'suit', 'sun'}
        studentSet = find_completions(prefix,word_dic)
        print("Instructor:")
        print(instructorSet)
        print("Student:")
        print(studentSet)

    def test_read_file(self):
        fp = open("melody.txt",encoding="UTF-8")
        print("File melody.txt opened.")
        instructorD = {'tom', 'such', 'sun', 'tow', 'toot', 'suit', 'son', 'sofa', 'too', 'soffit', 'town', 'to'}
        print("Instructor:")
        print(instructorD)

        studentD = read_file(fp)
        print("Student:")
        print(studentD)

        assert studentD == instructorD

        print("-"*20)
        fp = open("Indila.txt",encoding="UTF-8")
        print("File Indila.txt opened.")
        instructorD = {'importance', 'et', 'dernière', 'recommence', 'avec', 'peur', 'trimer', \
                    'souffrance', 'pour', 'une', 'tu', 'cette', 'un', 'oh', 'ce', 'être', 'bruit', \
                        'jour', 'vie', 'douce', 'sur', 'décor', 'dans', 'oublier', 'toutes', 'du', \
                            'je', 'vent', 'recommences', 'revient', 'cours', 'la', 'immense', 'écoute', \
                                'remue', 'ciel', 'miel', 'veux', 'vide', 'ma', 'comme', 'en', 'ton', \
                                    'paris', 'chemin', 'tour', 'pluie', 'pourquoi', 'qui', 'le', \
                                        'offenses', 'métro', 'tout', 'douleur', 'danse', 'de', 'paro', \
                                            'indila', 'nuit', 'déambule', 'vole', 'seule', 'sens', 'monde', \
                                                'peu', 'sans', 'brille', 'cœur', 'les', 'que', 'lui', 'mon', \
                                                    'brin', 'toi', 'absence', 'enfant', 'suis', 'dont', 'est', 
                                                    'beau', 'peine', 'payé'}
        print("Instructor:")
        print(instructorD)

        studentD = read_file(fp)
        print("Student:")
        print(studentD)

        assert studentD == instructorD