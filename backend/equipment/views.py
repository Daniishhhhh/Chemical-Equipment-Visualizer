import pandas as pd

from .models import Dataset

from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.authentication import SessionAuthentication

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas


# -----------------------------------
# CSRF DISABLED SESSION AUTH (REACT)
# -----------------------------------

from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return



# -----------------------------------
# LOGIN
# -----------------------------------

class LoginAPIView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = [CsrfExemptSessionAuthentication]

    def post(self, request):

        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password")
        )

        if user:
            login(request, user)
            return Response({"message": "Login successful"})

        return Response({"error": "Invalid credentials"}, status=401)


# -----------------------------------
# CSV UPLOAD (AUTH REQUIRED)
# -----------------------------------

class UploadCSVView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []


    parser_classes = [MultiPartParser, FormParser]

    def post(self, request):

        file = request.FILES.get("file")

        if not file:
            return Response({"error": "No file received"}, status=400)

        df = pd.read_csv(file)

        summary_stats = {
            "total_equipment": len(df),
            "avg_flowrate": round(float(df["Flowrate"].mean()), 2),
            "avg_pressure": round(float(df["Pressure"].mean()), 2),
            "avg_temperature": round(float(df["Temperature"].mean()), 2),
        }

        equipment_distribution = df["Type"].value_counts().to_dict()

        Dataset.objects.create(
            file_name=file.name,
            raw_data=df.to_dict(),
            summary_stats=summary_stats,
            equipment_distribution=equipment_distribution
        )

        return Response({
            "message": "CSV uploaded successfully",
            "summary": summary_stats,
            "distribution": equipment_distribution
        })


# -----------------------------------
# HISTORY
# -----------------------------------


# ----------------------------------
# Latest Summary API (PUBLIC)
# ----------------------------------

class LatestSummaryView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):

        latest = Dataset.objects.order_by("-upload_time").first()

        if not latest:
            return Response(
                {"message": "No data available"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response({
            "file_name": latest.file_name,
            "upload_time": latest.upload_time,
            "summary": latest.summary_stats,
            "distribution": latest.equipment_distribution
        })

class HistoryView(APIView):

    permission_classes = []
    authentication_classes = []

    def get(self, request):

        datasets = Dataset.objects.order_by("-upload_time")[:5]

        return Response([
            {
                "file_name": d.file_name,
                "upload_time": d.upload_time,
                "summary": d.summary_stats
            }
            for d in datasets
        ])


# -----------------------------------
# PDF
# -----------------------------------
class GeneratePDFView(APIView):

    permission_classes = [AllowAny]
    authentication_classes = []

    def get(self, request):

        latest = Dataset.objects.order_by("-upload_time").first()

        if not latest:
            return Response(
                {"message": "No data available"},
                status=status.HTTP_404_NOT_FOUND,
            )

        response = HttpResponse(content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="equipment_report.pdf"'

        pdf = canvas.Canvas(response, pagesize=A4)
        width, height = A4

        y_position = height - 50

        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(50, y_position, "Chemical Equipment Analysis Report")

        y_position -= 40

        pdf.setFont("Helvetica", 11)
        pdf.drawString(50, y_position, f"File Name: {latest.file_name}")
        y_position -= 20
        pdf.drawString(50, y_position, f"Upload Time: {latest.upload_time}")

        y_position -= 40

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y_position, "Summary Statistics:")

        y_position -= 25
        pdf.setFont("Helvetica", 11)

        for key, value in latest.summary_stats.items():
            pdf.drawString(
                70,
                y_position,
                f"{key.replace('_', ' ').title()} : {value}",
            )
            y_position -= 20

        y_position -= 20

        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y_position, "Equipment Distribution:")

        y_position -= 25
        pdf.setFont("Helvetica", 11)

        for key, value in latest.equipment_distribution.items():
            pdf.drawString(70, y_position, f"{key} : {value}")
            y_position -= 20

        pdf.showPage()
        pdf.save()

        return response
