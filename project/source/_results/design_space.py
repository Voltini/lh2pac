"""
H2TurboFan: Design_Space
########################
"""

from numpy import array, ndarray
from gemseo.algos.design_space import DesignSpace
from gemseo.api import create_design_space


class MyDesignSpace(DesignSpace):
    DESIGN_VARIABLES = ["thrust", "bpr", "area", "aspect_ratio"]
    def __init__(self):
        super().__init__()
        self.add_variable("thrust",l_b = 100, u_b = 150)
        self.add_variable("bpr", l_b=5, u_b = 12)
        self.add_variable("area", l_b=120, u_b=200)
        self.add_variable("aspect_ratio", l_b=7, u_b=12)
design_space = MyDesignSpace()
print(design_space)