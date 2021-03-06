# -*- coding: utf-8 -*-

import unittest
from unittest import SkipTest

import taxonlist2json


class BinomialToDictTest(unittest.TestCase):
class ConverterTest(unittest.TestCase):

    def test_binomial_to_dict__with_simple_author(self):
        s = ' Abuta velutina Gleason'
        result = taxonlist2json.binomial_to_dict(s)
        expect = {'object': 'taxon',
                  'rank': 'species',
                  'epithet': 'velutina',
                  'ht-rank': 'genus',
                  'ht-epithet': 'Abuta',
                  'hybrid': False,
                  'author': 'Gleason',
                  }
        self.assertEquals(result, expect)

    def test_binomial_to_dict__with_composite_author(self):
        result = taxonlist2json.binomial_to_dict(
            'Abutilon mollissimum (Cav.) Sweet')
        expect = {'object': 'taxon',
                  'rank': 'species',
                  'epithet': 'mollissimum',
                  'ht-rank': 'genus',
                  'ht-epithet': 'Abutilon',
                  'hybrid': False,
                  'author': '(Cav.) Sweet',
                  }
        self.assertEquals(result, expect)

    def test_binomial_to_dict__author_with_utf8_char(self):
        s = "Abutilon nudiflorum (L'H&eacute;r.) Sweet"
        result = taxonlist2json.binomial_to_dict(s)
        expect = {'ht-epithet': 'Abutilon',
                  'rank': 'species',
                  'author': u"(L'Hér.) Sweet",
                  'hybrid': False,
                  'object': 'taxon',
                  'epithet': 'nudiflorum',
                  'ht-rank': 'genus'}
        self.assertEquals(result, expect)

    def test_binomial_to_dict__varietas_with_autor(self):
        s = "Abutilon amplissimum var. subpeltata Ktze."
 
        result = taxonlist2json.line_to_binomial_to_dict(s)
 
        expect = {'object': 'taxon',
                 'rank': 'varietas',
                 'epithet': 'subpeltata',
                 'ht-rank': 'genus',
                 'ht-epithet': 'amplissimum',
                 'hybrid': False,
                 'author': 'Ktze',
          }
          self.assertEquals(result, expect)


class SynonymLineToObjectsPairTest(unittest.TestCase):

    def test_synonym_line_to_objects_pair(self):
        s = "Abutilon pulverulentum Ulbrich = "\
            "Sidasodes jamesonii (Baker f. ) Fryxell & Fuertes"

        result = taxonlist2json.synonym_line_to_objects_pair(s)

        expect = ({'ht-epithet': 'Abutilon', 'rank': 'species',
                   'author': 'Ulbrich', 'hybrid': False,
                   'object': 'taxon', 'epithet': 'pulverulentum',
                   'ht-rank': 'genus'},
                  {'ht-epithet': 'Sidasodes',
                   'rank': 'species',
                   'author': '(Baker f. ) Fryxell & Fuertes',
                   'hybrid': False,
                   'object': 'taxon',
                   'epithet': 'jamesonii',
                   'ht-rank': 'genus'})
        self.assertEquals(result, expect)

