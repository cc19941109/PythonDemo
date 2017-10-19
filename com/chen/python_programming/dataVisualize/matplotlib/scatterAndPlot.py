import matplotlib.pyplot as plt

values= [0,1,2,3,4,5]
squares = [0,1,4,9,16,25]

plt.plot(values,squares,linewidth = 5)
plt.title("Square Numbers",fontsize = 24)
plt.xlabel("value",fontsize = 14)
plt.ylabel("Square of value",fontsize = 14)

plt.tick_params(axis='both',which = 'major',labelsize = 14)

plt.scatter(values,squares,s=150)


plt.show()






