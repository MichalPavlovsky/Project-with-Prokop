from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register('employees', views.EmployeeViewset)
router.register('patients', views.PatientViewset)
router.register('workingtimes', views.WorkingTimeViewset)
router.register('actions', views.ActionsViewset)
router.register('visits', views.VisitsViewset)
router.register('typeworkings', views.TypeWorkingViewset)
router.register('realworkingtime', views.RealWorkingTimeViewset)
router.register('config', views.ConfigViewset)
router.register('typeemployees', views.TypeEmployeeViewset)
router.register('typeworking', views.TypeWorkingViewset)





urlpatterns = [
    path('', include(router.urls)),
    path('suma/<int:pk>', views.suma),
    path('sumar', views.sumal)
]