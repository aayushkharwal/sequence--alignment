import numpy as np
import matplotlib.pyplot as plt

x_axis_basic = np.array([16, 64, 128, 256, 384, 512, 768, 1024, 1280, 1536, 2048, 2560, 3072, 3584, 3968])

# Time
y_axis_basic = np.array([
    3.016710,
    5.321264,
    9.997845,
    18.998861,
    30.000448,
    54.658413,
    112.696409,
    185.956240,
    277.534246,
    379.178762,
    666.635513,
    1044.125795,
    1434.108257,
    1974.054337,
    2772.069216
])
y_axis_eff = np.array([
    16.010761,
    72.981358,
    136.001110,
    274.044514,
    330.477476,
    710.593939,
    1200.760126,
    1584.869623,
    1927.115202,
    2717.127800,
    3719.980240,
    4604.018688,
    5771.957874,
    7809.846163,
    9347.956181
])

# Memory
# y_axis_basic = np.array([
#     32720,
#     32856,
#     32892,
#     33436,
#     33316,
#     34676,
#     33612,
#     34052,
#     33548,
#     33152,
#     33280,
#     34524,
#     34708,
#     35100,
#     35044
# ])
# y_axis_eff = np.array([
#     32744,
#     32824,
#     32872,
#     32916,
#     32908,
#     32808,
#     32908,
#     33040,
#     33084,
#     33108,
#     33084,
#     33112,
#     33468,
#     33504,
#     33468,

# ])

plt.plot(x_axis_basic, y_axis_basic, label='Basic', marker='o', markerfacecolor='blue', markersize=5)
plt.plot(x_axis_basic, y_axis_eff, label='Efficient',  marker='o', markerfacecolor='orange', markersize=5)
plt.xlabel('Problem Size (m+n)')

plt.ylabel('CPU Time (milliseconds)')
plt.title('CPU Time vs Problem Size')
plt.savefig('CPU Time.png')

# plt.ylabel('Memory Usage (KB)')
# plt.title('Memory Usage vs Problem Size')
# plt.savefig('Memory Usage.png')

plt.legend(["Basic", "Efficient"], loc="lower right")
plt.show()