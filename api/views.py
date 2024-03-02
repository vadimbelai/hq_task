from rest_framework import generics, permissions
from django.db.models import Count, Sum, Q
from django.contrib.auth.models import User

import datetime

from products.models import Product, Group, ProductAccess
from .serializers import ProductSerializer


def student_to_group(Group, Product, ProductAccess):
    for product in Product.objects.all():
        #считаем количество групп
        students = ProductAccess.objects.filter(product=product)
        students_amount = students.count()
        max_amount = product.max_amount
        count_1 = students_amount / max_amount
        groups_amount = int(count_1) + bool(count_1 % 1)

        #создаем список списков для записи студентов в группы
        groups_list = [] * groups_amount
        tab_str = 0
        for student in students:
            if len(groups_list[tab_str]) < max_amount:
                groups_list[tab_str].append(student.pk)
            else:
                tab_str += 1
                groups_list[tab_str].append(student.pk)
        for group in groups_list:
            for student_pk in group:
                User.objects.get(pk=student_pk)
                Group.objects.create(students=User)


class ProductListView(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(start_datetime__lte=datetime.datetime.now())