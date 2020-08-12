import numpy as np
import mulberry as mb
import unittest


class TestTree(unittest.TestCase):
    def setUp(self):
        self.tree = mb.Tree()
        self.tree.setTransform(np.array([[0,0,1, 0.5],
                                         [1,0,0, 0.1],
                                         [0,1,0, 0  ],
                                         [0,0,0, 1  ]]), "/base_link", "/cam_fl")
        self.tree.setTransform(np.array([[0,0,1, 0.5],
                                         [1,0,0,-0.1],
                                         [0,1,0, 0  ],
                                         [0,0,0, 1  ]]), "/base_link", "/cam_fr")

        def allclose(a, b, msg=None):
            try:
                np.testing.assert_allclose(a, b)
                eq = True
            except Exception as e:
                eq = False
                msg = str(e)
            if not eq:
                raise self.failureException(msg)

        self.addTypeEqualityFunc(np.ndarray, allclose)

    def testHasFrame(self):
        fl2fr = np.array([[1,0,0,0.2],
                           [0,1,0,0 ],
                           [0,0,1,0 ],
                           [0,0,0,1 ]])
        self.assertEqual(self.tree.getTransform("/cam_fr", "/cam_fl"), fl2fr)

if __name__ == '__main__':
    unittest.main()
