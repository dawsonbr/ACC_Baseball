import matplotlib.pyplot as plt
import pandas as pd

# Load data
df = pd.read_excel('ACC_players_with_distances.xlsx')

# Extract the distance column
distances = df['Distance (miles)']

# Filter out the extreme outliers
filtered_distances = distances[distances <= 3000]

# Define bin edges 
bins = list(range(0, 3100, 100))  

# Create the histogram
plt.figure(figsize=(12, 8))
plt.hist(filtered_distances, bins=bins, edgecolor='black', alpha=0.7)

# Add labels and title
plt.title('Distances Between Hometowns and Universities (Up to 3000 miles)', fontsize=16)
plt.xlabel('Distance (miles)', fontsize=13)
plt.ylabel('# of Players', fontsize=13)

# Customize x-axis ticks
plt.xticks(ticks=range(0, 3100, 500), labels=[str(x) for x in range(0, 3100, 500)])

# Add a grid for better readability
plt.grid(True)

# Add note
plt.gca().text(0.5, -0.15, 'Note: Two players were excluded from the histogram who were greater than 4000 miles away due to readability of the graph.',
                ha='center', va='center', fontsize=10, color='gray', transform=plt.gca().transAxes)

# Adjust layout 
plt.tight_layout(rect=[0, 0.1, 1, 1])  


plt.show()


