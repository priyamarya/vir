"""Filter."""
from django import template
register = template.Library()


@register.filter
def filter_private_cards(values):
    # import ipdb; ipdb.set_trace()
    all_list = []
    for value in values:
        if (value.v_type == 'private'):
            all_list.append(value)

    return all_list
