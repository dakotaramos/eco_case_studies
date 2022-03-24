import matplotlib.pyplot as plt
import openmdao.api as om
import numpy as np


cr = om.CaseReader("cases.sql")
cases = cr.list_cases('driver')
print(cases)

solar_sizes = []
npvs = []
for case in cases:
    outputs = cr.get_case(case).outputs
    solar_sizes.append(outputs['solar_size_mw'])
    npvs.append(outputs['hybrid_npv'])
    
solar_sizes = np.array(solar_sizes)
npvs = np.array(npvs)

print(solar_sizes)
print(npvs)

plt.scatter(solar_sizes, npvs)

plt.plot([np.max(solar_sizes), np.min(solar_sizes)], [np.min(npvs), np.max(npvs)])
plt.show()