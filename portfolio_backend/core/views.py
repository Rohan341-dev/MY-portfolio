import logging

from django.conf import settings
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .models import (
    Profile, Project, Company, Achievement, Certificate,
    TechStackCategory, TimelineEvent, ExploringItem,
    AILabCard, LeadershipPrinciple, BuildingUpdate
)

logger = logging.getLogger(__name__)

MAX_MESSAGE_LENGTH = 5000


def portfolio_home(request):
    profile = Profile.objects.first()
    if not profile:
        return render(request, 'portfolio.html', {'empty': True})

    context = {
        'profile': profile,
        'identity_tags': profile.identity_tags.all(),
        'about_paragraphs': profile.about_paragraphs.all(),
        'projects': profile.projects.all(),
        'companies': profile.companies.all(),
        'achievements': profile.achievements.all(),
        'certificates': profile.certificates.all(),
        'stack_categories': TechStackCategory.objects.all(),
        'journey_events': profile.timeline_events.filter(event_type='journey'),
        'founder_events': profile.timeline_events.filter(event_type='founder'),
        'exploring_items': profile.exploring_items.all(),
        'ailab_cards': profile.ailab_cards.all(),
        'leadership_principles': profile.leadership_principles.all(),
        'building_updates': profile.building_updates.all(),
    }
    return render(request, 'portfolio.html', context)


@require_POST
def contact_send(request):
    """Send the contact form to the owner's inbox over SMTP."""
    name = (request.POST.get('name') or '').strip()
    email = (request.POST.get('email') or '').strip()
    message = (request.POST.get('message') or '').strip()

    errors = {}
    if not name:
        errors['name'] = 'Please tell me your name.'
    elif len(name) > 200:
        errors['name'] = 'Name is too long.'
    if not email:
        errors['email'] = 'Please add your email so I can reply.'
    elif '@' not in email or email.startswith('@') or email.endswith('@'):
        errors['email'] = 'That email address does not look valid.'
    if not message:
        errors['message'] = 'Please write a message.'
    elif len(message) > MAX_MESSAGE_LENGTH:
        errors['message'] = f'Message is too long (max {MAX_MESSAGE_LENGTH} characters).'

    wants_json = 'application/json' in (request.headers.get('Accept') or '')
    if errors:
        if wants_json:
            return JsonResponse({'ok': False, 'errors': errors}, status=400)
        return redirect('/?contact=error')

    subject = f'Portfolio: message from {name}'
    body = (
        f'Name: {name}\n'
        f'Email: {email}\n'
        f'Sent: {request.META.get("REMOTE_ADDR", "unknown")}\n'
        f'\n{message}\n'
    )

    mail = EmailMessage(
        subject=subject,
        body=body,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[settings.CONTACT_TO_EMAIL],
        reply_to=[email],
    )

    try:
        mail.send()
    except Exception:
        logger.exception('Contact form email failed to send')
        if wants_json:
            return JsonResponse(
                {'ok': False, 'error': 'Could not send your message right now. Please try again.'},
                status=502,
            )
        return redirect('/?contact=error')

    if wants_json:
        return JsonResponse({'ok': True})
    return redirect('/?contact=sent')
