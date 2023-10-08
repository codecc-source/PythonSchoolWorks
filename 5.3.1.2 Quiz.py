from matplotlib import pyplot as plt
month_x = ["January", "February", "March", "April", "May"]

dev_y = [28580,29225,26326,30017,36134]
plt.plot(month_x, dev_y, color='red', linestyle='--', label='Classics')

dev_y2 = [28970,22262,28640,39985,33428]
plt.plot(month_x, dev_y2, color='blue', linestyle='--', label='Mystery')

dev_y3 = [24236,231390,29022,31009,31474]
plt.plot(month_x, dev_y3, color='black', linestyle='--', label='Romance')

dev_y4 = [26730,29730,22109,31355,37686]
plt.plot(month_x, dev_y4, color='Yellow', linestyle='--', label='Sci-Fi & Fantasy')

dev_y5 = [25358,22685,20893,36065,31388]
plt.plot(month_x, dev_y5, color='green', linestyle='--', label='Young Adult')

plt.xlabel('Month')
plt.ylabel('Book Sales')
plt.title('Chart')
plt.legend()
plt.show()
