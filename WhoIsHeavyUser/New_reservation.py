import pandas as pd

# Load the DataFrame
df = pd.read_csv('df_reservation.csv')

# Read the top 5 duplicated dog names from the txt file
with open('top_5_duplicated_dog_names.txt', 'r') as file:
    top_5_names = [line.strip() for line in file]

# Remove all rows where the dogName is in top_5_names
df = df[~df['dogName'].isin(top_5_names)]

# Print the total number of remaining cases
print(f"Total number of remaining cases: {len(df)}")

# Write the remaining data to a new csv file
df.to_csv('filtered_def_reservation.csv', index=False)
