from django.urls import path, include
from med import views

app_name="med"

urlpatterns = [
 path('home/', views.homeview.as_view()),
 path('about/', views.aboutview.as_view()),
 path('medicine/', views.product_list),
 path('contact/', views.contactusview.as_view()),
 path('blog/', views.blogview.as_view()),
 path('signin/', views.signinview.as_view()),
 path('suscribe/', views.suscribeview.as_view()),
 path('upload/', views.uploadview.as_view()),
 path('blogdetail/<int:id>', views.showblog),
 path('cartdetail/', views.cartdetailview.as_view()),
 path('detail/', views.cartdetailview.as_view()),
path('blog1/', views.blog1view.as_view()),
path('blog2/', views.blog2view.as_view()),
 
path('insert',views.insert),
path('insertsubscribe',views.insertsubscribe),
path('insertcontactus',views.insertcontactus),
path('insertupload',views.insertupload),




]