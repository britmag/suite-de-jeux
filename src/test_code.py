import unittest
import numpy as np
import bm_prob

class TestMethods(unittest.TestCase):

    def setUp(self):
        n_choices = 10
        self.names = np.arange(n_choices)
        self.weights = np.random.random(n_choices)
        self.norm_weights = bm_prob.normalize_weights(self.weights)
        self.prob_fn = bm_prob.initialize_named_choices(self.names,
                                                        self.weights)
    
    def test_normalization(self):
        sum_weights = np.sum(self.norm_weights)
        self.assertAlmostEqual(sum_weights,1)

    def test_initalize_named_choices(self):
        xk = np.arange(len(self.names))
        pk = self.prob_fn.pmf(xk)
        np.testing.assert_allclose(pk, self.norm_weights)

    def test_setup_ordered_weights(self):
        names = ['A', 'B', 'C', 'DD']
        w = bm_prob.setup_ordered_weights(names)
        np.testing.assert_allclose(w, np.array([4, 3, 2, 1]))


if __name__=='__main__':

    suite = unittest.TestLoader().loadTestsFromTestCase(TestMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
