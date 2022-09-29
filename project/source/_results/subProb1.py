r"""
Sub Problem 1
################

Final code .... 
"""

from numpy import array, ndarray
from gemseo.algos.design_space import DesignSpace
from gemseo.api import create_design_space
from gemseo.api import create_discipline
from gemseo.api import create_surrogate
from gemseo.mlearning.qual_measure.r2_measure import R2Measure
from gemseo.mlearning.qual_measure.rmse_measure import RMSEMeasure
from gemseo_mlearning.api import sample_discipline
import discipline as disc

# %%
# Firstly,
# we define the discipline computing the Rosenbrock function
# and the Euclidean distance to the optimum:

discipline = disc.H2TurboFan()

class suProb1_design_space(DesignSpace):

    def __init__(self):
        super().__init__()
        self.add_variable("thrust", value = discipline.DEFAULT_DESIGN_VALUES["thrust"][0], l_b = unit.N_kN(100), u_b = unit.N_kN(150) )
        self.add_variable("bpr",value = discipline.DEFAULT_DESIGN_VALUES["bpr"][0], l_b=5, u_b = 12)
        self.add_variable("area",value = discipline.DEFAULT_DESIGN_VALUES["area"][0], l_b=120, u_b=200)
        self.add_variable("aspect_ratio",value = discipline.DEFAULT_DESIGN_VALUES["aspect_ratio"][0], l_b=7, u_b=12)

# %%
# Then,
# we sample the discipline with an optimal LHS:
design_space = suProb1_design_space()
dataset = sample_discipline(discipline, design_space, output_names = ["tolf", "vapp", "vz_mcl","vz_mcr","oei_path","ttc","far"], algo_name = "OT_OPT_LHS", n_samples = 30)

# %%
# let's take a look at the dataset 
print(dataset.export_to_dataframe().head())

# %%
# before creating a surrogate discipline:
surrogate_discipline = create_surrogate("RBFRegressor", dataset)

# %%
# and using it for prediction:
surrogate_discipline.execute({"x": array([1.])})
print(surrogate_discipline.cache.last_entry)

# %%
# This surrogate discipline can be used in a scenario.
# The underlying regression model can also be assessed,
# with the R2 measure for instance:
r2 = R2Measure(surrogate_discipline.regression_model, True)
print(r2.evaluate_learn())  # learning measure
print(r2.evaluate_kfolds())  # k-folds cross-validation measure

# %%
# or with the root mean squared error:
rmse = RMSEMeasure(surrogate_discipline.regression_model, True)
print(rmse.evaluate_learn())
print(rmse.evaluate_kfolds())
