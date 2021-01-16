from django.views.generic import View
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import redirect
from django.views import generic
from django.http import Http404, HttpResponseRedirect

from .models import Book
from .forms import BookEditForm


class IndexView(View):
    def get(self, request, *args, **kwargs):
        books = Book.objects.all()
        # いいねや編集後に順番が変わらないように本を登録した順(id順)に並び替える
        books = Book.objects.order_by('id')

        # 10冊を超えたら次のページを作る
        paginator = Paginator(books, 10)

        page = request.GET.get('page', 1)
        books = paginator.page(page)

        return TemplateResponse(request, 'bookshelf/index.html', {'books': books})


index = IndexView.as_view()


class BookDetail(View):
    def get(self, request, book_id, *args, **kwargs):
        try:
            book = Book.objects.get(id=book_id)
        # 本が存在しない時はエラーメッセージを表示する
        except Book.DoesNotExist:
            raise Http404
        return TemplateResponse(request, 'bookshelf/book_detail.html', {'book': book})


book_detail = BookDetail.as_view()


class BookDelete(View):
    def get(self, request, book_id, *args, **kwargs):
        try:
            book = Book.objects.get(id=book_id)

        # 本が存在しない時はエラーメッセージを表示する
        except Book.DoesNotExist:
            raise Http404

        # book_delete.htmlのformからデータが送られてきた時にそのデータを消す
        if request.method == 'POST':
            book.delete()
            return HttpResponseRedirect(reverse('bookshelf:index'))
        else:
            return TemplateResponse(request, 'bookshelf/book_delete.html', {'book': book})


book_delete = BookDelete.as_view()


class Like(View):
    def get(self, request, book_id, *args, **kwargs):
        try:
            book = Book.objects.get(id=book_id)

        # 本が存在しない時はエラーメッセージを表示する
        except Book.DoesNotExist:
            raise Http404

        # この関数が呼び出された時にlikeに１を足して保存する
        book.like += 1

        book.save()
        return redirect('/bookshelf/')


like = Like.as_view()


class Book_Add(generic.edit.CreateView):
    model = Book
    fields = '__all__'


class BookEdit(View):
    def get(self, request, book_id, *args, **kwargs):
        try:
            book = Book.objects.get(id=book_id)
        # 本が存在しない時はエラーメッセージを表示する
        except Book.DoesNotExist:
            raise Http404

        # book_edit.htmlのformからデータが送られてきた時にそのデータを保存する
        if request.method == 'POST':
            form = BookEditForm(request.POST, instance=book)
            if form.is_valid():
                form.save()
                # 編集後はHome画面に戻る
                return HttpResponseRedirect(reverse('book:book_list'))

        else:
            form = BookEditForm(instance=book)
        # book_edit.htmlを呼び出す
        return TemplateResponse(request, 'bookshelf/book_edit.html', {'form': form, 'book': book})


book_edit = BookEdit.as_view()
