from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),

    # # CREATE requests
    # path('users/create/', views.create_user),
    # path('items/create/', views.create_item),
    # path('borrows/create/', views.create_borrow),
    # path('reviews/create/', views.create_review),

    # # GET and UPDATE requests
    path('users/<int:data>/', views.user),
    path('items/<int:id>/', views.item),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('login/', views.login, name="login"),
    path('logout/', views.logout),
    path('all_reviews/<int:id>/', views.review),
    path('post_review/<int:id>/', views.post_review),
    path('post_item/', views.post_item, name="create_listing"),
    path('search/', views.search),
    path('all_items/', views.all_items),

    # path('borrows/<int:id>/', views.borrow),
    # path('reviews/<int:id>/', views.review),

    # # DELETE requests
    # path('users/<int:id>/delete/', views.delete_user),
    # path('items/<int:id>/delete/', views.delete_item),
    # path('borrows/<int:id>/delete/', views.delete_borrow),
    # path('reviews/<int:id>/delete/', views.delete_review),
]
