from django.http import JsonResponse
import json
import sys
sys.path.append('../../')
import myoutlet.db_ops.db as db

DEFAULT_OFFSET = 100

def index(request):
    if request.method == 'GET':
        try:
            body = request.GET.dict()
            userid = body['_id']
            lat = float(body['latitude'])
            long = float(body['longitude'])

            collection = db.get_collection()
            data = db.query_nearby_users(collection, userid, DEFAULT_OFFSET, lat, long)
            return JsonResponse({
                'status': 200,
                'data': json.dumps(data),
            })
        except:
            print("Something went wrong with GET request for /nearbyusers")
        
    return JsonResponse({
        'status': 400,
    })


