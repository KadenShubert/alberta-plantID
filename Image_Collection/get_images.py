import requests
import pandas as pd

def main():
    url_df = pd.read_csv("All_Images_CanadianBuffaloBerry.csv")
    num_images = len(url_df)
    img_folder = 'images'
    
    print(f'Downloading {num_images} images...')

    url_df['image_name'] = url_df['id'].apply(lambda x: 'CanadianBuffaloBerry_'+str(x)+'.jpg')
    url_df.drop(columns=['id'], inplace=True)
    # url_df.apply(image_and_csv, axis=1)

    for i, row in url_df.iterrows():
        url,name = row.loc['image_url'],row.loc['image_name']
        data = requests.get(url).content
        f = open(f'{img_folder}/{name}', 'wb')
        f.write(data)
        f.close()
        print(f'Processing image {(i + 1)} / {num_images} ({round(((i + 1) / num_images) * 100, 1)}%)',
            end="\r")

    print('Saving image information to "CanadianBuffaloBerry_Canada_Info.csv"')
    url_df.to_csv('CanadianBuffaloBerry_Canada_Info.csv', index=False)