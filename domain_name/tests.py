# coding: utf-8
from __future__ import absolute_import

from unittest.case import TestCase

from .utils import domain_ranking


class DomainRankingTests(TestCase):
    """ Тесты утиты для построения иерархии доменов
    """

    def testSimple(self):
        self.assertEqual(['www.rutube.ru', '*.rutube.ru', '*.ru', '*'],
                         domain_ranking('www.rutube.ru'))

    def testEmpty(self):
        self.assertRaises(ValueError, domain_ranking, '')

    def testRoot(self):
        self.assertEqual(['ru', '*'], domain_ranking('ru'))

    def testRootDot(self):
        self.assertEqual(['ru', '*'], domain_ranking('ru.'))

    def testJunkDomain(self):
        self.assertEqual(['rutube.ru', '*.ru', '*'],
                         domain_ranking('\t \nrutube.ru.\n \t'))
