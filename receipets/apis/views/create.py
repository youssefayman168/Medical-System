from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from globals.track_activity import track_activity
from patients.models import Paitent
from receipets.models import Receipet

@api_view(['POST'])
@permission_classes([permissions.IsAdminUser])
def create_receipt(request):
    data = request.data
    user = request.user
    if not data:
        return Response({
            "message": "لا يوجد بيانات لاضافة استلام"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    doc_number = data.get("doc_number")
    receiving_date = data.get("receiving_date")
    notes = data.get("notes")

    if not doc_number:
        return Response({
            "message": "من فضلك ادخل رقم الملف"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not receiving_date:
        return Response({
            "message": "من فضلك ادخل تاريخ الأستلام"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        patient = Paitent.objects.get(doc_number=doc_number)
    except Paitent.DoesNotExist:
        return Response({
            "message": "المريض ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        receipt = Receipet.objects.create(
            patient=patient,
            receiving_date=receiving_date,
            notes=notes
        )
        patient.date_order_delivered = receipt.receiving_date
        patient.save()
        track_activity.delay(f"تم اضافة استلام جديد بواسطة {user.username}")
        return Response({
            "message": "تم اضافة الاستلام بنجاح"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "حدث خطأ انثاء اضافة الاستلام...حاول مرة اخري"
        }, stauts=status.HTTP_400_BAD_REQUEST)