import matplotlib.pyplot as plt
import openmdao.api as om
import numpy as np


cr = om.CaseReader("cases.sql")
cases = cr.list_cases('driver')
print(cases)

des_var = []
obj = []
for case in cases:
    outputs = cr.get_case(case).outputs
    des_var.append(outputs['interconnection_size_mw'])
    obj.append(outputs['internal_rate_of_return'])

# results = {}
# for case in cases:
#     outputs = cr.get_case(case).outputs
#     for key in outputs:

#         if key not in results.keys():
#             results[key] = []

#         results[key].append(outputs[key])

# for key in results:
#     results[key] = np.array(results[key]) 
    
des_var = np.array(des_var)
obj = np.array(obj)

print(des_var)
print(obj)

plt.scatter(des_var, obj)
plt.xlabel('Interconnection Size (MW)')
plt.ylabel('Internal Rate of Return (%)')

plt.plot([np.min(des_var), np.max(des_var)], [np.min(obj), np.max(obj)])
plt.show()