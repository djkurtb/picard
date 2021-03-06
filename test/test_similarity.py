from test.picardtestcase import PicardTestCase

from picard.similarity import similarity


class SimilarityTest(PicardTestCase):

    def test_correct(self):
        self.assertEqual(similarity(u"K!", u"K!"), 1.0)
        self.assertEqual(similarity(u"BBB", u"AAA"), 0.0)
        self.assertAlmostEqual(similarity(u"ABC", u"ABB"), 0.7, 1)
