from rest_framework import permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework import status
from exports.models import Export, Order
from activity.models import Activity

@api_view(['PUT',])
@permission_classes([permissions.IsAdminUser])
def update_export(request, export_id):
    user = request.data
    data = request.data

    try:
        export = Export.objects.get(pk=export_id)
    except Export.DoesNotExist:
        return Response({
            "message": "التوريد ليس موجود"
        }, status=status.HTTP_404_NOT_FOUND)
    
    if not data:
        return Response({
            "message": "من فضلك ادخل بيانات التوريد لتحديثه"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    orders = data.get("orders")
    date = data.get("date")
    invoice_date = data.get("invoice_date")
    receiver_name = data.get("receiver_name")
    attachment = data.get("attachment")
    is_updated = False
    if orders:
        if len(orders) == 0:
            return Response({
                "message": "من فضلك ادخل منتجات لتحديثها"
            }, status=status.HTTP_400_BAD_REQUEST)
        orders_list = []
        for order in orders:
            try:
                order_item = Order.objects.create(
                    quantity=order["quantity"],
                    prod_name=order["prod_name"],
                    export=export
                )
                orders_list.append(order_item)
                is_updated = True
            except Exception as e:
                print(e)
                return Response({
                    "message": "حدث خطأ اثناء ادخال المنتجات الخاصة بالتوريد...حاول مرة اخري"
                }, status=status.HTTP_400_BAD_REQUEST)
        export.order_set.set(orders_list)

    if date and export.date != date:
        export.date = date
        is_updated = True
    

    if invoice_date and export.invoice_date != invoice_date:
        export.invoice_date = invoice_date
        is_updated = True

    if receiver_name and export.receiver_name != receiver_name:
        export.receiver_name = receiver_name
        is_updated = True

    if attachment and export.attachment != attachment:
        export.attachment = attachment
        is_updated = True

    try:
        if is_updated:
            export.save()
            try:
                Activity.objects.create(
                    content=f"تم تحديث توريد بواسطة {user.username}",
                    made_by=user
                )
            except Exception as e:
                return Response({
                    "message": "حدث خطأ اثناء التجديث...رجاء حاول مرة اخري"
                })
            return Response({
                "message": "تم تحديث التوريد بنجاح !"
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "لا يوجد شئ لتحديثه!"
        }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": f"حدث خطأ اثناء التحديث...حاول مرة اخري {e}"
        }, status=status.HTTP_400_BAD_REQUEST)
    