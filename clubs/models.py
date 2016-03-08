from django.db import models
 # TODO: Add a weekly meeting time.

"""
So this is a model file.

How does it work?
Basically, I mocked up my app in Sketch and
I asked myself what I wanted my app to look like. After I did
that, I outlined what kind of data I wanted to store. Mocking
up my data isn't necessary, but it gives me a general idea of
what kind of data I'm going to be working with.

After I mocked up my app, I used this models file to edit the
outline of how I want my data to be stored in a 'clubs' file.

REMEMBER: After every single time I edit the models file, I
need to let Django translate everything into database
language (SQL). This means after every single time I edit
models, I MUST run in bash (or command line) at the project
directory the command:

>> python manage.py makemigrations clubs

Which tells Python: Hey, I made some changes to the model.
Read through what I did, and make the relevant changes to
how you handle databases. Python then makes a list of
changes that need to be done, but this isn't actually
applied because as the name 'makemigrations' implies,
it only creates the changes to be made. It doesn't make
them. If I want to make the changes, I must type:

>> python manage.py migrate

Which then changes the database and makes it ready to
handle the new type of data that I'm storing.

Cool, huh?
"""
class Club(models.Model):
    ACADEMIC                = "AC"
    AFFINITY                = "AF"
    AWARENESS               = "AW"
    MEDIA_AND_PUBLICATIONS  = "ME"
    MUSIC                   = "MU"
    PREPROFESSIONAL         = "PR"
    RELIGIOUS_AND_SPIRITUAL = "RE"
    SERVICE                 = "SE"
    SPECIAL_INTEREST        = "SP"
    SPORTS_AND_OUTDOORS     = "OU"
    STUDENT_GOVERNMENT      = "ST"
    VISUAL_PERF_ART         = "AR"

    CATEGORY_CHOICES = (
        (ACADEMIC, "Academic"),
        (AFFINITY, "Affinity Group"),
        (AWARENESS, "Awareness and Activism"),
        (MEDIA_AND_PUBLICATIONS, "Media and Publications"),
        (MUSIC, "Music"),
        (PREPROFESSIONAL, "Preprofessional Society"),
        (RELIGIOUS_AND_SPIRITUAL, "Religious and Spiritual Groups"),
        (SERVICE, "Service Groups"),
        (SPECIAL_INTEREST, "Special Interests and Hobbies"),
        (SPORTS_AND_OUTDOORS, "Sports and Outdoors Clubs"),
        (STUDENT_GOVERNMENT, "Student Government Organization"),
        (VISUAL_PERF_ART, "Visual and Performing Arts"),
        )
    category       = models.CharField(max_length=2,
                                   choices = CATEGORY_CHOICES,
                                      default=ACADEMIC)
    cover_image    = models.ImageField()
    name           = models.CharField(max_length=20, default="Your Club Name Here")
    contact_person = models.CharField(max_length=20, default="Dan Weiss")
    contact_email  = models.CharField(max_length=20, default="dweiss@haverford.edu")
    club_website   = models.CharField(max_length=50, default="http://myclub.com")
    tagline        = models.CharField(max_length=40, default="Something clever.")
    description    = models.TextField()
    image_1        = models.ImageField()
    image_2        = models.ImageField()
    image_3        = models.ImageField()

    def __str__(self):
        return self.name
