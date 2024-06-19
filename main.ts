import 'npm:@turf/turf';

function geojsonToSVG(geojsonFile: string, svgFile: string) {
  const data = Deno.readFileSync(geojsonFile);

  console.log(data);

  let svgContent = '<svg xmlns="http://www.w3.org/2000/svg" version="1.1">';

  data.features.forEach((feature) => {
    const geom = feature.geometry;
    if (geom.type === 'LineString') {
      const coordinates = geom.coordinates.map((coord) => `${coord[0]},${-coord[1]}`).join(' ');
      svgContent += `<polyline points="${coordinates}" stroke="black" fill="none"/>`;
    }
  });

  svgContent += '</svg>';

  fs.writeFileSync(svgFile, svgContent, 'utf8');
}

// Example usage
geojsonToSVG('trail.geojson', 'trail.svg');
