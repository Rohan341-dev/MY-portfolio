from django.shortcuts import render, get_object_or_404
from .models import (
    Profile, Project, Company, Achievement, Certificate,
    TechStackCategory, TimelineEvent, ExploringItem,
    AILabCard, LeadershipPrinciple, BuildingUpdate
)


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
