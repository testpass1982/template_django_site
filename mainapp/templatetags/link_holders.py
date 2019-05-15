from django import template
from ..models import Menu, Post, Document, Chunk
from django.urls import reverse
# from django.shortcuts import get_object_or_404

register = template.Library()

@register.simple_tag
def link_holder(url_code):
    try:
        post = Post.objects.get(url_code=url_code)
        link = reverse('details', kwargs={'pk': post.pk})
    except Post.DoesNotExist:
        link = '#'
    return link

@register.simple_tag
def title_holder(url_code):
    try:
        post = Post.objects.get(url_code=url_code)
        title = post.title
    except Post.DoesNotExist:
        title = 'Страница еще не создана ({})'.format(url_code)
    return title

@register.simple_tag
def doc_holder(url_code):
    try:
        doc = Document.objects.get(url_code=url_code)
        url = doc.document.url
    except Document.DoesNotExist:
        url = '#'
    return url

@register.simple_tag
def chunk(chunk_code):
    try:
        chunk = Chunk.objects.get(code=chunk_code)
        html = chunk.html
    except Chunk.DoesNotExist:
        html = """
            <hr>
            <i>!!! Создайте вставку с кодом <strong>{}</strong> !!!</i>
            <hr>
        """.format(chunk_code)
    return html

