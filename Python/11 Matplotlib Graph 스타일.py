import matplotlib.pyplot as plt

plt.style.use('bmh')
plt.style.use('ggplot')
plt.style.use('classic')
plt.style.use('Solarize_Light2')
plt.style.use('default')

plt.plot([1, 2, 3, 4], [4, 6, 2, 7])
plt.show()
# matplotlib.style.use()를 사용해서 다양한 스타일을 지정


plt.style.use('default')
plt.rcParams['xtick.top'] = True
plt.rcParams['ytick.right'] = True
plt.rcParams['xtick.direction'] = 'in'
plt.rcParams['ytick.direction'] = 'in'
# plt.rcParams['xtick.major.size'] = 7
# plt.rcParams['ytick.major.size'] = 7
# plt.rcParams['xtick.minor.visible'] = True
# plt.rcParams['ytick.minor.visible'] = True
plt.plot([1, 2, 3, 4], [4, 6, 2, 7])
plt.show()


