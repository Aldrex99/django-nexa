# jobs/api_views.py
from rest_framework.views        import APIView
from rest_framework.response     import Response
from rest_framework.permissions  import IsAuthenticated
from rest_framework.pagination   import PageNumberPagination
from django.db.models            import Avg, Count, F
from .models                     import JobRecord
from .serializers                import DashboardSerializer

class DashboardAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        qs = (
            JobRecord.objects
                .values(job_title_name=F('job_title__title'))
                .annotate(
                    avg_rating=Avg('feedbacks__rating'),
                    feedback_count=Count('feedbacks')
                )
                .order_by('job_title_name')
        )

        paginator = PageNumberPagination()
        paginator.page_size = 10

        page = paginator.paginate_queryset(qs, request, view=self)

        serializer = DashboardSerializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
