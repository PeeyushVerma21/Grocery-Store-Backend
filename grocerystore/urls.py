"""
URL configuration for grocerystore project.

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
from django.http import HttpResponse
from django.urls import path, include

def landing_page(request):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Grocery Store Backend API</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; background-color: #f4f4f4; }
            .container { background: white; padding: 30px; border-radius: 8px; max-width: 600px; margin: auto; }
            a { color: #007acc; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Grocery Store Backend API</h1>
            <p>This is a Django REST API project.</p>
            <p><strong>Available Endpoints:</strong></p>
            <ul>
                <li>/api/accounts/</li>
                <li>/api/products/</li>
                <li>/api/orders/</li>
            </ul>
            <p>View the code on GitHub:</p>
            <p><a href="https://github.com/PeeyushVerma21/Grocery-Store-Backend" target="_blank">GitHub Repository</a></p>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html_content)

urlpatterns = [
    path('', landing_page),
    path("admin/", admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/products/', include('products.urls')),
    path('api/orders/', include('orders.urls')),
]
