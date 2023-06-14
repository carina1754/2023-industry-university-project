import pandas as pd

# Load the DataFrame
df = pd.read_csv('df_reservation.csv')

# Filter the DataFrame for rows where the dogName is '또복이'
dog_rows = df[df['dogName'] == '또복이']

# Concatenate the 'deptAddress' and 'destAddress' columns into one
addresses = pd.concat([dog_rows['deptAddress'], dog_rows['destAddress']])

# Get the top 5 most common addresses
top_5_addresses = addresses.value_counts().head(5)

# Write the top 5 addresses to a txt file
with open('top_5_addresses.txt', 'w') as file:
    for address, count in top_5_addresses.items():
        file.write(f'{address}: {count}\n')
