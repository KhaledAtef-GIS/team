import osmnx as ox
import geopandas as gpd
import pandas as pd

def main():
 
    place_name = "Riyadh, Saudi Arabia"
    tags = {
        "amenity": "school"
    }

    
    # Download OSM data
   
    print(f"Downloading school data for {place_name} ...")
    schools = ox.features_from_place(place_name, tags=tags)

    print(f"Total features found: {len(schools)}")

    
    #  Filter points & polygons
    schools_points = schools[schools.geometry.type == "Point"].copy()
    schools_polygons = schools[schools.geometry.type == "Polygon"].copy()

    print(f"Points: {len(schools_points)}")
    print(f"Polygons: {len(schools_polygons)}")

    # Convert polygons to centroids
    schools_polygons["geometry"] = schools_polygons.centroid

    # Merge all points
    schools_all_points = gpd.GeoDataFrame(
        pd.concat([schools_points, schools_polygons], ignore_index=True),
        crs=schools_points.crs
    )

    print(f"Total points (including polygon centroids): {len(schools_all_points)}")

    # Export to file
    output_file = "saudi_arabia_schools_points.gpkg"
    schools_all_points.to_file(output_file, driver="GPKG")

    print(f"Saved to: {output_file}")

if __name__ == "__main__":
    main()