import osmnx as ox
import geopandas as gpd
import pandas as pd

def main():
   
    # Define area & tags
 
    place_name = "Riyadh, Saudi Arabia"
    tags = {
        "amenity": "hospital"
    }

  
    # Download OSM data

    print(f"Downloading hospital data for {place_name} ...")
    hospitals = ox.features_from_place(place_name, tags=tags)

    print(f"Total features found: {len(hospitals)}")


    # Filter points & polygons
    
    hospitals_points = hospitals[hospitals.geometry.type == "Point"].copy()
    hospitals_polygons = hospitals[hospitals.geometry.type == "Polygon"].copy()

    print(f"Points: {len(hospitals_points)}")
    print(f"Polygons: {len(hospitals_polygons)}")

   
    # Convert polygons to centroids

    hospitals_polygons["geometry"] = hospitals_polygons.centroid

  
    # Merge all points
 
    hospitals_all_points = gpd.GeoDataFrame(
        pd.concat([hospitals_points, hospitals_polygons], ignore_index=True),
        crs=hospitals_points.crs
    )

    print(f"Total points (including polygon centroids): {len(hospitals_all_points)}")

   
    # Export to file

    output_file = "saudi_arabia_hospitals_points.gpkg"
    hospitals_all_points.to_file(output_file, driver="GPKG")

    print(f" Saved to: {output_file}")

if __name__ == "__main__":
    main()