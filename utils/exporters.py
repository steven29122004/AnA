def export_kml(path, nodes_data, filename="route.kml"):
    kml_header = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>
    <Style id="routeStyle"><LineStyle><color>ff0000ff</color><width>5</width></LineStyle></Style>
    <Placemark><styleUrl>#routeStyle</styleUrl><LineString><coordinates>"""
    
    coords = []
    for node_id in path:
        if node_id in nodes_data:
            node = nodes_data[node_id]
            coords.append(f"{node['x']},{node['y']},0")
    
    kml_footer = """</coordinates></LineString></Placemark></Document></kml>"""
    
    with open(filename, "w") as f:
        f.write(kml_header + "\n".join(coords) + kml_footer)