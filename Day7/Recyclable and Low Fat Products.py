import pandas as pd

data = {
    "product_id"    :[0,1,2,3,4,5],
    "low_fats"      :['Y','N','Y','N','Y','Y'],
    "recyclables"   :['Y','N','Y','N','Y','Y'],
}

df = pd.DataFrame(data)

filtered_data = df[(df['low_fats'] == 'Y') & (df['recyclables'] == 'Y')]

results = filtered_data[['product_id']]

print(results)