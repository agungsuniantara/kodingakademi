from flask import Flask, render_template, request, jsonify
import requests
import logging
from shapely.geometry import Point
import geopandas as gpd
import pandas as pd
import numpy as np

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

GOOGLE_MAPS_API_KEY = 'AIzaSyBgLXMmx_qx8EQ3PCIpe69WTkj9JxFZXzU'
GOOGLE_GEOCODING_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"
GOOGLE_PLACES_API_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"

RADIUS = 300  

shapefiles = [
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIDESA_AR_denpasar.shp', 
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIDESA_AR_karangasem.shp', 
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIKECAMATAN_AR_tabanan.shp', 
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIKECAMATAN_AR_badung.shp', 
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIKECAMATAN_AR_bangli.shp', 
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIKECAMATAN_AR_buleleng.shp', 
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIKECAMATAN_AR_gianyar.shp', 
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIKECAMATAN_AR_jembrana.shp', 
    '/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/shapefile/ADMINISTRASIKECAMATAN_AR_klungkung.shp'
]

gdfs = []
for shapefile in shapefiles:
    gdf_temp = gpd.read_file(shapefile)
    if gdf_temp.crs is None:
        gdf_temp = gdf_temp.set_crs(epsg=4326)
    gdfs.append(gdf_temp)

gdf = pd.concat(gdfs, ignore_index=True)
gdf = gdf.to_crs(epsg=4326)

population_data = pd.read_csv('/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/jumlah_penduduk_bali.csv')
ruko_data = pd.read_csv('/Applications/MAMP/htdocs/local/kodingakademi/Python/pkl/data_ruko_tanah.csv')

@app.route('/')
def input_page():
    return render_template('index.html')

@app.route('/pemetaan')
def pemetaan():
    return render_template('peta.html')

@app.route('/properti')
def properti():
    area = request.args.get('area')
    filtered_ruko = ruko_data

    if area:
        filtered_ruko = ruko_data[ruko_data['Place'].str.contains(area, case=False, na=False)]

    ruko_list = filtered_ruko.to_dict('records')
    return render_template('properti.html', ruko_list=ruko_list)

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        logging.debug(f'Received data: {data}')
        competitors = data.get('competitors', [])
        areas = data.get('area', [])
        facilities = data.get('facilities', [])

        if not areas:
            return jsonify({'error': 'Area is required'}), 400

        results = []
        matched_ruko = []

        sub_area_mapping = {
            'serangan': 'denpasar selatan', 'pedungan': 'denpasar selatan', 'sesetan': 'denpasar selatan',
            'panjer': 'denpasar selatan', 'renon denpasar': 'denpasar selatan', 'sanur': 'denpasar selatan',
            'sidakarya': 'denpasar selatan', 'pemogan': 'denpasar selatan', 'sanur kaja': 'denpasar selatan',
            'sanur kauh': 'denpasar selatan', 'kesiman': 'denpasar selatan', 'sumerta': 'denpasar selatan',
            'kesiman': 'denpasar timur', 'sumerta': 'denpasar timur', 'dangin puri': 'denpasar timur',
            'penatih': 'denpasar timur', 'dangin puri kelod': 'denpasar timur', 'sumerta kelod': 'denpasar timur',
            'kesiman petilan': 'denpasar timur', 'kesiman kertalangu': 'denpasar timur', 'sumerta kaja': 'denpasar timur',
            'sumerta kauh': 'denpasar timur', 'penatih dangin puri': 'denpasar timur', 'dauh puri': 'denpasar barat',
            'pemecutan': 'denpasar barat', 'padangsambian': 'denpasar barat', 'padangsambian kelod': 'denpasar barat',
            'dauh puri kauh': 'denpasar barat', 'dauh puri kelod': 'denpasar barat', 'dauh puri kangin': 'denpasar barat',
            'tegal harum': 'denpasar barat', 'tegal kertha': 'denpasar barat', 'padangsambian kaja': 'denpasar barat',
            'tonja denpasar': 'denpasar utara', 'ubung': 'denpasar utara', 'peguyangan': 'denpasar utara',
            'dangin puri kangin': 'denpasar utara', 'dangin puri kauh': 'denpasar utara', 'dangin puri kaja': 'denpasar utara',
            'pemecutan kaja': 'denpasar utara', 'dauh puri kaja': 'denpasar utara', 'ubung kaja': 'denpasar utara',
            'peguyangan kaja': 'denpasar utara', 'peguyangan kangin': 'denpasar utara', 
        }

        for area in areas:
            area_lower = area.lower()
            if area_lower in sub_area_mapping:
                area_lower = sub_area_mapping[area_lower]

            geocode_params = {
                'address': area,
                'key': GOOGLE_MAPS_API_KEY
            }
            geocode_response = requests.get(GOOGLE_GEOCODING_API_URL, params=geocode_params).json()
            logging.debug(f'Geocode response for {area}: {geocode_response}')

            if not geocode_response.get('results'):
                logging.error(f'Area not found: {area}')
                continue

            location = geocode_response['results'][0]['geometry']['location']
            lat, lng = location['lat'], location['lng']

            def is_within_shapefile(lat, lng):
                point = Point(lng, lat)
                within = gdf.contains(point).any()
                logging.debug(f'Point ({lat}, {lng}) within shapefile: {within}')
                return within

            if not is_within_shapefile(lat, lng):
                logging.error(f'The specified area is not within the target shapefiles: {area}')
                continue

            matching_population = population_data[population_data['wilayah'].str.contains(area, case=False, na=False)]
            if matching_population.empty:
                logging.error(f'Population data not found for the specified area: {area}')
                continue

            kabupaten = matching_population['kabupaten'].values[0]
            population_count = int(matching_population['penduduk'].values[0])

            for _, row in ruko_data.iterrows():
                kecamatan, ruko_kabupaten = row['Place'].split(', ')
                if (kabupaten.lower() == ruko_kabupaten.lower()) or (area_lower in kecamatan.lower()):
                    matched_ruko.append({
                        'Product Name': row['Product Name'],
                        'Price': row['Price'],
                        'Place': row['Place'],
                        'Link': row['Link']
                    })

            competitors_locations = []
            for competitor in competitors:
                params = {
                    'key': GOOGLE_MAPS_API_KEY,
                    'query': f'{competitor} in {area}',
                    'location': f'{lat},{lng}',
                    'radius': RADIUS
                }
                response = requests.get(GOOGLE_PLACES_API_URL, params=params).json()
                logging.debug(f'Places API response for {competitor} in {area}: {response}')

                if response.get('results'):
                    for place in response.get('results', []):
                        place_lat = place['geometry']['location']['lat']
                        place_lng = place['geometry']['location']['lng']
                        if is_within_shapefile(place_lat, place_lng):
                            competitors_locations.append({
                                'name': place['name'],
                                'lat': place_lat,
                                'lng': place_lng
                            })

            public_facilities = []
            for facility in facilities:
                params = {
                    'key': GOOGLE_MAPS_API_KEY,
                    'query': f'{facility} in {area}',
                    'location': f'{lat},{lng}',
                    'radius': RADIUS
                }
                response = requests.get(GOOGLE_PLACES_API_URL, params=params).json()
                logging.debug(f'Places API response for {facility} in {area}: {response}')

                if response.get('results'):
                    for place in response.get('results', []):
                        place_lat = place['geometry']['location']['lat']
                        place_lng = place['geometry']['location']['lng']
                        if is_within_shapefile(place_lat, place_lng):
                            public_facilities.append({
                                'name': place['name'],
                                'lat': place_lat,
                                'lng': place_lng,
                                'type': facility
                            })

            result = {
                'area': area,
                'area_lat': lat,
                'area_lng': lng,
                'population': population_count,
                'competitors': competitors_locations,
                'facilities': public_facilities,
            }
            results.append(result)

        if not matched_ruko:
            logging.info(f'No ruko found for areas: {areas}')
            return jsonify({'results': results, 'ruko': []})

        return jsonify({'results': results, 'ruko': matched_ruko})

    except Exception as e:
        logging.error(f'Error: {e}')
        return jsonify({'error': 'An error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True)