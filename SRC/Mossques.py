import osmnx as ox
import geopandas as gpd
import pandas as pd

def main():
    place_name = "Riyadh, Saudi Arabia"
    tags = {
        "amenity": "place_of_worship",
        "religion": "muslim"
    }

    print(f"Downloading mosque data for {place_name} ...")
    mosques = ox.features_from_place(place_name, tags=tags)

    print(f"Total features found: {len(mosques)}")

    mosques_points = mosques[mosques.geometry.type == "Point"].copy()
    mosques_polygons = mosques[mosques.geometry.type == "Polygon"].copy()

    print(f"Points: {len(mosques_points)}")
    print(f"Polygons: {len(mosques_polygons)}")

    mosques_polygons["geometry"] = mosques_polygons.centroid

    mosques_all_points = gpd.GeoDataFrame(
        pd.concat([mosques_points, mosques_polygons], ignore_index=True),
        crs=mosques_points.crs
    )

    output_file = "saudi_arabia_mosques_points.gpkg"
    mosques_all_points.to_file(output_file, driver="GPKG")

    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    main()