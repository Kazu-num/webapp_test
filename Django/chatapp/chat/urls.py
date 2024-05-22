from django.contrib import admin
from django.urls import include, path
from chat.views import root_redirect  # 追加

urlpatterns = [
    path('admin/', admin.site.urls),
    path('chat/', include('chat.urls')),
    path('', root_redirect),  # ルートURLをチャットアプリにリダイレクト
]
