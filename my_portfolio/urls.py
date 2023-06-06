from django.urls import path


urlpatterns = []

from .views.home import Home
urlpatterns += [
    path('', Home.as_view(), name="home"),
]


from .views.about_me import Add_about_me, About_me_list
urlpatterns += [
    path('about_me/', About_me_list.as_view(), name="about_me_list"),
    path('about_me/add/', Add_about_me.as_view(), name="add_about_me"),
]


from .views.experience import Add_experience, Experience_list
urlpatterns += [
    path('experience/', Experience_list.as_view(), name="experience_list"),
    path('experience/add/', Add_experience.as_view(), name="add_experience"),
]


from .views.education import Add_education, Education_list
urlpatterns += [
    path('education/', Education_list.as_view(), name="education_list"),
    path('education/add/', Add_education.as_view(), name="add_education"),
]


from .views.skills import Add_skills, Skills_list
urlpatterns += [
    path('skills/', Skills_list.as_view(), name="skills_list"),
    path('skills/add/', Add_skills.as_view(), name="add_skills"),
]


from .views.project import Add_projects, Projects_list
urlpatterns += [
    path('projects/', Projects_list.as_view(), name="projects_list"),
    path('projects/add/', Add_projects.as_view(), name="add_projects"),
]
