from django.urls import path

import adminapp.views as adminapp

app_name = 'adminapp'

urlpatterns = [
    path('users/create/', adminapp.users_create, name='user_create'),
    path('users/read/', adminapp.UsersListView.as_view(), name='users'),
    path('users/update/<int:pk>/', adminapp.users_update, name='user_update'),
    path('users/delete/<int:pk>/', adminapp.users_delete, name='user_delete'),

    path('categories/create/', adminapp.ProductCategoryCreateView.as_view(), name='category_create'),
    path('categories/read/', adminapp.categories, name='categories'),
    path('categories/update/<int:pk>/', adminapp.ProductCategoryUpdateView.as_view(), name='category_update'),
    path('categories/delete/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='category_delete'),

    path('products/create/category/<int:pk>/', adminapp.products_create, name='products_create'),
    path('products/read/<int:pk>/', adminapp.ProductCategoryDeleteView.as_view(), name='product_read'),
    path('products/read/category/<int:pk>/', adminapp.products, name='products'),
    path('products/update/<int:pk>/', adminapp.products_update, name='products_update'),
    path('products/delete/<int:pk>/', adminapp.products_delete, name='product_delete'),
]
