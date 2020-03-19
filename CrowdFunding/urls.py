from django.contrib import admin
from django.urls import path, include
from projects import urls as ProjectUrls
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("HomePage.urls", namespace="crowdFund")),
    path('projects/', include(ProjectUrls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


