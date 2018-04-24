
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import mypage.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mypage.views.home, name = 'home'),
    path('aboutme/', mypage.views.aboutme, name = 'aboutme'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
