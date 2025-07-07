import pandas as pd
import folium
import json

pop_df = pd.read_csv("tokyo.csv", delim_whitespace=True)

islands = ['大島町','利島村','新島村','神津島村','三宅村','御蔵島村','八丈町','青ヶ島村','小笠原村']
pop_df = pop_df[~pop_df["City"].isin(islands)]

pop_df["Population"] = pd.to_numeric(pop_df["Population"].str.replace(",", ""), errors="coerce")
pop_df["City"] = pop_df["City"].str.split("_").str[-1]

pop_df



# https://github.com/dataofjapan/land/blob/master/tokyo.geojson
with open('tokyo.geojson', encoding='utf-8') as f:
    geo_data = json.load(f)
    
geo_data["features"] = [
    feature for feature in geo_data["features"]
    if feature["properties"].get("ward_ja", "") not in islands and feature["properties"].get("ward_ja", "") != "所属未定地"
]

tokyo_map = folium.Map(location=[35.6895, 139.6917], zoom_start=10)

folium.Choropleth(
    geo_data=geo_data,
    data=pop_df,
    columns=["City", "Population"],
    key_on="feature.properties.ward_ja",
    fill_color="YlOrRd",
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name="人口"
).add_to(tokyo_map)

tokyo_map.save("tokyo_population_map.html")

pop_df_sorted = pop_df.sort_values('Population', ascending=False)
top5 = pop_df_sorted.head(5)
bottom5 = pop_df_sorted.tail(5)
print("Top 5 populations:\n", top5[['City','Population']])
print("\nBottom 5 populations:\n", bottom5[['City','Population']])

