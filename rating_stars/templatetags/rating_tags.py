# -*- coding: utf-8 -*-
from django import template
from django.contrib.contenttypes.models import ContentType

from rating.forms import UpdateRatingForm
from rating.models import Rating

register = template.Library()


@register.inclusion_tag(
    'rating/rating_wrapper.html',
    takes_context=True
)
def get_rating(context, obj):
    ctx = context
    ctx['form'] = UpdateRatingForm()
    request = ctx['request']
    ctype = ContentType.objects.get_for_model(obj)

    try:
        rating_obj = Rating.objects.get(
            content_type=ctype, object_id=obj.id
        )
    except Rating.DoesNotExist:
        rating_obj = Rating(
            content_type=ctype, object_id=obj.id
        )
    except:
        rating_obj = None

    if rating_obj is not None:
        ctx['vote_average'] = rating_obj.average
        ctx['vote_amount'] = rating_obj.votes
        if request.user.is_authenticated():
            ctx['vote_user_id'] = request.user.id
        else:
            ctx['vote_user_id'] = None
    return ctx


@register.filter
def content_type(obj):
    if not obj:
        return False
    return ContentType.objects.get_for_model(obj).id