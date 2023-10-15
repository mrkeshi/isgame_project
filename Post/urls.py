from django.urls import path
from . import views

urlpatterns = [
    path('article', views.PostManger.as_view(), name="post_admin"),
    path('article/add', views.PostAdd.as_view(), name="post_add_admin"),
    path('article/<int:id>', views.EditPost.as_view(), name="post_edit_admin"),
    path('article/delete/', views.PostDelete, name="post_delete_admin"),
    path('article/filter',views.ListPost,name="filter_article_admin"),

    path('tag',views.TagManer.as_view(),name="tag_admin"),
    path('tag/add',views.TagAdd.as_view(),name="tag_add_admin"),
    path('tag/<int:id>',views.EditTag.as_view(),name="tag_edit_admin"),
    path('tag/delete/<pk>',views.TagDelete.as_view(),name="tag_delete_admin"),

    path('category',views.CategoryManger.as_view(),name="category_admin"),
    path('category/add',views.CategoryAdd.as_view(),name="category_add_admin"),
    path('category/<int:id>',views.EditCategory.as_view(),name="category_edit_admin"),
    path('category/delete/<pk>',views.CategoryDelete.as_view(),name="category_delete_admin"),
]
