from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializers
from blog.models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET','POST'])
def postList(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        


@api_view()
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=True)
    serializer = PostSerializers(post)
    return Response(serializer.data)

    # try:
    #     post = Post.objects.get(pk=id)
    #     serializer = PostSerializers(post)
    #     return Response(serializers.data)
    # except Post.DoesNotExist:
    #     '''
    #     post not found
    #     '''
    #     return Response({'detail':'Post not found'},status= 404)
    #     return Response({'detail':'Post not found'},status=status.HTTP_404_NOT_FOUND)
