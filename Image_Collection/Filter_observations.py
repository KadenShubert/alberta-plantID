import pandas as pd

# 'observations_Full.csv' Information collected from: https://www.inaturalist.org/observations/export

# Query: has[]=photos&license=cc0&photo_license=cc0&identifications=most_agree&iconic_taxa[]=Plantae&taxon_ids[]=79072

# Columns: id, observed_on_string, observed_on, time_observed_at, quality_grade, license, url, image_url, tag_list,
# captive_cultivated, place_guess, latitude, longitude, positional_accuracy, private_place_guess, coordinates_obscured,
# place_town_name, place_county_name, place_state_name, place_country_name, species_guess, scientific_name, common_name,
# iconic_taxon_name, taxon_id

def main():    
    # Get full dataset as dataframe
    print('Filtering "observations_Full.csv" for Canadian observations')
    df_all = pd.read_csv('observations_Full.csv', usecols=['id', 'url', 'image_url', 'place_country_name'])
    print(f'Total observations: {df_all.shape[0]}')
    
    # Filter dataframe to only have Canadian observations
    df_filtered = df_all.loc[df_all['place_country_name'] == 'Canada'].drop(columns=['place_country_name'])
    print(f'Canadian observations: {df_filtered.shape[0]}')    
    
    # Save filtered df to csv
    df_filtered.to_csv('Canadian_Observations.csv', index=False)
    print('Filtered observations saved as "Canadian_Observations.csv"')