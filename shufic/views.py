from django.shortcuts import render, redirect
from shufic.models import Video, Comment
from django.http import HttpResponse
from django.template.context_processors import csrf
from django.contrib import auth
from . import forms

def hello(request, video_id):
   return HttpResponse("<h1>!!!!!!!!!!!!!!</h1>")

def addlikes(request, video_id):
   if video_id not in request.COOKIES:
      video = Video.objects.get(id=video_id)
      video.Video_like += 1
      video.save()
      if request.path.split('/')[2][0] == 'V':
         response = redirect("/videoshufic/")
      else:
         response =  redirect("/videoshufic/onevideo/" + str(video_id))
      response.set_cookie(video_id, "test")
      return response
   if request.path.split('/')[2][0] == "V":
      return redirect("/videoshufic/")
   return redirect("/videoshufic/onevideo/" + str(video_id))

def onevideo(request, video_id):
   comment_form = forms.CommentForm
   args = {}
   args.update(csrf(request))
   args['video'] = Video.objects.get(id=video_id)
   args['comments'] = Comment.objects.filter(comment_video_id=video_id)
   args['forms'] = comment_form
   args['username'] = auth.get_user(request).username
   return render(request, 'onevideo.html', args)


def addcomment(request, video_id):
   if request.POST and ('pause' not in request.session):
      forma = forms.CommentForm(request.POST)
      if forma.is_valid():
         comment = forma.save(commit=False)
         comment.comment_video = Video.objects.get(id=video_id)
         forma.save()
         request.session.set_expiry(60)
         request.session['pause'] = True
   return redirect('/videoshufic/onevideo/%s/' % video_id)


def Hello(request):
   class content(Video):
      comments = ""
   content_list = []
   for i in Video.objects.all():
      j = content()
      j.Video_URL = i.Video_URL
      j.Video_title = i.Video_title
      j.Video_o = i.Video_o
      j.Video_like = i.Video_like
      j.id = i.id
      j.comments = Comment.objects.filter(comment_video_id=i.id)
      content_list.append(j)
   return render(request, 'videop.html', {'urls': content_list, 'username': auth.get_user(request).username})


