from django.urls import path, include
from . import views


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('dreams/', views.dream_list, name='dream-list'),
    path('sleeps/', views.sleep_list, name='sleep-list'),
    path('dreams/<post>', views.dream_by_post_id, name='single-dream'),
    path('sleeps/<post>', views.sleep_by_post_id, name='single-sleep'),
    path('q-entries/<post>', views.q_result_by_post_id, name='q-result'),
    path('people/<post>', views.people_by_post_id, name='dream-people'),
    path('dreams/update/<post>', views.update_dream, name='update-dream'),
    path('sleeps/update/<post>', views.update_sleep, name='update-sleep'),
    path('people/update/<post>', views.update_people, name='update-people'),
    path('add-lucidity-to-dream/<post>/<q_result>', views.update_add_lucidity_to_dream, name='add-lucidity-to-dream'),
]
