import antigravity
import sys


def get_geohash():
    if len(sys.argv) == 4:
        try:
            latitude = float(sys.argv[1])
            longitude = float(sys.argv[2])
            datedow = sys.argv[3].encode('utf-8')
            antigravity.geohash(latitude, longitude, datedow)
        except Exception as e:
            print(e)
    else:
        print('Wrong arguments. You need: latitude, longitude and datedow')


if __name__ == '__main__':
    get_geohash()
