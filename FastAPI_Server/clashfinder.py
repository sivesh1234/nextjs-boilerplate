import pandas as pd



def clashfinder_Function(array_of_acts):
    # Check if array_of_acts is empty or contains only empty strings
    if not array_of_acts or all(not act.strip() for act in array_of_acts):
        return []
    acts_to_remove = ['Diddy Sweg', '10 Yrs Of Jungle Cakes - Burt Cope, Deekline, Ed Solo & Maddy V']
    # Load the lineup data from the uploaded CSV file
    file_path = './Lineup.csv'
    lineup_df = pd.read_csv(file_path)

    # Combine date and time columns to create Start DateTime and Finish DateTime columns
    lineup_df['Start DateTime'] = pd.to_datetime(lineup_df['Start Date'] + ' ' + lineup_df['Start'], format='%d/%m/%Y %H:%M')
    lineup_df['Finish DateTime'] = pd.to_datetime(lineup_df['Finish Date'] + ' ' + lineup_df['Finish'], format='%d/%m/%Y %H:%M')

    # Filter the dataframe to include only the acts we're interested in
    filtered_df = lineup_df[lineup_df['Act'].str.contains('|'.join(array_of_acts), case=False, na=False)].reset_index(drop=True)

    # Remove the acts that are in the acts_to_remove list
    filtered_df = filtered_df[~filtered_df['Act'].str.contains('|'.join(acts_to_remove), case=False, na=False)].reset_index(drop=True)

    # Display the filtered dataframe to manually inspect the relevant columns
    print(filtered_df[['Act', 'Start DateTime', 'Finish DateTime']])

    # Initialize a list to store clashes
    clashes = []

    # Check for clashes between the acts
    for i in range(len(filtered_df)):
        for j in range(i + 1, len(filtered_df)):
            start_i = filtered_df.loc[i, 'Start DateTime']
            end_i = filtered_df.loc[i, 'Finish DateTime']
            start_j = filtered_df.loc[j, 'Start DateTime']
            end_j = filtered_df.loc[j, 'Finish DateTime']

            # Check if the time ranges overlap
            if start_i < end_j and start_j < end_i:
                clash_day = start_i.strftime('%A')
                clash = {
                    "artists": [filtered_df.loc[i, 'Act'], filtered_df.loc[j, 'Act']],
                    "stages": [filtered_df.loc[i, 'Stage'], filtered_df.loc[j, 'Stage']],
                    "start": max(start_i, start_j).isoformat(),
                    "end": min(end_i, end_j).isoformat(),
                    "day": clash_day
                }
                clashes.append(clash)

    # Output the clashes
    return clashes

# Example usage:
array_of_acts = ["Diddy Sweg", "Act2", "Act3"]
acts_to_remove = ["Act2"]
clashes = clashfinder_Function(array_of_acts)
print(clashes)
