from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from apps.user_profile.views import dashboard
from apps.core.views import frontpage
from apps.template.views import display_profile_card_id, display_profile_card_profile_name
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('card-profile/', include('apps.card_profile.urls')),
    path('userprofile/', include('apps.user_profile.urls')),
    path('card/', include('apps.card.urls')),
    path('<int:card_id>/', display_profile_card_id, name='display_profile_card_id'),
    path('<str:card_profile_name>/', display_profile_card_profile_name, name='display_profile_card_profile_name'),
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
