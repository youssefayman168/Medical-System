from exports.models import Export
from exports.apis.serializer import ExportSerializer
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from datetime import datetime, timedelta

"""
HOW TO BUILD IT:
1. FIRST, GET MONTHS
"""
@permission_classes([permissions.IsAdminUser])
@api_view(['GET'])
def get_exported_items(request, date, sec_date):
    try:
        date_from = datetime.strptime(date, '%Y-%m-%d').date()
        date_to = datetime.strptime(sec_date, '%Y-%m-%d').date()
    except (KeyError, ValueError):
        return Response({'error': 'تاريخ خاطئ'}, status=status.HTTP_400_BAD_REQUEST)

    # Generate a list of months between date_from and date_to
    months = []
    current_date = date_from.replace(day=1)
    while current_date <= date_to:
        months.append(current_date)
        # Move to the first day of the next month
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)
    
    results = []
    for month_start in months:
        month_end = (month_start + timedelta(days=32)).replace(day=1) - timedelta(days=1)
        exists = Export.objects.filter(date__range=(month_start, month_end)).exists()
        results.append({
            "month": month_start.strftime('%Y-%m'),
            "export_created": "YES" if exists else "NO"
        })

    return Response(results, status=status.HTTP_200_OK)

@permission_classes([permissions.IsAdminUser])
@api_view(['GET'])
def get_monthly_exports(request, date):
    try:
        if not date:
            return Response({'error': 'Date is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Parse the date string to extract the month and year
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        year = date_obj.year
        month = date_obj.month
        
        # Define the date range for the specified month
        date_from = datetime(year, month, 1)
        if month == 12:
            date_to = datetime(year + 1, 1, 1)
        else:
            date_to = datetime(year, month + 1, 1)

    # Retrieve all exports for the specified month
        exports = Export.objects.filter(date__range=(date_from, date_to))
        serializer = ExportSerializer(exports, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "حدث خطأ اثناء جلب التقرير الشهري"
        }, status=status.HTTP_400_BAD_REQUEST)