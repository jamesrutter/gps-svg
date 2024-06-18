import geojson
from shapely.geometry import shape 
import svgwrite 

def geojson_to_svg_1(geojson_file, svg_file):
    with open(geojson_file) as f:
        gj = geojson.load(f)
    # Create a new SVG figure
    dwg = svgwrite.Drawing(svg_file, profile='tiny')
    for feature in gj['features']:
        geom = shape(feature['geometry'])
        if geom.geom_type == 'Polygon':
            dwg.add(dwg.polygon(points=geom.exterior.coords, fill='none', stroke='black'))
        elif geom.geom_type == 'MultiPolygon':
            for polygon in geom:
                dwg.add(dwg.polygon(points=polygon.exterior.coords, fill='none', stroke='black'))
    dwg.save()
    
def geojson_to_svg_2(geojson_file, svg_file):
    with open(geojson_file, 'r') as f:
        data = geojson.load(f)

    features = data['features']
    dwg = svgwrite.Drawing(svg_file, profile='tiny')

    for feature in features:
        geom = shape(feature['geometry'])
        if geom.geom_type == 'LineString':
            points = [(x, -y) for x, y in geom.coords]  # Invert y-axis for correct orientation
            dwg.add(dwg.polyline(points, stroke=svgwrite.rgb(0, 0, 0, '%'), fill='none'))

    dwg.save()
    
# Example usage
geojson_to_svg_1('trail.geojson', 'trail1.svg')
geojson_to_svg_2('trail.geojson', 'trail2.svg')