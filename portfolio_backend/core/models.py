from django.db import models
from django.contrib import admin


class Profile(models.Model):
    name = models.CharField(max_length=100, default='Rohan Yadav')
    brand = models.CharField(max_length=100, default='Rohan Codekage')
    title = models.CharField(max_length=200, default='Student Programmer · Full-Stack Developer · AI Builder · Founder')
    location = models.CharField(max_length=100, default='Nepal')
    bio = models.TextField(blank=True)
    about_statement = models.TextField(blank=True, help_text='Opening quote for About section')
    about_philosophy = models.TextField(blank=True, help_text='Philosophy quote')
    hero_title = models.CharField(max_length=300, default='I build things that turn ideas into reality.')
    hero_subtitle = models.TextField(default="I'm Rohan Yadav — a student programmer, full-stack developer, AI/LLM builder, and tech entrepreneur from Nepal.")
    hero_description = models.TextField(default='I build web applications, SaaS products, AI-powered tools, and experimental systems while constantly exploring what is possible with technology.')
    status_text = models.CharField(max_length=100, default='Currently building')
    email = models.EmailField(default='rohan@example.com')
    github_url = models.URLField(default='https://github.com/Rohan341-dev')
    linkedin_url = models.URLField(default='https://np.linkedin.com/in/rohan-codekage-746656356')
    instagram_url = models.URLField(default='https://www.instagram.com/rohanl2l')
    facebook_url = models.URLField(default='https://www.facebook.com/rohanl2l')
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return f'{self.brand} — Profile'


class IdentityTag(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='identity_tags')
    label = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Identity Tag'
        verbose_name_plural = 'Identity Tags'

    def __str__(self):
        return self.label


class AboutParagraph(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='about_paragraphs')
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    is_highlight = models.BooleanField(default=False, help_text='Highlight this paragraph')

    class Meta:
        ordering = ['order']
        verbose_name = 'About Paragraph'
        verbose_name_plural = 'About Paragraphs'

    def __str__(self):
        return f'Paragraph {self.order}'


class Project(models.Model):
    CATEGORY_CHOICES = [
        ('product', 'Product'),
        ('fullstack', 'Full-Stack'),
        ('ai', 'AI / ML'),
        ('system', 'System'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='projects')
    name = models.CharField(max_length=200)
    tagline = models.CharField(max_length=300)
    year = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    role = models.CharField(max_length=200)
    focus = models.CharField(max_length=300)
    problem = models.TextField(blank=True)
    solution = models.TextField(blank=True)
    outcome = models.TextField(blank=True)
    technologies = models.CharField(max_length=500, blank=True, help_text='Comma-separated')
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['order']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.name


class Company(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='companies')
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    tagline = models.CharField(max_length=300)
    quote = models.TextField(blank=True)
    description = models.TextField(blank=True)
    services = models.CharField(max_length=1000, blank=True, help_text='Comma-separated services')
    roles = models.CharField(max_length=500, blank=True, help_text='Comma-separated role tags')
    website_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class Achievement(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='achievements')
    title = models.CharField(max_length=200)
    description = models.TextField()
    year = models.CharField(max_length=50)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Achievement'
        verbose_name_plural = 'Achievements'

    def __str__(self):
        return self.title


class Certificate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='certificates')
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    image = models.ImageField(upload_to='certificates/')
    year = models.CharField(max_length=50, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Certificate'
        verbose_name_plural = 'Certificates'

    def __str__(self):
        return self.name


class TechStackCategory(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='stack_categories')
    name = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Stack Category'
        verbose_name_plural = 'Stack Categories'

    def __str__(self):
        return self.name


class TechStackItem(models.Model):
    category = models.ForeignKey(TechStackCategory, on_delete=models.CASCADE, related_name='items')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Stack Item'
        verbose_name_plural = 'Stack Items'

    def __str__(self):
        return self.name


class TimelineEvent(models.Model):
    TYPE_CHOICES = [
        ('journey', 'Journey'),
        ('founder', 'Founder Journey'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='timeline_events')
    event_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='journey')
    phase = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Timeline Event'
        verbose_name_plural = 'Timeline Events'

    def __str__(self):
        return f'{self.title} ({self.get_event_type_display()})'


class ExploringItem(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='exploring_items')
    label = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Exploring Item'
        verbose_name_plural = 'Exploring Items'

    def __str__(self):
        return self.label


class AILabCard(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='ailab_cards')
    number = models.CharField(max_length=5)
    tag = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'AI Lab Card'
        verbose_name_plural = 'AI Lab Cards'

    def __str__(self):
        return self.title


class LeadershipPrinciple(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='leadership_principles')
    number = models.CharField(max_length=5)
    title = models.CharField(max_length=300)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Leadership Principle'
        verbose_name_plural = 'Leadership Principles'

    def __str__(self):
        return self.title


class BuildingUpdate(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='building_updates')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_label = models.CharField(max_length=50, default='Recent')
    tags = models.CharField(max_length=300, blank=True, help_text='Comma-separated tags')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
        verbose_name = 'Building Update'
        verbose_name_plural = 'Building Updates'

    def __str__(self):
        return self.title
