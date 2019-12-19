from django.urls import path

from . import views

urlpatterns = [
    # Homepage
    path('', views.index_page, name='index_page'),

    # Gateway
    path('register', views.register_page, name='register_page'),
    path('register/success', views.register_success_page, name='register_success_page'),
    path('login', views.login_page, name='login_page'),
    path('logout', views.logout_page, name='logout_page'),
    path('api/logout', views.post_logout_api, name='logout_api'),

    # Dashboard
    path('dashboard', views.dashboard_page, name='dashboard_page'),

    # # User Profile
    # path('profile', views.profile_retrieve_page, name='profile_retrieve_page'),
    # path('profile/update', views.profile_update_page, name='profile_update_page'),
]
