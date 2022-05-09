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
plt.ylabel("Annual Energy (MWh)")
plt.title("Annual Energy by component")
plt.legend()
fname = 'annual_energy_by_component.pdf'
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
plt.ylabel("LCOE ($/kWh)")
plt.title("Levelized Cost Of Energy by component")
plt.legend()
fname = 'lcoe_by_component.pdf'
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
fname = 'total_revenues_by_component.pdf'
plt.savefig(fname)
plt.clf()

#NPV by system component
X = ['Solar', 'Wind', 'Hybrid']
Y = [float(nrel_results['pv_npv']/(1e6)), float(nrel_results['wind_npv']/(1e6)), float(nrel_results['hybrid_npv']/(1e6))]
Z = [float(nasa_results['pv_npv']/(1e6)), float(nasa_results['wind_npv']/(1e6)), float(nasa_results['hybrid_npv']/(1e6))]
X_axis = np.arange(3)

plt.bar(X_axis - 0.2, Y, 0.4, label = "NREL")
plt.bar(X_axis + 0.2, Z, 0.4, label = "NASA")
plt.xticks(X_axis, X)
plt.xlabel("Systems")
plt.ylabel("Net Present Value ($ Millions)")
plt.title("Net Present Value by component")
plt.legend()
fname = 'npv_by_component.pdf'
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
plt.ylabel("Solar Power (kW)")
plt.title("Solar Power Generation Profiles")
plt.legend()
fname = 'one_week_solar_generation_profile.pdf'
plt.savefig(fname)
plt.clf()

# Wind generation profile, 1 week timescale
X = list(range(0,168))
Y = nrel_results['wind_generation_profile'][0][0:168]
Z = nasa_results['wind_generation_profile'][0][0:168]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Wind Power (kW)")
plt.title("Wind Power Generation Profiles")
plt.legend()
fname = 'one_week_wind_generation_profile.pdf'
plt.savefig(fname)
plt.clf()

# Hybrid generation profile, 1 week timescale
X = list(range(0,168))
Y = nrel_results['hybrid_generation_profile'][0][0:168]
Z = nasa_results['hybrid_generation_profile'][0][0:168]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Hybrid Power (kW)")
plt.title("Hybrid Power Generation Profiles")
plt.legend()
fname = 'one_week_hybrid_generation_profile.pdf'
plt.savefig(fname)
plt.clf()

### Visualize timeseries resource data
# Solar GHI
# 2 week range
X = list(range(0,336))
Y = nrel_results['pv_resource_gh'][0][0:336]
Z = nasa_results['pv_resource_gh'][0][0:336]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("GHI (W/$m^2$)")
plt.title("Global Horizontal Irradiance")
plt.legend()
fname = 'two_week_pv_resource_gh.pdf'
plt.savefig(fname)
plt.clf()
# 1 year range
X = list(range(0,8760))
Y = nrel_results['pv_resource_gh'][0][0:8760]
Z = nasa_results['pv_resource_gh'][0][0:8760]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("GHI (W/$m^2$)")
plt.title("Global Horizontal Irradiance")
plt.legend()
fname = 'one_year_pv_resource_gh.pdf'
plt.savefig(fname)
plt.clf()

# Wind resource data
# Wind speed: 2 week range
X = list(range(0,336))
Y = nrel_results['wind_resource_speed'][0][0:336]
Z = nasa_results['wind_resource_speed'][0][0:336]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Wind speed (m/s)")
plt.title("Wind speed at hub height")
plt.legend()
fname = 'two_week_wind_resource_speed.pdf'
plt.savefig(fname)
plt.clf()
# Wind speed: 1 year range
X = list(range(0,8760))
Y = nrel_results['wind_resource_speed'][0][0:8760]
Z = nasa_results['wind_resource_speed'][0][0:8760]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Wind speed (m/s)")
plt.title("Wind speed at hub height")
plt.legend()
fname = 'one_year_wind_resource_speed.pdf'
plt.savefig(fname)
plt.clf()

# Wind temp: 2 week range
X = list(range(0,336))
Y = nrel_results['wind_resource_temp'][0][0:336]
Z = nasa_results['wind_resource_temp'][0][0:336]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Temperature (\N{DEGREE SIGN}C)")
plt.title("Temperature at hub height")
plt.legend()
fname = 'two_week_wind_resource_temp.pdf'
plt.savefig(fname)
plt.clf()
# Wind temp: 1 year range
X = list(range(0,8760))
Y = nrel_results['wind_resource_temp'][0][0:8760]
Z = nasa_results['wind_resource_temp'][0][0:8760]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Temp (\N{DEGREE SIGN}C)")
plt.title("Temperature at hub height")
plt.legend()
fname = 'one_year_wind_resource_temp.pdf'
plt.savefig(fname)
plt.clf()

# Wind pres: 2 week range
X = list(range(0,336))
Y = nrel_results['wind_resource_pres'][0][0:336]
Z = nasa_results['wind_resource_pres'][0][0:336]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Pressure (atm)")
plt.title("Pressure at hub height")
plt.legend()
fname = 'two_week_wind_resource_pres.pdf'
plt.savefig(fname)
plt.clf()
# Wind pres: 1 year range
X = list(range(0,8760))
Y = nrel_results['wind_resource_pres'][0][0:8760]
Z = nasa_results['wind_resource_pres'][0][0:8760]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Pressure (atm)")
plt.title("Pressure at hub height")
plt.legend()
fname = 'one_year_wind_resource_pres.pdf'
plt.savefig(fname)
plt.clf()

# Wind direction: 2 week range
X = list(range(0,336))
Y = nrel_results['wind_resource_dir'][0][0:336]
Z = nasa_results['wind_resource_dir'][0][0:336]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Wind direction (degrees)")
plt.title("Wind direction at hub height")
plt.legend()
fname = 'two_week_wind_resource_dir.pdf'
plt.savefig(fname)
plt.clf()
# Wind direction: 1 year range
X = list(range(0,8760))
Y = nrel_results['wind_resource_dir'][0][0:8760]
Z = nasa_results['wind_resource_dir'][0][0:8760]

plt.plot(X, Y, label="NREL")
plt.plot(X, Z, label="NASA", linestyle='--')
plt.xlabel("Hours")
plt.ylabel("Wind direction (degrees)")
plt.title("Wind direction at hub height")
plt.legend()
fname = 'one_year_wind_resource_dir.pdf'
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
#         fname = '{}_vs_{}.pdf'.format(des_var,key)
#         plt.savefig(fname)
#         plt.clf()
    # plt.show()