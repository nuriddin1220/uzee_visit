import os
import random
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE","config.settings")

django.setup()
from main.models import Vacancy

vacancies = [
    {
        "title_uz": "Loyiha boshqaruvi bo‘yicha mutaxassis",
        "title_ru": "Специалист по управлению проектами",
        "title_en": "Project Management Specialist",
        "description_uz": """
Lavozim tavsifi:
Energetika va infratuzilma loyihalarini rejalashtirish, muddatlar va resurslarni nazorat qilish, loyiha ishtirokchilari faoliyatini muvofiqlashtirish hamda loyiha hisobotlarini tayyorlash.

Talablar:
- Oliy ma'lumot.
- Kamida 3 yil ish tajribasi.
- MS Project va Excel dasturlarini bilish.
- Analitik fikrlash qobiliyati.
- Ingliz tilini bilish afzallik beradi.
""",
        "description_ru": """
Описание вакансии:
Планирование энергетических и инфраструктурных проектов, контроль сроков и ресурсов, координация участников проекта и подготовка отчетности.

Требования:
- Высшее образование.
- Опыт работы не менее 3 лет.
- Знание MS Project и Excel.
- Аналитическое мышление.
- Знание английского языка будет преимуществом.
""",
        "description_en": """
Job Description:
Planning energy and infrastructure projects, monitoring schedules and resources, coordinating project participants, and preparing project reports.

Requirements:
- Higher education.
- At least 3 years of experience.
- Knowledge of MS Project and Excel.
- Strong analytical skills.
- English proficiency is an advantage.
"""
    },
    {
        "title_uz": "Xaridlar bo‘yicha mutaxassis",
        "title_ru": "Специалист по закупкам",
        "title_en": "Procurement Specialist",
        "description_uz": """
Lavozim tavsifi:
Loyihalar uchun uskunalar va materiallarni xarid qilish, tender hujjatlarini tayyorlash va yetkazib beruvchilar bilan ishlash.

Talablar:
- Oliy ma'lumot.
- Xaridlar bo‘yicha kamida 2 yil tajriba.
- Muzokara olib borish ko‘nikmasi.
- MS Office dasturlarini yaxshi bilish.
""",
        "description_ru": """
Описание вакансии:
Закупка оборудования и материалов для проектов, подготовка тендерной документации и взаимодействие с поставщиками.

Требования:
- Высшее образование.
- Опыт работы в закупках не менее 2 лет.
- Навыки ведения переговоров.
- Уверенное владение MS Office.
""",
        "description_en": """
Job Description:
Procurement of equipment and materials for projects, preparation of tender documents, and supplier relations.

Requirements:
- Higher education.
- At least 2 years of procurement experience.
- Negotiation skills.
- Proficiency in MS Office.
"""
    },
    {
        "title_uz": "Rele himoyasi va avtomatika muhandisi",
        "title_ru": "Инженер РЗА",
        "title_en": "Relay Protection and Automation Engineer",
        "description_uz": """
Lavozim tavsifi:
Rele himoyasi va avtomatika tizimlarini loyihalash, sozlash va texnik ekspertiza o'tkazish.

Talablar:
- Oliy texnik ma'lumot.
- Kamida 3 yil tajriba.
- Mikroprotsessorli himoya qurilmalarini bilish.
- Xizmat safarlariga tayyorlik.
""",
        "description_ru": """
Описание вакансии:
Проектирование, настройка и экспертиза систем релейной защиты и автоматики.

Требования:
- Высшее техническое образование.
- Опыт работы не менее 3 лет.
- Знание микропроцессорных устройств защиты.
- Готовность к командировкам.
""",
        "description_en": """
Job Description:
Design, commissioning, and assessment of relay protection and automation systems.

Requirements:
- Higher technical education.
- At least 3 years of experience.
- Knowledge of microprocessor-based protection devices.
- Willingness to travel.
"""
    }
]

for item in vacancies:
    Vacancy.objects.create(**item)

print("Vacancies created successfully.")