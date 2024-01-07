import os
import json
import geojson

def convert_linestring_to_polygon(feature_collection_geojson):
    # Load the GeoJSON data
    feature_collection = geojson.loads(feature_collection_geojson)

    # Check if the features are LineStrings
    if feature_collection.type == "FeatureCollection" and all(feature.geometry.type == "LineString" for feature in feature_collection.features):
        # Convert each LineString to a Polygon
        for feature in feature_collection.features:
            coordinates = feature.geometry.coordinates
            coordinates.append(coordinates[0])

            # Update the geometry type and coordinates
            feature.geometry.type = "Polygon"
            feature.geometry.coordinates = [coordinates]

        # Convert to GeoJSON and return the result
        return geojson.dumps(feature_collection, indent=2)

    else:
        return "Input features are not LineStrings in a FeatureCollection"

def read_geojson_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def write_geojson_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# File name for the input and output GeoJSON
input_filename = 'input-cape-verde.geojson'
output_filename = 'output-cape-verde.geojson'

# Read input GeoJSON from file
input_geojson = read_geojson_from_file(input_filename)

# Example usage:
output_geojson = convert_linestring_to_polygon(input_geojson)

# Write the output GeoJSON to a file
write_geojson_to_file(output_filename, output_geojson)

print("Input GeoJSON:")
print(input_geojson)
print("\nOutput GeoJSON:")
print(output_geojson)

# Validate the output GeoJSON
try:
    geojson.loads(output_geojson)
    print("\nOutput GeoJSON is valid.")
except ValueError as e:
    print("\nError: Output GeoJSON is not valid.")
    print(e)
