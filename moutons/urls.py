from django.conf.urls import url, include
from rest_framework import routers
from . import api, views


router = routers.DefaultRouter()
router.register(r'mouton', api.MoutonViewSet)
router.register(r'lot', api.LotViewSet)
router.register(r'lutte', api.LutteViewSet)
router.register(r'treatment', api.TreatmentViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for Mouton
    url(r'^mouton/$', views.MoutonListView.as_view(), name='moutons_mouton_list'),
    url(r'^mouton/create/$', views.MoutonCreateView.as_view(), name='moutons_mouton_create'),
    url(r'^mouton/detail/(?P<pk>\S+)/$', views.MoutonDetailView.as_view(), name='moutons_mouton_detail'),
    url(r'^mouton/update/(?P<pk>\S+)/$', views.MoutonUpdateView.as_view(), name='moutons_mouton_update'),
    url(r'^mouton/sortie/(?P<pk>\S+)/$', views.MoutonSortieView.as_view(), name='moutons_mouton_sortie'),
    url(r'^mouton_inventaire/$', views.MoutonInventaireListView.as_view(), name='moutons_mouton_inventaire_list'),
)

urlpatterns += (
    # url for Treatment
    url(r'^mouton/(?P<mouton_number>\S+)/treatement/create/$', views.TreatmentCreateView.as_view(), name='moutons_treatment_create'),
    url(r'^treatment/update/(?P<pk>\S+)/$', views.TreatmentUpdateView.as_view(), name='moutons_treatment_update'),
)
urlpatterns += (
    # urls for Lutte
    url(r'^lutte/$', views.LutteListView.as_view(), name='moutons_lutte_list'),
    url(r'^lutte/create/$', views.LutteCreateView.as_view(), name='moutons_lutte_create'),
    url(r'^lutte/detail/(?P<pk>\S+)/$', views.LutteDetailView.as_view(), name='moutons_lutte_detail'),
    url(r'^lutte/update/(?P<pk>\S+)/$', views.LutteUpdateView.as_view(), name='moutons_lutte_update'),
)

