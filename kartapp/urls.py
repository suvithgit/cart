from django.urls import path
from .import views
app_name='kartapp'

urlpatterns = [
    path('',views.allprodtCate,name='allprodtCate'),
    path('<slug:c_slug>/',views.allprodtCate,name='product_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/',views.productDetail,name='product_detail'),

]