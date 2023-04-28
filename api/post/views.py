from rest_framework.response import Response
from rest_framework import generics, permissions, status
from api.post.models import Post
from api.post.permission import IsOwnerOrReadOnly


from api.post.serializers import PostCreateSerializer

# Create your views here.
class PostCreateAPIView(generics.CreateAPIView):
    
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = PostCreateSerializer

    def create(self, request):
        data = request.data
        serializer = self.serializer_class(data=data,context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class PostDeleteAPIView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Post.objects.all()
    lookup_field = "id"

    def delete(self, request, id):
        try:
            post = Post.objects.get(id=id)
            self.destroy(request)
            return Response("Post deleted successful", status=status.HTTP_204_NO_CONTENT)
        except Post.DoesNotExist:
            return Response("Post does not exist", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response("Error occur while deleting post")