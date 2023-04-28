from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework import permissions, status, generics

from api.post.models import Post
from api.services.models import Reaction
from api.services.serializers import CommentSerializer, ReactionSerializer

# Create your views here.

class ReactionAPIView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ReactionSerializer

    def get(self, request, id):
        try:
            post = Post.objects.get(id=id)
            reaction = Reaction.objects.get(post=post, user=request.user)
            reaction.delete()
        except Reaction.DoesNotExist:
            pass
        data = {"post": post.id, "user": request.user, "reaction": reaction}
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, id):
        try:
            post = Post.objects.get(id=id)
            user = request.user
            reaction = request.data.get("reaction")
            try:
                _reaction,_is_reaction = Reaction.objects.get_or_create(post=post, user=user)
                response = f"{request.user.email} {'LIKE' if reaction in [1,'1'] else 'DISLIKE'} on {post.title}"
                _reaction.reaction=reaction
                _reaction.save()
                return Response(response)
            except Reaction.DoesNotExist:
                return Response("Opps something bad Happended")
        except Post.DoesNotExist:
            return Response("Post does not exits")
        
class CommentAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def post(self, request, id):
        try:
            post = Post.objects.get(id=id)
            comment = request.data
            comment["post"] = post.id
            comment["user"] = request.user.id
            serializer = self.serializer_class(data=comment)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            raise NotFound("Post does not exist")

@api_view(('GET',))
def get_post(request, id):
    post = get_object_or_404(Post,id=id)
    no_of_likes = Reaction.objects.filter(post=post, reaction=1).count()
    total_comments = post.comments.count()
    data = {
        'post_id': post.id,
        'no_of_likes': no_of_likes,
        'total_comments': total_comments
    }
    return Response(data,status=status.HTTP_200_OK)