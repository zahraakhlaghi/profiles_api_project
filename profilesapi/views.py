from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profilesapi import serializerss
from rest_framework import viewsets

class HelloApiView(APIView):
    """Test API view"""
    serializer_class=serializerss.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView features"""
        an_apiview = [
             'Uses HTTP methods as function (get,post,patch,put,delete)',
             'Is similar to a traditional Django View',
             'Gives you the most control over you application logic',
             'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello','an_apiview':an_apiview})

    def post(self,request):
        """Create a hello message with our name"""
        serial=self.serializer_class(data=request.data)

        if serial.is_valid():
          name=serial.validated_data.get('name')
          message='Hello '+str(name)
          return Response({'message':message})

        else:
            return Response(
                serial.errors,
                status=status.HTTP_400_BAD_REQUEST
            )  

    def put(self,request,pk=None):
        """Handle updatig an object"""
        return Response({'method': 'PUT'})

    def patch(self,request,pk=None):
        """Handle a partial update of an object"""
        return Response({'method':'PATCH'})    
 
    def delete(self,request,pk=None):
        """Delete on object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test api ViewSet"""
    serializer_class=serializerss.HelloSerializer

    def list(self,request):
        """Return a hello message"""
        a_viewset=[
            'Use actions (list,create,retrieve,partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionally with less code'
        ]
        
        return Response({'message':'Hello!','a_viewset':a_viewset})
         
    def create(self,request):
        serializ=self.serializer_class(data=request.data)

        if serializ.is_valid:
            name=serializ.validated_data.get.name('name')
            message='Hello '+str(name)
            return Response({'message':message})

        else:
            return Response(
                serializ.errors,
                status=status.HTTP_400_BAD_REQUEST) 

    def retrieve(self,request,pk=None):
        return Response({'Http_method':'GET'}) 

    def update(self,request,pk=None):
        return Response({'Http_method':'PUT'})     

    def partial_update(self,request,pk=None):
        return Response({'Http_method':'PATCH'})       

    def destroy(self,request,pk=None):
        return Response({'Http_method':'DELETE'})        
