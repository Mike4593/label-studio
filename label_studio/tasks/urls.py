"""This file and its contents are licensed under the Apache License 2.0. Please see the included NOTICE for copyright information and LICENSE for a copy of the license.
"""
from django.urls import include, path
from rest_framework import routers

from . import api

app_name = 'tasks'

router = routers.DefaultRouter()
router.register(r'predictions', api.PredictionAPI, basename='prediction')

_api_urlpatterns = [
    # CRUD
    path('', api.TaskListAPI.as_view(), name='task-list'),
    path('<int:pk>/', api.TaskAPI.as_view(), name='task-detail'),
    path('<int:pk>/annotations/', api.AnnotationsListAPI.as_view(), name='task-annotations'),
    path('<int:pk>/drafts', api.AnnotationDraftListAPI.as_view(), name='task-drafts'),
    path(
        '<int:pk>/annotations/<int:annotation_id>/drafts',
        api.AnnotationDraftListAPI.as_view(),
        name='task-annotations-drafts',
    ),
]

_api_annotations_urlpatterns = [
    path('<int:pk>/', api.AnnotationAPI.as_view(), name='annotation-detail'),
    path('<int:pk>/convert-to-draft', api.AnnotationConvertAPI.as_view(), name='annotation-convert-to-draft'),
]

_api_drafts_urlpatterns = [
    path('<int:pk>/', api.AnnotationDraftAPI.as_view(), name='draft-detail'),
]

_api_predictions_urlpatterns = router.urls

# TODO : new
# Add to task API urlpatterns

_api_review_urlpatterns = [
    path('', api.TaskReviewListAPI.as_view(), name='review-list'),
    path('<int:task_id>/', api.TaskReviewDetailAPI.as_view(), name='review-detail'),
    path('<int:task_id>/accept/', api.TaskReviewAcceptAPI.as_view(), name='review-accept'),
    path('<int:task_id>/modify/', api.TaskReviewModifyAPI.as_view(), name='review-modify'),
    path('<int:task_id>/reject/', api.TaskReviewRejectAPI.as_view(), name='review-reject'),
]

urlpatterns = [
    path('api/tasks/', include((_api_urlpatterns, app_name), namespace='api')),
    # TODO: these should be moved to the separate apps
    path('api/annotations/', include((_api_annotations_urlpatterns, app_name), namespace='api-annotations')),
    path('api/drafts/', include((_api_drafts_urlpatterns, app_name), namespace='api-drafts')),
    path('api/', include((_api_predictions_urlpatterns, app_name), namespace='api-predictions')),
    # new
    path('api/reviews/', include((_api_review_urlpatterns, app_name), namespace='api-reviews')),
]

