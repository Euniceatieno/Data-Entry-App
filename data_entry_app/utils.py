from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import redis
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework import status

##############################################################
# Absracted caching logic
###############################################################


def redis_instance():
    # create a redis instance
    return redis.Redis()


class RedisCache(object):
    def __init__(self):
        self.redis = redis_instance()

    def get(self, key):
        # read cache
        return self.redis.get(str(key))

    def set_(self, key, value):
        # set cache
        self.redis.set(str(key), value)


###############################################################
# Abstracted CRUD logic
###############################################################
class BaseCRUDAPIController(APIView):
    model = None
    serializer = None
    redis_cache = RedisCache()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)

    def post(self, request):
        try:
            header = request.headers.get("Authorization", None)
            if header is None:
                return Response(
                    error={f"Access token is missing"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = Token.objects.get(key=header[8:]).user
            request.data["created_by"] = user
            serializer = self.serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()

                # save data to cache
                cache_key = f"Item ID:{request.data.id}"
                self.redis_cache.set_(cache_key, request.data)

                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error creating record : {e} ")

    def delete(self, id):
        # retrieve item from cache
        cached_item = self.redis_cache.get(f"Item ID:{id}")
        if cached_item is None:
            item = self.model.objects.get(id=id)
            if item is None:
                return f"item where id = {id} does not exist"
            else:
                item.delete()
                return Response(
                    status=status.HTTP_200_OK, message="Item successfully deleted"
                )

        else:
            item.delete()
            return Response(
                status=status.HTTP_200_OK, message="Item successfully deleted"
            )

    def put(self, id, request):
        item = self.model.objects.get(id=id)
        if item is None:
            return f"item where id = {id} does not exist"
        else:
            serializer = self.serializer(item, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, id):
        item = self.model.objects.get(id=id)
        if item is None:
            return f"item where id = {id} does not exist"
        else:
            serializer = self.serializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)


###############################################################
# Abstracted filtering logic
###############################################################


@api_view(["POST"])
def filter_records(request, model, serializer):
    try:
        if request.data.date_created:
            professions = model.objects.filter(
                date_created=request.data.date_created
            )
            serializer = serializer(professions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.data.name:
            professions = model.objects.filter(name=request.data.name)
            serializer = serializer(professions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        return f"Error rerieving records : {e} "
