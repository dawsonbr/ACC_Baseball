import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load data
df = pd.read_excel('ACC_players_with_distances.xlsx')

# Extract data
distances = df['Distance (miles)']

# Define distance ranges 
bins = [0, 250, 500, 1000, 3000, np.inf]  # Adjust upper bound as needed
range_labels = ['0-250 miles', '251-500 miles', '501-1000 miles', '1001-3000 miles', '> 3001 miles']

# Calculate counts and percentages
counts, _ = np.histogram(distances, bins=bins)
total_count = len(distances)
percentages = [(count / total_count) * 100 for count in counts]

# Format the percentages
percentages_formatted = [f'{int(p)}%' for p in percentages]

# Prepare data for the summary table
summary_data = {
    'Distance Range': range_labels,
    'Count': counts,
    'Percentage': percentages_formatted
}
summary_df = pd.DataFrame(summary_data)

# Plot the summary table as an image
fig, ax = plt.subplots(figsize=(12, 6))  
ax.axis('off')

# Create a table
table = ax.table(cellText=summary_df.values, 
                 colLabels=summary_df.columns, 
                 cellLoc='center', 
                 loc='center',
                 cellColours=[['#f9f9f9' if i % 2 == 0 else '#e0e0e0' for i in range(len(summary_df.columns))] for _ in range(len(summary_df))],
                 rowColours=['#d0e1f9']*len(summary_df),
                 colColours=['#1f77b4']*len(summary_df.columns),
                 edges='closed')  

# Style the table
table.auto_set_font_size(False)
table.set_fontsize(12)  
table.scale(1.6, 1.6)

# Ensure no extra cell colors
for key, cell in table.get_celld().items():
    if key[0] == 0:  
        cell.set_facecolor('#1f77b4')  
    elif key[1] < 0:  
        cell.set_facecolor('none')  
    else:
        cell.set_facecolor(cell.get_facecolor())  



plt.show()
