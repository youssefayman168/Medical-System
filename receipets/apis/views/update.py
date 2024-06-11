from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from globals.track_activity import track_activity
from patients.models import Paitent
from receipets.models import Receipet

@api_view(['POST', 'PUT'])
@permission_classes([permissions.IsAdminUser])
def update_receipt(request, receipt_id):
    data = request.data
    user = request.user

    try:
        receipt = Receipet.objects.get(pk=receipt_id)
    except Receipet.DoesNotExist:
        return Response({
            "message": "لم نستطع العثور علي الاستلام"
        }, status=status.HTTP_404_NOT_FOUND)

    if not data:
        return Response({
            "message": "لا توجد بيانات لتحديث الاستلام"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    doc_number = data.get("doc_number")
    receiving_date = data.get("receiving_date")
    notes = data.get("notes")
    is_update = False
    try:
        if doc_number and receipt.patient.document_number != doc_number:
            try:
                patient = Paitent.objects.get(doc_number=doc_number)
            except Paitent.DoesNotExist:
                return Response({
                    "message": "المريض ليس موجود"
                }, status=status.HTTP_404_NOT_FOUND)
            receipt.patient = patient
            is_update = True
        if receiving_date and receipt.receiving_date != receiving_date:
            receipt.receiving_date = receiving_date
            is_update = True
        if notes and receipt.notes != notes:
            receipt.notes = notes
            is_update = True
        
        if is_update:
            receipt.save()
            track_activity.delay(f"تم تحديث استلام بواسطة {user.username}")
            return Response({
                "message": "تم تحديث الاستلام بنجاح"
            }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            "message": "لا يوجد اي بيانات لتحديثها "
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "حدث خطأ انثاء تحديث الاستلام...حاول مرة اخري"
        }, stauts=status.HTTP_400_BAD_REQUEST)