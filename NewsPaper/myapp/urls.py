from django.urls import path
from .views import PostList, PostDetail, SearchList, PostAdd, PostEdit, PostDelete
from django.views.decorators.cache import cache_page
 
urlpatterns = [
    path('', cache_page(60)(PostList.as_view())),
    path('<int:pk>', cache_page(20)(PostDetail.as_view())),
    path('search/', cache_page(300)(SearchList.as_view())),
    path('add/', PostAdd.as_view()),
    path('<int:pk>/edit/', PostEdit.as_view()),
    path('<int:pk>/delete/', PostDelete.as_view()),
]