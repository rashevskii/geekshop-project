from django.urls import path
import ordersapp.views as orders
app_name="ordersapp"

urlpatterns = [
   path('', orders.OrderList.as_view(), name='orders_list'),
   path('forming/complete/<int:pk>/', orders.order_forming_complete, name='order_forming_complete'),
   path('create/', orders.OrderItemsCreate.as_view(), name='order_create'),
   path('read/<int:pk>/', orders.OrderRead.as_view(), name='order_read'),
   path('update/<int:pk>/', orders.OrderItemsUpdate.as_view(), name='order_update'),
   path('delete/<int:pk>/', orders.OrderDelete.as_view(), name='order_delete'),
]