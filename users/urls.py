from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

import users

app_name = 'usersConfig.name'


urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#{
#    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5OTUzNDYzNCwiaWF0IjoxNjk5NDQ4MjM0LCJqdGkiOiJiZWIyYmE5MjBlMGU0ZGY1ODFhZWM3YjM5ODYwOThlOCIsInVzZXJfaWQiOjh9.trbjNWM432d5Xw-T8oV5eJMKzP_Ac2ImRvO83RZmDkw",
#    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk5NDQ4NTM0LCJpYXQiOjE2OTk0NDgyMzQsImp0aSI6IjE1ZmVhMmMwYWU1YTQ2Njg4OGI4YTNhOGY3MTkwNjhlIiwidXNlcl9pZCI6OH0.78RTU-B2IOsYfjUW-HIc-ZpLNf1VmO6ZSiXZKrv0k0I"
#}
