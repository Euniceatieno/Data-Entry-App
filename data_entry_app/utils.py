from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


###############################################################
# Abstracted CRUD logic
###############################################################
class BaseCRUDAPIController(APIView):
    def __init__(self, model, serializer):
        self.model = model
        self.serializer = serializer

    def create_model_entry(self, request):
        try:
            serializer = self.serializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(f"Error creating record : {e} ")

    def delete_model_entry(self, id):
        item = self.model.objects.get(id=id)
        if item is None:
            return f"item where id = {id} does not exist"
        else:
            item.delete()
            return Response(
                status=status.HTTP_200_OK, message="Item successfully deleted"
            )

    def update_model_entry(self, id, request):
        item = self.model.objects.get(id=id)
        if item is None:
            return f"item where id = {id} does not exist"
        else:
            serializer = self.serializer(item, request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_all_entries(self):
        try:
            items = self.model.objects.all()
            serializer = self.serializer(items, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return f"Error rerieving records : {e} "

    @classmethod
    def get_model_entry(self, id):
        item = self.model.objects.get(id=id)
        if item is None:
            return f"item where id = {id} does not exist"
        else:
            serializer = self.serializer(item)
            return Response(serializer.data, status=status.HTTP_200_OK)
