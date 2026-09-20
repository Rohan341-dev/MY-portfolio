from django.contrib import admin
from .models import (
    Profile, IdentityTag, AboutParagraph, Project, Company,
    Achievement, Certificate, TechStackCategory, TechStackItem,
    TimelineEvent, ExploringItem, AILabCard, LeadershipPrinciple,
    BuildingUpdate
)


class IdentityTagInline(admin.TabularInline):
    model = IdentityTag
    extra = 1


class AboutParagraphInline(admin.TabularInline):
    model = AboutParagraph
    extra = 1


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 0
    fields = ('name', 'category', 'year', 'order', 'is_featured')


class CompanyInline(admin.TabularInline):
    model = Company
    extra = 0


class AchievementInline(admin.TabularInline):
    model = Achievement
    extra = 0


class CertificateInline(admin.TabularInline):
    model = Certificate
    extra = 0


class TechStackItemInline(admin.TabularInline):
    model = TechStackItem
    extra = 1


class TimelineEventInline(admin.TabularInline):
    model = TimelineEvent
    extra = 0


class ExploringItemInline(admin.TabularInline):
    model = ExploringItem
    extra = 1


class AILabCardInline(admin.TabularInline):
    model = AILabCard
    extra = 0


class LeadershipPrincipleInline(admin.TabularInline):
    model = LeadershipPrinciple
    extra = 0


class BuildingUpdateInline(admin.TabularInline):
    model = BuildingUpdate
    extra = 0


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('brand', 'name', 'location', 'updated_at')
    search_fields = ('name', 'brand')
    inlines = [
        IdentityTagInline,
        AboutParagraphInline,
        ProjectInline,
        CompanyInline,
        AchievementInline,
        CertificateInline,
        ExploringItemInline,
        AILabCardInline,
        LeadershipPrincipleInline,
        BuildingUpdateInline,
        TimelineEventInline,
    ]
    fieldsets = (
        ('Identity', {
            'fields': ('name', 'brand', 'title', 'location', 'profile_image', 'resume_file')
        }),
        ('Hero Section', {
            'fields': ('hero_title', 'hero_subtitle', 'hero_description', 'status_text')
        }),
        ('About', {
            'fields': ('bio', 'about_statement', 'about_philosophy')
        }),
        ('Contact & Social', {
            'fields': ('email', 'github_url', 'linkedin_url', 'instagram_url', 'facebook_url')
        }),
    )


@admin.register(TechStackCategory)
class TechStackCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    ordering = ('order',)
    inlines = [TechStackItemInline]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'year', 'is_featured', 'order')
    list_filter = ('category', 'is_featured')
    search_fields = ('name', 'tagline')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'order')
    ordering = ('order',)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'issuer', 'order')
    ordering = ('order',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'order')
    ordering = ('order',)


admin.site.site_header = 'Rohan Codekage — Portfolio Admin'
admin.site.site_title = 'Portfolio Admin'
admin.site.index_title = 'Content Management'
