import matplotlib.pyplot as plt

province_population = [1234444, 5334354, 7878686, 4242546, 7687696]
activities = ['Balochistan', 'Punjab', 'Sindh', 'Khyber', 'Gilgit-Baltistan']

plt.pie(province_population,
        labels=activities,
        startangle=50,
        autopct='%1.1f%%')   # corrected format string
plt.title('Pakistan Population Province Wise')
plt.show()
