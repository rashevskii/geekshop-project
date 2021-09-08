from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminEditForm, ProductCategoryEditForm, ProductEditForm
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def users_create(request):
    title = "пользователи / создание"
    if request.method == 'POST':
        update_form = ShopUserRegisterForm(request.POST, request.FILES)

        if update_form.is_valid():
            update_form.save()
            return HttpResponseRedirect(reverse('admin:users'))
    else:
        update_form = ShopUserRegisterForm()

    context = {
        'title': title,
        'update_form': update_form
    }
    return render(request, "adminapp/user_update.html", context)


# @user_passes_test(lambda u: u.is_superuser)
# def users(request):
#     title = 'админка / пользователи'
#     users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser', '-is_staff', 'username')
#     context = {
#         'title': title,
#         'objects': users_list
#     }
#     return render(request, 'adminapp/users.html', context)

class UsersListView(ListView):
    model = ShopUser
    template_name = "adminapp/users.html"

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(is_active=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'пользователи / список'
        return context


@user_passes_test(lambda u: u.is_superuser)
def users_update(request, pk):
    title = "пользователи / редактирование"

    edit_user = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        edit_form = ShopUserAdminEditForm(request.POST, request.FILES, instance=edit_user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("admin:users"))
    else:
        edit_form = ShopUserAdminEditForm(instance=edit_user)

    context = {
        "title": title,
        "update_form": edit_form
    }
    return render(request, "adminapp/user_update.html", context)


@user_passes_test(lambda u: u.is_superuser)
def users_delete(request, pk):
    title = "пользователи / удаление"
    user_item = get_object_or_404(ShopUser, pk=pk)
    if request.method == "POST":
        if user_item.is_active:
            user_item.is_active = False
        else:
            user_item.is_active = True
        user_item.save()
        return HttpResponseRedirect(reverse("admin:users"))

    context = {
        "title": title,
        "user_to_delete": user_item
    }
    return render(request, "adminapp/user_delete.html", context)


@user_passes_test(lambda u: u.is_superuser)
def categories(request):
    title = 'админка / категории'
    categories_list = ProductCategory.objects.all().order_by('-is_active', '-id')
    context = {
        'title': title,
        'objects': categories_list
    }
    return render(request, 'adminapp/categories.html', context)


# @user_passes_test(lambda u: u.is_superuser)
# def category_create(request):
#     title = "категории / создание"
#     if request.method == 'POST':
#         update_form = ProductCategoryEditForm(request.POST, request.FILES)
#
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         update_form = ProductCategoryEditForm()
#
#     context = {
#         'title': title,
#         'update_form': update_form
#     }
#     return render(request, "adminapp/category_update.html", context)


class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")

    # fields = "__all__"

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории / создание'
        return context


class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    form_class = ProductCategoryEditForm
    template_name = "adminapp/category_update.html"
    success_url = reverse_lazy("admin:categories")

    # fields = "__all__"

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории / редактирование'
        return context


class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    template_name = "adminapp/category_delete.html"

    @method_decorator(user_passes_test(lambda user: user.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории / удаление'
        return context

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.is_active:
            obj.is_active = False
        else:
            obj.is_active = True
        obj.save()

        return HttpResponseRedirect(reverse("admin:categories"))


# @user_passes_test(lambda u: u.is_superuser)
# def category_update(request, pk):
#     title = "категории / редактирование"
#
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#
#     if request.method == 'POST':
#         update_form = ProductCategoryEditForm(request.POST, request.FILES, instance=category_item)
#
#         if update_form.is_valid():
#             update_form.save()
#             return HttpResponseRedirect(reverse('admin:categories'))
#     else:
#         update_form = ProductCategoryEditForm(instance=category_item)
#
#     context = {
#         'title': title,
#         'update_form': update_form
#     }
#     return render(request, "adminapp/category_update.html", context)


# @user_passes_test(lambda u: u.is_superuser)
# def category_delete(request, pk):
#     title = "категории / удаление"
#     category_item = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == "POST":
#         if category_item.is_active:
#             category_item.is_active = False
#         else:
#             category_item.is_active = True
#         category_item.save()
#         return HttpResponseRedirect(reverse("admin:categories"))
#
#     context = {
#         "title": title,
#         "category_to_delete": category_item
#     }
#     return render(request, "adminapp/category_delete.html", context)


@user_passes_test(lambda u: u.is_superuser)
def products_create(request, pk):
    title = "категории / удаление"
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == "POST":
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse("adminapp:products", args=[pk]))
    else:
        product_form = ProductEditForm()

    context = {
        "title": title,
        "update_form": product_form,
        "category": category
    }
    return render(request, "adminapp/product_update.html", context)


class ProductDetailView(DetailView):
    model = Product
    template_name = "adminapp/product_read.html"

    method_decorator(user_passes_test(lambda user: user.is_superuser))

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# @user_passes_test(lambda u: u.is_superuser)
# def product_read(request, pk):
#     title = "продукт / подробнее"
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         "title": title,
#         "object": product
#     }
#     return render(request, "adminapp/product_read.html", context)


@user_passes_test(lambda u: u.is_superuser)
def products(request, pk, page=1):
    title = 'админка / товары'
    category_item = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category=category_item).order_by('-id')

    # paginator = Paginator(products_list, 5)
    # try:
    #     products_paginator = paginator.page(page)
    # except PageNotAnInteger:
    #     products_paginator = paginator.page(1)
    # except EmptyPage:
    #     products_paginator = paginator.page(paginator.num_pages)


    context = {
        'title': title,
        'objects': products_list,
        'category': category_item
    }
    return render(request, 'adminapp/products.html', context)


@user_passes_test(lambda u: u.is_superuser)
def products_update(request, pk):
    title = "продукт / редактирование"
    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("adminapp:products_update", args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)
    context = {
        "title": title,
        "update_form": edit_form,
        "category": edit_product.category
    }
    return render(request, "adminapp/product_update.html", context)


@user_passes_test(lambda u: u.is_superuser)
def products_delete(request, pk):
    title = "продукт / удаление"
    product = get_object_or_404(Product, pk=pk)
    if request.method == "POST":
        if product.is_active:
            product.is_active = False
        else:
            product.is_active = True
        product.save()
        return HttpResponseRedirect(reverse("adminapp:products", args=[product.category.pk]))

    context = {
        "title": title,
        "product_to_delete": product
    }
    return render(request, "adminapp/product_delete.html", context)
