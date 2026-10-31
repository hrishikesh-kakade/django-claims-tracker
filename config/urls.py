"""
URL configuration for config project.

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
from claims.views import home, claim_list, claim_detail, update_decision, claim_create, delete_claim

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('claims/', claim_list, name='claim_list'),
    path('claims/<int:claim_id>/', claim_detail, name='claim_details'),
    path('claims/<int:claim_id>/update/', update_decision, name='claim_update'),
    path('claims/create/', claim_create, name='claim_create'),
    path(    'claims/<int:claim_id>/delete/',delete_claim,name='claim_delete'),  
]
