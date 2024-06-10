from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from exports.models import Export, Order
from activity.models import Activity

@api_view(["POST"])
@permission_classes([permissions.IsAdminUser])
def create_export(request):
    data = request.data
    user = request.user 
    
    if not data:
        return Response({
            "message": "من فضلك ادخل بيانات التوريد لاضافته"
        }, status=status.HTTP_100_CONTINUE)
    
    orders = data.get("orders")
    date = data.get("date")
    invoice_date = data.get("invoice_date")
    receiver_name = data.get("receiver_name")
    attachment = data.get("attachment")

    if not orders or len(orders) == 0:
        return Response({
            "message": "من فضلك ادخل علي الأقل منتج واحد"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not date:
        return Response({
            "message": "من فضلك ادخل تاريخ التوريد"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not invoice_date:
        return Response({
            "message": "من فضلك ادخل تاريخ الفاتورة"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not receiver_name:
        return Response({
            "message": "من فضلك ادخل اسم المستلم"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    if not attachment:
        return Response({
            "message": "من فضلك ادخل مستند التوريد"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        export = Export.objects.create(
            date=date,
            invoice_date=invoice_date,
            receiver_name=receiver_name,
            attachment=attachment
        )
        for order in orders:
            try:
                Order.objects.create(
                    quantity=order.get("quantity"),
                    prod_name=order.get("prod_name"),
                    export=export
                )
            except Exception as e:
                print(e)
                return Response({
                    "message": "حدث خطأ اثناء ادخال المنتجات الخاصة بالتوريد...حاول مرة اخري"
                }, status=status.HTTP_400_BAD_REQUEST)
            
        try:
                Activity.objects.create(
                        content="تم انشاء توريد جديد حديثاً",
                        made_by=user
                    )
        except Exception as e:
                return Response({
                    "message": "حدث خطأ اثناء انشاء التوريد"
                })       
        return Response({
            "message": "تم اضافة التوريد بنجاح !"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"حدث خطأ اثناء انشاء التوريد...الرجاء المحاولة مرة اخري {e}"
        }, status=status.HTTP_400_BAD_REQUEST)
