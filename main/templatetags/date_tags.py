from django import template

register=template.Library()


MONTHS={
    "uz":[
        "Yan","Fev","Mar","Apr","May","Iyn",
        "Iyl","Avg","Sen","Okt","Noy","Dek"
    ],

    "ru":[
        "Янв","Фев","Мар","Апр","Май","Июн",
        "Июл","Авг","Сен","Окт","Ноя","Дек"
    ],

    "en":[
        "Jan","Feb","Mar","Apr","May","Jun",
        "Jul","Aug","Sep","Oct","Nov","Dec"
    ]
}


@register.filter
def custom_date(value,lang):

    if not value:
        return ""

    month=MONTHS.get(
        lang,
        MONTHS["uz"]
    )[value.month-1]

    return f"{month} {value.day}, {value.year}"