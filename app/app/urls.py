"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from account.urls import urlpatterns as account_urls
from category.urls import urlpatterns as category_urls
from subcategory.urls import urlpatterns as subcategory_urls
from product.urls import urlpatterns as product_urls
from settings.urls import urlpatterns as settings_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(account_urls)),
    path('', include(category_urls)),
    path('', include(subcategory_urls)),
    path('', include(product_urls)),
    path('', include(settings_urls)),
]
