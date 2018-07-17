import math
from ....settings import GOOGLE_KEY
import googlemaps


class Gmaps:
    __gmaps = googlemaps.Client(key=GOOGLE_KEY)

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

    def create_address_reverse(self, descricao_endereco):
        address_full = self.__gmaps.geocode(address=descricao_endereco)
        try:
            address = address_full[0]['geometry']['viewport']['northeast']
        except:
            address = address_full[0]['geometry']['viewport']['southwest']

        return address


    def shorter_distance(self, lat1, lon1, lat2, lon2):

        R = 6371.
        x = (lon2 - lon1) * math.cos((lat2 + lat1) / 2.)
        y = lat2 - lat1
        return math.sqrt(x ** 2 + y ** 2) * R

    def shorter_distance_address(self, current_address=None, destination_address=[]):
        if current_address:
            distances = []
            list_address = []
            for destination in destination_address:
                distances.append((destination,
                                  self.shorter_distance(float(current_address['lat']),
                                                        float(current_address['lng']),
                                                        float(destination.imovel.address.latitude),
                                                        float(destination.imovel.address.longitude)
                                                        )
                                 ))
            distances.sort(key=lambda x: x[1])
            list_address.append(distances[0][0])
            return list_address
        return destination_address
