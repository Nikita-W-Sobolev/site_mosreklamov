from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, \
    PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeDoneView
from django.contrib.sitemaps.views import sitemap
from django.urls import path, re_path, register_converter, reverse_lazy
from django.contrib.auth import views as auth_views
from django.views.decorators.cache import cache_page

from . import views
from .sitemaps import ArticleSitemap, CategorySitemap, StaticSitemap
from .views import UserDeleteView


sitemaps = {
    'articles': ArticleSitemap,
    'categories': CategorySitemap,
    'static': StaticSitemap,
}

urlpatterns = [
    path('', views.index, name='home'),
    path('nashi_raboti/', views.nashi_raboti, name='nashi-raboti'),
    path('dobavit_staty/', views.dobavit_staty, name='dobavit_staty'),
    path('article/edit/<int:article_id>/', views.edit_article, name='edit_article'),
    path('article/delete/<int:article_id>/', views.delete_article, name='delete_article'),
    path('contacts/', views.contacts, name='contacts'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
    path('article/<slug:art_slug>/', views.show_article, name='article'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('password-reset/', PasswordResetView.as_view(
        template_name="main_app/password_reset_form.html",
        success_url=reverse_lazy("password_reset_done"),
        html_email_template_name="main_app/password_reset_email.html"),
        name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name="main_app/password_reset_done.html"),
        name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name="main_app/password_reset_confirm.html",
        success_url=reverse_lazy("password_reset_complete")),
        name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(
        template_name="main_app/password_reset_complete.html"),
        name='password_reset_complete'),
    path('password-change/', views.UserPasswordChange.as_view(),
         name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(
        template_name='main_app/password_change_done.html'),
        name='password_change_done'),
    path('account/delete/', UserDeleteView.as_view(), name='account_delete'),
    path('sitemap.xml', cache_page(86400)(sitemap), {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
