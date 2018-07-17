import googlemaps


class Gmaps:
    __gmaps = googlemaps.Client(key='AIzaSyCSZtX_qV_ltqQ0azDtbdlpA9-fxmNW9Cs')

    def create_address(self, lat, lng):
        address = {}
        reverse_geocode_result = self.__gmaps.reverse_geocode((lat, lng))
        address_componentes = reverse_geocode_result[0]['address_components']

        address['number']   = address_componentes[0]['long_name']
        address['street']   = address_componentes[1]['long_name']
        address['street']  += ', {}'.format(address_componentes[2]['long_name'])
        try:
            address['zip_code'] = address_componentes[7]['long_name']
        except:
            address['zip_code'] = ''

        address['latitude']  = float(lat)
        address['longitude'] = float(lng)

        return address
