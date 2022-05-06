import matplotlib.pyplot as plt
import openmdao.api as om
import numpy as np
from pathlib import Path

root_dir = Path(__file__).parent.absolute()
nrel_file = root_dir / "nrel_data" / "cases.sql"
nasa_file = root_dir / "nasa_data" / "cases.sql"

nrel_cr = om.CaseReader(nrel_file)
nasa_cr = om.CaseReader(nasa_file)
nrel_cases = nrel_cr.list_cases('driver')
nasa_cases = nasa_cr.list_cases('driver')

nrel_results = {}
for case in nrel_cases:
    outputs = nrel_cr.get_case(case).outputs
    for key in outputs:

        if key not in nrel_results.keys():
            nrel_results[key] = []

        nrel_results[key].append(outputs[key])

for key in nrel_results:
    nrel_results[key] = np.array(nrel_results[key]) 

nasa_results = {}
for case in nasa_cases:
    outputs = nasa_cr.get_case(case).outputs
    for key in outputs:

        if key not in nasa_results.keys():
            nasa_results[key] = []

        nasa_results[key].append(outputs[key])

for key in nasa_results:
    nasa_results[key] = np.array(nasa_results[key]) 

### multi-bar charts
# Annual Energies (MW) by system component
X = ['Solar', 'Wind', 'Hybrid']
Y = [float(nrel_results['pv_annual_energy']/1000), float(nrel_results['wind_annual_energy']/1000), float(nrel_results['hybrid_annual_energy']/1000)]
Z = [float(nasa_results['pv_annual_energy']/1000), float(nasa_results['wind_annual_energy']/1000), float(nasa_results['hybrid_annual_energy']/1000)]
X_axis = np.arange(3)

plt.bar(X_axis - 0.2, Y, 0.4, label = "NREL")
plt.bar(X_axis + 0.2, Z, 0.4, label = "NASA")
plt.xticks(X_axis, X)
plt.xlabel("Systems")
plt.ylabel("Annual Energy (MW)")
plt.title("Annual Energies by component")
plt.legend()
fname = 'annual_energies_by_component.png'
plt.savefig(fname)
plt.clf()

# LCOE real by system component 
X = ['Solar', 'Wind', 'Hybrid']
Y = [float(nrel_results['pv_lcoe_real']), float(nrel_results['wind_lcoe_real']), float(nrel_results['hybrid_lcoe_real'])]
Z = [float(nasa_results['pv_lcoe_real']), float(nasa_results['wind_lcoe_real']), float(nasa_results['hybrid_lcoe_real'])]
X_axis = np.arange(3)

plt.bar(X_axis - 0.2, Y, 0.4, label = "NREL")
plt.bar(X_axis + 0.2, Z, 0.4, label = "NASA")
plt.xticks(X_axis, X)
plt.xlabel("Systems")
plt.ylabel("LCOE (USD/kW*h)")
plt.title("LCOE by component")
plt.legend()
fname = 'lcoe_by_component.png'
plt.savefig(fname)
plt.clf()

# Total revenues ($ Millions) by system component
X = ['Solar', 'Wind', 'Hybrid']
Y = [float(nrel_results['pv_total_revenues']/(1e6)), float(nrel_results['wind_total_revenues']/(1e6)), float(nrel_results['hybrid_total_revenues']/(1e6))]
Z = [float(nasa_results['pv_total_revenues']/(1e6)), float(nasa_results['wind_total_revenues']/(1e6)), float(nasa_results['hybrid_total_revenues']/(1e6))]
X_axis = np.arange(3)

plt.bar(X_axis - 0.2, Y, 0.4, label = "NREL")
plt.bar(X_axis + 0.2, Z, 0.4, label = "NASA")
plt.xticks(X_axis, X)
plt.xlabel("Systems")
plt.ylabel("Total Revenues ($ Millions)")
plt.title("Total Revenues by component")
plt.legend()
fname = 'total_revenues_by_component.png'
plt.savefig(fname)
plt.clf()

#NPV by system component
X = ['Solar', 'Wind', 'Hybrid']
Y = [float(nrel_results['pv_npv']), float(nrel_results['wind_npv']), float(nrel_results['hybrid_npv'])]
Z = [float(nasa_results['pv_npv']), float(nasa_results['wind_npv']), float(nasa_results['hybrid_npv'])]
X_axis = np.arange(3)

plt.bar(X_axis - 0.2, Y, 0.4, label = "NREL")
plt.bar(X_axis + 0.2, Z, 0.4, label = "NASA")
plt.xticks(X_axis, X)
plt.xlabel("Systems")
plt.ylabel("Net Present Value ($)")
plt.title("Net Present Value by component")
plt.legend()
fname = 'npv_by_component.png'
plt.savefig(fname)
plt.clf()

### Visualize time series generation profile
# Solar generation profile, 1 week timescale
X = list(range(0,168))
Y = nrel_results['pv_generation_profile'][0][0:168]
Z = nasa_results['pv_generation_profile'][0][0:168]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Solar Power Generation (kW)")
plt.title("Solar Generation Profiles")
plt.legend()
fname = 'solar_generation_profile.png'
plt.savefig(fname)
plt.clf()

# Wind generation profile, 1 week timescale
X = list(range(0,168))
Y = nrel_results['wind_generation_profile'][0][0:168]
Z = nasa_results['wind_generation_profile'][0][0:168]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Wind Power Generation (kW)")
plt.title("Wind Generation Profiles")
plt.legend()
fname = 'wind_generation_profile.png'
plt.savefig(fname)
plt.clf()

# Hybrid generation profile, 1 week timescale
X = list(range(0,168))
Y = nrel_results['hybrid_generation_profile'][0][0:168]
Z = nasa_results['hybrid_generation_profile'][0][0:168]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Hybrid Power Generation (kW)")
plt.title("Hybrid Generation Profiles")
plt.legend()
fname = 'hybrid_generation_profile.png'
plt.savefig(fname)
plt.clf()

### Visualize timeseries resource data
# Solar resource data
# 2 week range
X = list(range(0,336))
Y = nrel_results['pv_resource_gh'][0][0:336]
Z = nasa_results['pv_resource_gh'][0][0:336]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Global Horizontal Irradiance (W/m^2)")
plt.title("GHI by data source")
plt.legend()
fname = 'pv_resource_gh_2week.png'
plt.savefig(fname)
plt.clf()
# 1 year range
X = list(range(0,8760))
Y = nrel_results['pv_resource_gh'][0][0:8760]
Z = nasa_results['pv_resource_gh'][0][0:8760]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Global Horizontal Irradiance (W/m^2)")
plt.title("GHI by data source")
plt.legend()
fname = 'pv_resource_gh_1year.png'
plt.savefig(fname)
plt.clf()

# Wind resource data
# 2 week range
X = list(range(0,336))
Y = nrel_results['wind_resource_speed'][0][0:336]
Z = nasa_results['wind_resource_speed'][0][0:336]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Wind speed (m/s)")
plt.title("Wind speed by data source")
plt.legend()
fname = 'wind_resource_speed_2week.png'
plt.savefig(fname)
plt.clf()
# 1 year range
X = list(range(0,8760))
Y = nrel_results['wind_resource_speed'][0][0:8760]
Z = nasa_results['wind_resource_speed'][0][0:8760]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Wind speed (m/s)")
plt.title("Wind speed by data source")
plt.legend()
fname = 'wind_resource_speed_1year.png'
plt.savefig(fname)
plt.clf()

# plot_doe_results.py plotting
# Plot DV vs various objectives, intended for one design variable and 1+ objectives
# des_var = list(cr.get_case(case).get_design_vars().keys())[0]
# for key in results:
#     if key != des_var:
#         plt.scatter(results[des_var],results[key])
#         plt.xlabel('{}'.format(des_var))
#         plt.ylabel('{}'.format(key))
#         fname = '{}_vs_{}.png'.format(des_var,key)
#         plt.savefig(fname)
#         plt.clf()
    # plt.show()