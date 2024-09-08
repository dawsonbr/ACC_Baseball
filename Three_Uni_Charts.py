import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import gridspec

# Load data
df = pd.read_excel('ACC_players_with_distances.xlsx')

# Define universities to filter
universities = ['University of Louisville', 'Notre Dame', 'Boston College']

# Define bin edges 
bins = list(range(0, 3100, 100))  

# Create the figure and layout
fig = plt.figure(figsize=(15, 6))  
gs = gridspec.GridSpec(1, 3, wspace=0.4)  

# Plot histograms 
for i, university in enumerate(universities):
    ax = plt.Subplot(fig, gs[i])
    uni_distances = df[df['University'] == university]['Distance (miles)']
    uni_filtered_distances = uni_distances[uni_distances <= 3000]
    ax.hist(uni_filtered_distances, bins=bins, edgecolor='black', alpha=0.7)
    ax.set_title(f'{university}', fontsize=16)
    ax.set_xlabel('Distance (miles)', fontsize=13)
    ax.set_ylabel('# of Players', fontsize=13)
    ax.grid(True)
    ax.set_xticks(range(0, 3100, 500))
    ax.set_xticklabels([str(x) for x in range(0, 3100, 500)])
    ax.set_ylim(0, 18)  
    ax.set_yticks(range(0, 19, 2))  
    fig.add_subplot(ax)

plt.tight_layout()  
plt.show()


