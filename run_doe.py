import openmdao.api as om
import json
from pathlib import Path

from eco_case_studies.hopp_wrapper import HybridSystem
from hybrid.sites import SiteInfo, flatirons_site
from hybrid.hybrid_simulation import HybridSimulation
from hybrid.log import hybrid_logger as logger
from hybrid.keys import set_nrel_key_dot_env

        
examples_dir = Path(__file__).parent.absolute()

# Set API key
set_nrel_key_dot_env()

if __name__ == "__main__":
    # build the model
    prob = om.Problem()
    prob.model.add_subsystem('hybrid_system', HybridSystem(), promotes=['*'])

    # # setup the optimization
    prob.driver = om.ScipyOptimizeDriver()
    # prob.driver.options['optimizer'] = 'SLSQP'
    prob.driver = om.DOEDriver(om.UniformGenerator(num_samples=6, seed=1))
    prob.driver.options['debug_print'] = ["desvars", "objs"]
    prob.driver.add_recorder(om.SqliteRecorder("cases.sql"))
    
    # Solar DVs
    prob.model.add_design_var('solar_size_mw', lower=0., upper=100.)


    prob.model.add_objective('hybrid_npv', ref=-1.)
    prob.model.add_objective('lcoe_real', ref=-1.)
    prob.model.add_objective('lcoe_nom', ref=-1.)
    prob.model.add_objective('internal_rate_of_return', ref=1.)
     
    # prob.model.approx_totals()
    
    prob.setup()
    prob.run_driver()
    
    prob.model.list_outputs()
    

    
    