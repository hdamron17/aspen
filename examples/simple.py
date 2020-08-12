import numpy as np
import mulberry as mb

tree = mb.Tree()
tree.setTransform(np.array([[0,0,1, 0.5],
                            [1,0,0, 0.1],
                            [0,1,0, 0  ],
                            [0,0,0, 1  ]]), "/base_link", "/cam_fl")
tree.setTransform(np.array([[0,0,1, 0.5],
                            [1,0,0,-0.1],
                            [0,1,0, 0  ],
                            [0,0,0, 1  ]]), "/base_link", "/cam_fr")

print(tree.getTransform("/base_link", "/cam_fl"))
print(tree.getTransform("/cam_fl", "/base_link"))
print(tree.getTransform("/cam_fl", "/cam_fr"))
print(tree.getTransform("/cam_fr", "/cam_fl"))