from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView  # Import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('twitter/', include('twitter.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', RedirectView.as_view(url='/twitter/', permanent=True)),  # Redirect / to /twitter/
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
