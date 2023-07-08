from django.urls import path

from category_of_tech.views import ListOfCategoryView, CategoryDetailView, DeleteCategory, CategoryUpdateView

urlpatterns = [
    path('', ListOfCategoryView.as_view()),
    path('<int:pk>/', CategoryDetailView.as_view()),
    path('<int:pk>/update/', CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', DeleteCategory.as_view()),
]