import pandas as pd

# Load the DataFrame
df = pd.read_csv('df_reservation.csv')

# Filter the DataFrame for rows where the dogName is '또복이'
dog_rows = df[df['dogName'] == '또복이']

# Get the 'destAddress' column
dest_addresses = dog_rows['destAddress']

# Get the top 5 most common destination addresses
top_5_dest_addresses = dest_addresses.value_counts().head(5)

# Write the top 5 destination addresses to a txt file
with open('top_5_destination_addresses.txt', 'w') as file:
    for address, count in top_5_dest_addresses.items():
        file.write(f'{address}: {count}\n')

