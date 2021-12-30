from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('resume/', include('personal_portfolio.resume.urls')),
    path('projects/', include('personal_portfolio.projects.urls')),
    path('blog/', include('personal_portfolio.blog.urls')),
    path('hire-me/', include('personal_portfolio.hire_me.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
