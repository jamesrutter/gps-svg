import geojson
from shapely.geometry import shape, MultiLineString, Polygon


def preprocess_coordinates(coords):
    # Extract only the first two dimensions (longitude and latitude)
    return [[(x, y) for x, y, _, _ in line] for line in coords]

def geojson_to_svg(geojson_file, svg_file):
    print(f'Converting {geojson_file} to SVG...')
    svg_content = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">'
    
    with open(geojson_file, 'r') as f:
        gj_data = geojson.load(f)

    features = gj_data['features']
    for feature in features:
        geometry = feature['geometry']
        if geometry['type'] == 'MultiLineString':
            preprocessed_coords = preprocess_coordinates(geometry['coordinates'])
            geom = MultiLineString(preprocessed_coords)
            svg_content += geom.svg()
        elif geometry.geom_type == 'Polygon':
            # handle polygons here 
            processed_coords = preprocess_coordinates(geometry.exterior.coords)
            geom = Polygon(processed_coords)
            svg_content += geom.svg()
        elif geometry.geom_type == 'MultiPolygon':
            for polygon in geometry:
                processed_coords = preprocess_coordinates(polygon.exterior.coords)
                geom = Polygon(processed_coords)
                svg_content += geom.svg()

    svg_content += '</svg>'

    with open(svg_file, 'w') as f:
        f.write(svg_content)
        print(f'SVG file saved to {svg_file}')

# Example usage
geojson_to_svg('data/trail.geojson', 'output/trail.svg')