from .models import Partner,Contact


def global_data(request):
    
    lang = getattr(
        request,
        "CURRENT_LANG",
        "uz"
    )
    contact = Contact.objects.first()
    return {
        "partners": Partner.objects.all(),
        "footer_contact": {
            "title": getattr(contact, f"title_{lang}", "") if contact else "",
            "address": getattr(contact, f"address_{lang}", "") if contact else "",
            "phone": contact.phone if contact else "",
            "email": contact.email if contact else "",
        }
    }