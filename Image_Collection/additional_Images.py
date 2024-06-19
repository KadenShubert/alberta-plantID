import requests
import pandas as pd
import numpy as np
import os

def group_queries(df_q,n_size = 30):
    # Split list of IDs into groups of 30 (page limit for api)
    call_groups = [list(df_q['id'].astype(str))[i:i + n_size] for i in range(0, len(df_q), n_size)]
    # print(df_ids)
    grouped_queries = ['%2C'.join(q) for q in call_groups]
    return grouped_queries

def get_extra_images(df_cur,save_info = True):
    # For each set of 30 ids, go through results and get image ID's
    df_added = pd.DataFrame(columns=df_cur.columns)
    q_count = 0
    add_imgs = 0
    grouped_queries = group_queries(df_cur)
    for query in grouped_queries:
        q_count += 1
        url = f"https://api.inaturalist.org/v1/observations?id={query}&order=desc&order_by=created_at"
        # print(url)

        response = requests.get(url)
        body = response.json()

        # For each observation in results
        for obs in body['results']:
            # print(f'Processing results for observation {obs["id"]}')
            # If there are additional images get their IDs, create a URL, add rows to DF
            # (Additional since this is meant to gather any missing from the original Export)
            if len(obs['observation_photos']) > 1:
                # photo_urls = [x['photo']['url'].replace('square','medium') for x in obs['observation_photos'][1:]]
                # URL Format for images: https://inaturalist-open-data.s3.amazonaws.com/photos/{photo_id}/medium.jpg
                for photo in obs['observation_photos'][1:]:
                    add_imgs += 1
                    add_url = photo['photo']['url'].replace('square','medium')
                    # print(add_url)
                    df_added = pd.concat([df_added, (df_cur.loc[df_cur['id'] == obs['id']].assign(image_url=add_url))], ignore_index=True)
        print(f'Completed query {q_count} of {len(grouped_queries)}.\n{add_imgs} additional images have been collected.')
        print('==='*8)
    # Save image information to be processed/collected
    if save_info: 
        df_added.to_csv("Additional_images-CanadianBuffaloBerry.csv", index=False)
        print(f'Information for {add_imgs} additional images saved as "Additional_images-CanadianBuffaloBerry.csv"')
    df_all = pd.concat([df_added,df_cur], ignore_index=True)
    add_img_count(df_all)    

def add_img_count(df):
    count_occur = {x: 1 for x in df['id'].astype(str)}
    df['id'] = df['id'].astype(str)
    for index,row in df.iterrows():
        obs_id = row['id']
        row['id'] = f'{obs_id}_{count_occur[obs_id]}'
        count_occur[obs_id] += 1
        df.iloc[index] = row
    print(f'Information collected for {df.shape[0]} images.')
    df.to_csv('All_Images_CanadianBuffaloBerry.csv', index=False)
    print('Combined image information saved as "All_Images_CanadianBuffaloBerry.csv"')

def main():
    # Get Canadian Images
    df_obs = pd.read_csv('Canadian_Observations.csv')
    
    if os.path.isfile('Canadian_Observations.csv') and os.path.isfile("Additional_images-CanadianBuffaloBerry.csv"):
        # Use existing files
        df_all = pd.concat([df_obs,pd.read_csv("Additional_images-CanadianBuffaloBerry.csv")], ignore_index=True)
        print('Using previously generated files...')        
        add_img_count(df_all)        
    else:
        print('Gathering additonal image information from observations...')
        get_extra_images(df_obs)        