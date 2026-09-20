from django.core.management.base import BaseCommand
from core.models import (
    Profile, IdentityTag, AboutParagraph, Project, Company,
    Achievement, Certificate, TechStackCategory, TechStackItem,
    TimelineEvent, ExploringItem, AILabCard, LeadershipPrinciple,
    BuildingUpdate
)


class Command(BaseCommand):
    help = 'Seed the database with portfolio content'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        profile, _ = Profile.objects.get_or_create(
            id=1,
            defaults={
                'name': 'Rohan Yadav',
                'brand': 'Rohan Codekage',
                'title': 'Student Programmer · Full-Stack Developer · AI Builder · Founder',
                'location': 'Nepal',
                'bio': 'Portfolio of Rohan Yadav, also known as Rohan Codekage — a Nepalese student programmer, full-stack developer, AI/LLM explorer, and tech entrepreneur building web applications, SaaS products, and experimental technology.',
                'about_statement': '"I started with curiosity. Now I build with purpose."',
                'about_philosophy': '"Don\'t just learn technology. Build something with it."',
                'hero_title': 'I build things that\nturn ideas into reality.',
                'hero_subtitle': "I'm Rohan Yadav — a student programmer, full-stack developer, AI/LLM builder, and tech entrepreneur from Nepal.",
                'hero_description': 'I build web applications, SaaS products, AI-powered tools, and experimental systems while constantly exploring what is possible with technology.',
                'status_text': 'Currently building',
                'email': 'rohan@example.com',
                'github_url': 'https://github.com/Rohan341-dev',
                'linkedin_url': 'https://np.linkedin.com/in/rohan-codekage-746656356',
                'instagram_url': 'https://www.instagram.com/rohanl2l',
                'facebook_url': 'https://www.facebook.com/rohanl2l',
            }
        )

        # Identity Tags
        tags = ['FULL-STACK DEVELOPER', 'AI / LLM', 'BUILDER', 'ENTREPRENEUR', 'FOUNDER']
        for i, tag in enumerate(tags):
            IdentityTag.objects.get_or_create(profile=profile, label=tag, defaults={'order': i})

        # About Paragraphs
        about_paras = [
            "I didn't start with a plan. I started with a browser, a broken HTML page, and the question: <em>\"How does this actually work?\"</em>",
            "That question led me down a path I never fully mapped out — from writing my first lines of HTML and CSS, to building full-stack applications, exploring AI and large language models, launching SaaS products, and experimenting with systems that solve real problems.",
            "I'm Rohan Yadav, publicly known as <strong>Rohan Codekage</strong>. I'm a student programmer and full-stack developer based in Nepal. I'm still young, still learning, and still very much at the beginning — but I've already built things I'm genuinely proud of.",
            "My journey has taken me from basic frontend work into backend systems, databases, APIs, full-stack development, SaaS architecture, AI/LLM experimentation, automation, and product development. I've built management systems, e-commerce platforms, AI tools, and experimental hardware projects.",
            "I enjoy the entire process — taking an idea from <strong>Idea → Research → Design → Code → Debug → Improve → Ship</strong>. Every project teaches me something new, and every failure becomes the foundation for the next attempt.",
            "My interests extend beyond traditional software development. I'm curious about AI and how language models can be integrated into real products. I experiment with computer vision, automation, SaaS architecture, EdTech, e-commerce, hardware like Arduino, and physics-inspired systems.",
            "I don't just want to learn technology. I want to build with it. And I want to build things that matter.",
            "But somewhere along the way, I realized something. The best code in the world doesn't matter if it doesn't reach the people who need it. That realization pushed me beyond writing software — into building teams, companies, and products that solve real problems.",
            "Today, I'm the <strong>Founder of SajiloCode Pvt. Ltd.</strong> and <strong>CEO & Founder of Code Nest Nepal Pvt. Ltd.</strong> — two ventures born from the same curiosity that first led me to a browser and a broken HTML page.",
        ]
        for i, content in enumerate(about_paras):
            AboutParagraph.objects.get_or_create(profile=profile, content=content, defaults={'order': i})

        # Projects
        projects_data = [
            {'name': 'SajiloCode', 'tagline': 'A technology & product initiative focused on software, education, and real-world business systems.', 'year': '2024 — Present', 'category': 'product', 'role': 'Founder / Developer', 'focus': 'SaaS · EdTech · Business Systems · E-commerce', 'problem': 'Schools, restaurants, and small businesses in Nepal often rely on manual processes, paper-based records, or expensive imported software.', 'solution': 'SajiloCode was created as a product lab — a space to build and ship real-world systems.', 'outcome': 'Moving from coding into product thinking and entrepreneurship.', 'technologies': 'Python, Django, HTML, CSS, JavaScript, SQLite, PostgreSQL, REST APIs', 'order': 0, 'is_featured': True},
            {'name': 'Shope-ease', 'tagline': 'An e-commerce platform designed for product discovery and online shopping.', 'year': '2024', 'category': 'product', 'role': 'Founder + Developer', 'focus': 'E-commerce · Product Discovery · Online Shopping', 'problem': 'E-commerce platforms often feel generic and disconnected from local markets.', 'solution': 'Shope-ease was launched as an experiment in real-world digital commerce.', 'outcome': 'An early experiment with building real-world digital commerce.', 'technologies': 'HTML, CSS, JavaScript, Python, Django, SQLite', 'order': 1},
            {'name': 'AxisOne', 'tagline': 'A unified platform designed around students — Learn, Build, Launch.', 'year': '2024 — Present', 'category': 'product', 'role': 'Founder / Developer', 'focus': 'Learning · Digital Tools · Startup Building · Student Resources', 'problem': 'Students often lack a centralized platform that combines learning, building, and launching.', 'solution': 'AxisOne is designed as a unified ecosystem for students.', 'technologies': 'Next.js, React, Tailwind CSS, Python, PostgreSQL, REST APIs', 'order': 2},
            {'name': 'Smart School Route Management System', 'tagline': 'A school transportation and safety platform — GPS tracking, route management, driver monitoring, and real-time alerts.', 'year': '2024 — 2025', 'category': 'system', 'role': 'Lead Developer', 'focus': 'Safety · GPS Tracking · Route Optimization · Computer Vision', 'problem': 'School transportation systems often lack visibility.', 'solution': 'A comprehensive system combining GPS tracking, route management, driver monitoring, real-time dashboards.', 'outcome': 'Building systems that solve real-world problems, not just websites.', 'technologies': 'HTML, CSS, JavaScript, Python, Django, FastAPI, SQLite, PostgreSQL, MediaPipe, OpenCV', 'order': 3},
            {'name': 'GPS & Location Tracking Systems', 'tagline': 'Engineering experiments in GPS, device communication, real-time data, and location-based systems.', 'year': '2024', 'category': 'system', 'role': 'Developer / Researcher', 'focus': 'GPS · Location Systems · Device Communication · Real-time Data', 'solution': 'Experiments with GPS modules, location APIs, device communication, real-time dashboards, hardware integration.', 'technologies': 'Python, JavaScript, GPS APIs, Hardware, Arduino, REST APIs', 'order': 4},
        ]
        for data in projects_data:
            Project.objects.get_or_create(profile=profile, name=data['name'], defaults=data)

        # Companies
        companies_data = [
            {'name': 'SajiloCode Pvt. Ltd.', 'role': 'Founder', 'tagline': 'An IT and custom software development company focused on building practical digital solutions.', 'quote': "I didn't want to only build software. I wanted to build the team and the system behind it.", 'services': 'Web Development, Custom Software, SaaS, School Management, Restaurant Management, CRM, Billing Systems, CMS, E-commerce, ERP, HRM, Business Automation', 'roles': 'Founder, Product Builder, Developer, Team Leadership', 'order': 0},
            {'name': 'Code Nest Nepal Pvt. Ltd.', 'role': 'CEO & Founder', 'tagline': 'Software and SaaS development focused on helping organizations build and automate their digital operations.', 'quote': 'Building software. Building teams. Building the next version of myself.', 'services': 'SaaS Development, Business Websites, CMS, E-commerce, School Management, Restaurant Management, CRM, Lead Management, Business Automation, Custom Software', 'roles': 'Leadership, Product Strategy, Development, Team Building, Technology', 'order': 1},
        ]
        for data in companies_data:
            Company.objects.get_or_create(profile=profile, name=data['name'], defaults=data)

        # Achievements
        achievements_data = [
            {'title': 'SajiloCode — Founded', 'description': 'Launched a technology initiative building management systems, SaaS products, and business automation tools.', 'year': '2024', 'order': 0},
            {'title': 'Shope-ease — Launched', 'description': 'Built and launched an e-commerce platform covering electronics, fashion, and fitness products.', 'year': '2024', 'order': 1},
            {'title': 'Mathematics Competitions', 'description': 'Participated in mathematics competitions and olympiad-level problem solving.', 'year': '2024', 'order': 2},
            {'title': 'Smart School Route System', 'description': 'Designed and built a comprehensive school transportation safety platform.', 'year': '2024 — 2025', 'order': 3},
            {'title': 'AI / LLM Experiments', 'description': 'Started active experimentation with large language models, AI agents, and applied artificial intelligence.', 'year': '2025', 'order': 4},
            {'title': 'Building in Public', 'description': 'Sharing the journey of learning, building, and creating technology — transparently and authentically.', 'year': 'Ongoing', 'order': 5},
        ]
        for data in achievements_data:
            Achievement.objects.get_or_create(profile=profile, title=data['title'], defaults=data)

        # Tech Stack
        stack_data = {
            'Frontend': [('HTML', 'markup'), ('CSS', 'styling'), ('JavaScript', 'scripting'), ('React', 'UI library'), ('Next.js', 'framework'), ('Tailwind CSS', 'utility CSS')],
            'Backend': [('Python', 'language'), ('Flask', 'micro-framework'), ('Django', 'full framework'), ('REST APIs', 'architecture'), ('SQLite', 'embedded DB'), ('PostgreSQL', 'relational DB')],
            'AI / ML': [('LLMs', 'language models'), ('AI Agents', 'autonomous systems'), ('Computer Vision', 'image processing'), ('OpenCV', 'vision library'), ('MediaPipe', 'ML solutions')],
            'Tools': [('Git', 'version control'), ('GitHub', 'repository'), ('VS Code', 'editor'), ('macOS / Linux', 'environment'), ('APIs', 'integration')],
            'Product / Systems': [('SaaS', 'software as a service'), ('Automation', 'workflow'), ('Dashboards', 'data viz'), ('Management Systems', 'operations'), ('E-commerce', 'commerce'), ('EdTech', 'education')],
        }
        for i, (cat_name, items) in enumerate(stack_data.items()):
            cat, _ = TechStackCategory.objects.get_or_create(profile=profile, name=cat_name, defaults={'order': i})
            for j, (item_name, desc) in enumerate(items):
                TechStackItem.objects.get_or_create(category=cat, name=item_name, defaults={'description': desc, 'order': j})

        # Timeline Events - Journey
        journey_data = [
            ('Beginning', 'Early Coding', 'Started exploring programming and computers at a young age.'),
            ('Foundation', 'Frontend Development', 'HTML → CSS → JavaScript. Learning the building blocks of the web.'),
            ('Growth', 'Full-Stack Development', 'Backend → APIs → Databases → Frameworks.'),
            ('Products', 'Product Development', 'SaaS → Management Systems → E-commerce → EdTech.'),
            ('Exploration', 'AI Exploration', 'LLMs → AI Agents → Computer Vision → Automation.'),
            ('Ventures', 'Entrepreneurship', 'Turning technical ideas into products and ventures.'),
            ('Next', "What's Next", 'Continue learning, building, experimenting, and shipping.'),
        ]
        for i, (phase, title, desc) in enumerate(journey_data):
            TimelineEvent.objects.get_or_create(profile=profile, title=title, event_type='journey', defaults={'phase': phase, 'description': desc, 'order': i})

        # Timeline Events - Founder
        founder_data = [
            ('01', 'Developer', 'Started by learning how to build software.'),
            ('02', 'Builder', 'Started creating real-world projects and experimenting with different technologies.'),
            ('03', 'Product Thinker', 'Started thinking about users, problems, products, and systems.'),
            ('04', 'Founder', 'Built SajiloCode and began developing products with a team.'),
            ('05', 'CEO', 'Expanded into leadership, business development, product direction.'),
            ('06', "What's Next", 'Continue building companies, products, technology.'),
        ]
        for i, (phase, title, desc) in enumerate(founder_data):
            TimelineEvent.objects.get_or_create(profile=profile, title=title, event_type='founder', defaults={'phase': phase, 'description': desc, 'order': i})

        # Exploring Items
        exploring = ['AI / LLMs', 'Computer Vision', 'Next.js', 'Python', 'SaaS Architecture', 'Automation', 'Developer Tools', 'Product Design']
        for i, label in enumerate(exploring):
            ExploringItem.objects.get_or_create(profile=profile, label=label, defaults={'order': i})

        # AI Lab Cards
        ailab_data = [
            ('01', 'LLMs', 'Language Model Experiments', 'Working with large language models for content generation, summarization, and developer productivity tools.'),
            ('02', 'AGENTS', 'AI Agent Systems', 'Building autonomous and semi-autonomous AI agents that can reason, plan, and execute multi-step tasks.'),
            ('03', 'VISION', 'Computer Vision', 'Exploring OpenCV and MediaPipe for real-time image processing, face detection, hand tracking.'),
            ('04', 'AUTOMATION', 'AI-Powered Automation', 'Creating systems that automate repetitive tasks using AI.'),
            ('05', 'DEV TOOLS', 'Developer Productivity', 'Building AI-assisted coding tools and development workflow enhancers.'),
            ('06', 'APPLIED AI', 'Applied AI Products', 'Integrating AI capabilities into real products.'),
        ]
        for i, (num, tag, title, desc) in enumerate(ailab_data):
            AILabCard.objects.get_or_create(profile=profile, title=title, defaults={'number': num, 'tag': tag, 'description': desc, 'order': i})

        # Leadership Principles
        leadership_data = [
            ('01', 'Build with people, not just for people.', 'The best products are built through collaboration, trust, and shared purpose.'),
            ('02', 'Give ideas room to become products.', 'Every idea deserves the chance to be explored.'),
            ('03', 'Learn from mistakes instead of hiding them.', 'Mistakes are data. They tell you what doesn\'t work.'),
            ('04', 'A company is more than its software.', "It's the people, systems, culture, and vision behind it."),
            ('05', 'Leadership is another form of building.', 'Just as code is built line by line, leadership is built decision by decision.'),
        ]
        for i, (num, title, desc) in enumerate(leadership_data):
            LeadershipPrinciple.objects.get_or_create(profile=profile, title=title, defaults={'number': num, 'description': desc, 'order': i})

        # Building Updates
        building_data = [
            ('AI Agent Experiments', 'Running experiments with autonomous AI agents — testing tool use, memory systems, and multi-step reasoning.', 'Recent', 'AI, Agents'),
            ('SajiloCode Products', 'Continuously expanding the SajiloCode product lineup.', 'Recent', 'SaaS, Product'),
            ('Computer Vision Projects', 'Exploring real-time computer vision applications using OpenCV and MediaPipe.', 'Recent', 'Vision, OpenCV'),
        ]
        for i, (title, desc, date, tags) in enumerate(building_data):
            BuildingUpdate.objects.get_or_create(profile=profile, title=title, defaults={'description': desc, 'date_label': date, 'tags': tags, 'order': i})

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
