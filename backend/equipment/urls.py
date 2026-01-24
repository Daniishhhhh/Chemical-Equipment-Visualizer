from django.urls import path
from .views import UploadCSVView, LatestSummaryView, HistoryView, GeneratePDFView
from .views import LoginAPIView


urlpatterns = [
    path("upload-csv/", UploadCSVView.as_view(), name="upload_csv"),
    path("latest-summary/", LatestSummaryView.as_view(), name="latest_summary"),
    path("history/", HistoryView.as_view(), name="history"),
    path("generate-pdf/", GeneratePDFView.as_view(), name="generate_pdf"),
    path("auth/login/", LoginAPIView.as_view()),

]
