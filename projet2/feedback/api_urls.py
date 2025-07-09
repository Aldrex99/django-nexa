from rest_framework.routers import DefaultRouter
from .viewsets import FeedbackViewSet

router = DefaultRouter()
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = router.urls
