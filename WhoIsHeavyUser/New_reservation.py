import pandas as pd

# Load the DataFrame
df = pd.read_csv('reservation.csv')

# Create a new column by combining 'dogName' and 'dogSize'
df['dogIdentity'] = df['dogName'] + df['dogSize']

# Read the top 5 duplicated dog names and sizes from the txt file
top_5_names = []
with open('top_5_duplicated_dog_names.txt', 'r') as file:
    for line in file:
        # Split the line at the ':', and get only the dog's name
        name, _ = line.split(":")
        # If there is a comma in the name, split again to get the individual names
        if "," in name:
            names = name.split(",")
            top_5_names.extend(names)
        else:
            top_5_names.append(name)

# Trim leading/trailing white space from the names
top_5_names = [name.strip() for name in top_5_names]

# Remove all rows where the 'dogName' is in top_5_names
df = df[~df['dogName'].isin(top_5_names)]

# Print the total number of remaining cases
print(f"Total number of remaining cases: {len(df)}")

# Write the remaining data to a new csv file
df.to_csv('filtered_reservation.csv', index=False)
