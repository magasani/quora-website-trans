from django.urls import path

from . import views

urlpatterns = [
    path('',views.Home,name='homes'),
    path('logins/',views.login_view,name='logins'),
    path('questionlist/',views.question_list,name='questionslist'),
    path('logouts/',views.logout_view,name='logouts'),
    path('register/',views.register_view,name='registeruser'),
    path('answerqe/<int:pk>',views.view_question,name='answerquestion'),
    path('viewanswer/',views.view_answer,name='viewanswers'),
    path('postques/',views.post_question,name='postquestion'),
    path('like/<int:answer_id>',views.like_answer,name='like'),
    path('likes/',views.view_likes,name='viewlike')

]