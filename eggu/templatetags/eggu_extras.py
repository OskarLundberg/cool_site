from django import template

import random

register = template.Library()


@register.simple_tag
def random_quote():
    """Returns a random quote to be displayed on the community sandwich page"""
    quotes = [
        "Growth is never by mere chance; it is the result of forces working together.\n-James Cash Penney",
        "We cannot accomplish all that we need to do without working together\n-Bill Richardson",
        "The power of one, if fearless and focused, is formidable, but the power of many working together is better.\n-Gloria Macapagal Arroyo",
        "The power of one, if fearless and focused, is formidable, but the power of many working together is better.\n-Jacqueline Novogratz",
        "I love a sandwich that you can barely fit in your mouth because there's so much stuff on it. The bread should not be the main thing on a sandwich.\n-Adrianne Palicki",
        "Communism will win.\n-Slavoj Zizek",
    ]
    return random.choice(quotes)

