from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import datetime, timedelta
from receipets.models import Receipet
from globals.get_month_range import get_month_range

def get_receipts(request):
        today = timezone.now()
        
        # Calculate the current month range
        current_month_start, current_month_end = get_month_range(today.year, today.month)
        
        # Calculate the previous month range
        previous_month_date = current_month_start - timedelta(days=1)
        previous_month_start, previous_month_end = get_month_range(previous_month_date.year, previous_month_date.month)
        
        # Query the database
        current_month_count = Receipet.objects.filter(receiving_date__range=(current_month_start, current_month_end)).count()
        previous_month_count = Receipet.objects.filter(receiving_date__range=(previous_month_start, previous_month_end)).count()
        
        # Calculate the increase percentage
        if previous_month_count == 0:
            if current_month_count == 0:
                increase_percentage = 0
            else:
                increase_percentage = 100  # Considering any count compared to zero is 100% increase
        else:
            increase_percentage = ((current_month_count - previous_month_count) / previous_month_count) * 100
        
        # Create response data
        data = {
            'current_month_count': current_month_count,
            'increase_percentage': increase_percentage
        }
        
        return Response(data)