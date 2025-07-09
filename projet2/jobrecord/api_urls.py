from rest_framework.routers import DefaultRouter
from .viewsets import (
    ContractViewSet, SkillViewSet, IndustryViewSet,
    LocationViewSet, JobTitleViewSet,
    CandidateViewSet, JobRecordViewSet
)

router = DefaultRouter()
router.register(r'contracts', ContractViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'industries', IndustryViewSet)
router.register(r'locations', LocationViewSet)
router.register(r'job-titles', JobTitleViewSet)
router.register(r'candidates', CandidateViewSet)
router.register(r'jobs', JobRecordViewSet, basename='jobrecord')

urlpatterns = router.urls
