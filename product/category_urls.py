from django.urls import path
from product import views

urlpatterns = [
    # path('', views.view_categories ,name='view-categories'),
    # path('<int:pk>/', views.view_specific_category, name='specific-category'),
    # path('', views.ViewCategories.as_view(), name='category-list'),
    # path('<int:id>/', views.ViewSpecificCategory.as_view(),name='specific-category')
    path('', views.CategoryList.as_view(), name='category-list'),
    path('<int:id>/', views.CategoryDetails.as_view(),name='specific-category')
]
