import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# Using histplot (recommended)
sns.histplot(data, bins=4, color="skyblue")  # Control bins, color, etc.
plt.title("Histplot")
plt.show()
plt.figure(figsize=(20,70))
plt.xticks(rotation=90)
# If you want the combined view, you now combine separate plots:
sns.histplot(data, kde=True, color="skyblue")  # Histogram with KDE
sns.rugplot(data, color="darkblue")  # Add rug plot separately
plt.title("Histplot with KDE and Rugplot")
plt.show()


# distplot - would give you a similar view as the combined histplot/kde/rugplot above.
# However, it is now deprecated, so it's best to use histplot + other plots as needed.
# sns.distplot(data)  # Avoid using this as it's deprecated.