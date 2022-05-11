import matplotlib.pyplot as plt
import openmdao.api as om
import numpy as np
from pathlib import Path

root_dir = Path(__file__).parent.absolute()
battery_capacity_file = root_dir / "DOE_battery_capacity_mwh_vs_all_objs" / "cases.sql"
battery_power_file = root_dir / "DOE_battery_power_mw_vs_all_objs" / "cases.sql"
interconnection_size_file = root_dir / "DOE_interconnection_size_mw_vs_all_objs" / "cases.sql"
solar_size_file = root_dir / "DOE_solar_size_mw_vs_all_objs" / "cases.sql"
wind_size_file = root_dir / "DOE_wind_size_mw_vs_all_objs" / "cases.sql"

battery_cap_cr = om.CaseReader(battery_capacity_file)
battery_power_cr = om.CaseReader(battery_power_file)
interconnection_size_cr = om.CaseReader(interconnection_size_file)
solar_size_cr = om.CaseReader(solar_size_file)
wind_size_cr = om.CaseReader(wind_size_file)

battery_cap_cases = battery_cap_cr.list_cases('driver')
battery_power_cases = battery_power_cr.list_cases('driver')
interconnection_size_cases = interconnection_size_cr.list_cases('driver')
solar_size_cases = solar_size_cr.list_cases('driver')
wind_size_cases = wind_size_cr.list_cases('driver')

battery_cap_results = {}
for case in battery_cap_cases:
    outputs = battery_cap_cr.get_case(case).outputs
    for key in outputs:

        if key not in battery_cap_results.keys():
            battery_cap_results[key] = []

        battery_cap_results[key].append(outputs[key])

for key in battery_cap_results:
    battery_cap_results[key] = np.array(battery_cap_results[key]) 

battery_power_results = {}
for case in battery_power_cases:
    outputs = battery_power_cr.get_case(case).outputs
    for key in outputs:

        if key not in battery_power_results.keys():
            battery_power_results[key] = []

        battery_power_results[key].append(outputs[key])

for key in battery_power_results:
    battery_power_results[key] = np.array(battery_power_results[key]) 

interconnection_size_results = {}
for case in interconnection_size_cases:
    outputs = interconnection_size_cr.get_case(case).outputs
    for key in outputs:

        if key not in interconnection_size_results.keys():
            interconnection_size_results[key] = []

        interconnection_size_results[key].append(outputs[key])

for key in interconnection_size_results:
    interconnection_size_results[key] = np.array(interconnection_size_results[key]) 

solar_size_results = {}
for case in solar_size_cases:
    outputs = solar_size_cr.get_case(case).outputs
    for key in outputs:

        if key not in solar_size_results.keys():
            solar_size_results[key] = []

        solar_size_results[key].append(outputs[key])

for key in solar_size_results:
    solar_size_results[key] = np.array(solar_size_results[key])

wind_size_results = {}
for case in wind_size_cases:
    outputs = wind_size_cr.get_case(case).outputs
    for key in outputs:

        if key not in wind_size_results.keys():
            wind_size_results[key] = []

        wind_size_results[key].append(outputs[key])

for key in wind_size_results:
    wind_size_results[key] = np.array(wind_size_results[key])


### scatter plots to visualize DOE results
# Battery capacity MWh vs Hybrid LCOE
X = battery_cap_results['battery_capacity_mwh'][1:]
Y = battery_cap_results['hybrid_lcoe_real'][1:]

plt.scatter(X, Y)
plt.xlabel('Battery Capacity (MWh)', fontsize=16)
plt.ylabel('Hybrid system LCOE ($/kWh)', fontsize=16)
plt.title('Battery capacity vs Hybrid system LCOE', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
fname = 'battery_capacity_vs_hybrid_system_lcoe.pdf'
plt.savefig(fname, bbox_inches='tight')
plt.clf()

# Battery power MW vs Hybrid LCOE
X = battery_power_results['battery_power_mw'][1:]
Y = battery_power_results['hybrid_lcoe_real'][1:]

plt.scatter(X, Y)
plt.xlabel('Battery Power (MW)', fontsize=16)
plt.ylabel('Hybrid system LCOE ($/kWh)', fontsize=16)
plt.title('Battery power vs Hybrid system LCOE', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
fname = 'battery_power_vs_hybrid_system_lcoe.pdf'
plt.savefig(fname, bbox_inches='tight')
plt.clf()

# Interconnection size MW vs Hybrid LCOE
X = interconnection_size_results['interconnection_size_mw'][1:]
Y = interconnection_size_results['hybrid_lcoe_real'][1:]

plt.scatter(X, Y)
plt.xlabel('Grid interconnection size (MW)', fontsize=16)
plt.ylabel('Hybrid system LCOE ($/kWh)', fontsize=16)
plt.title('Interconnection size vs Hybrid system LCOE', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
fname = 'interconnection_size_vs_hybrid_system_lcoe.pdf'
plt.savefig(fname, bbox_inches='tight')
plt.clf()

# Solar size MW vs Hybrid LCOE
X = solar_size_results['solar_size_mw']
Y = solar_size_results['hybrid_lcoe_real']

plt.scatter(X, Y)
plt.xlabel('Solar size (MW)', fontsize=16)
plt.ylabel('Hybrid system LCOE ($/kWh)', fontsize=16)
plt.title('Solar size vs Hybrid system LCOE', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
fname = 'solar_size_vs_hybrid_system_lcoe.pdf'
plt.savefig(fname, bbox_inches='tight')
plt.clf()

# Wind size MW vs Hybrid LCOE
X = wind_size_results['wind_size_mw']
Y = wind_size_results['hybrid_lcoe_real']

plt.scatter(X, Y)
plt.xlabel('Wind size (MW)', fontsize=16)
plt.ylabel('Hybrid system LCOE ($/kWh)', fontsize=16)
plt.title('Wind size vs Hybrid system LCOE', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
fname = 'wind_size_vs_hybrid_system_lcoe.pdf'
plt.savefig(fname, bbox_inches='tight')
plt.clf()

# Wind size MW vs Hybrid LCOE
X = wind_size_results['wind_size_mw']
Y = wind_size_results['grid_curtailment_%']

plt.scatter(X, Y)
plt.xlabel('Wind size (MW)', fontsize=16)
plt.ylabel('Grid curtailment (%)', fontsize=16)
plt.title('Wind size vs Grid curtailment', fontsize=16)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
fname = 'wind_size_vs_grid_curtailment_%.pdf'
plt.savefig(fname, bbox_inches='tight')
plt.clf()
