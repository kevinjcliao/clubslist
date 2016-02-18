from django.db import models

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
        (RELIGIOUS_AND_SPIRITUAL, "Religious and Spiritugal Groups"),
        (SERVICE, "Service Groups"),
        (SPECIAL_INTEREST, "Special Interests and Hobbies"),
        (SPORTS_AND_OUTDOORS, "Sports and Outdoors Clubs"),
        (STUDENT_GOVERNMENT, "Student Government Organization"),
        (VISUAL_PERF_ART, "Visual and Performing Arts"),
        )
    category    = models.CharField(max_length=2,
                                   choices = CATEGORY_CHOICES, default=ACADEMIC)
    cover_image = models.ImageField()
    name        = models.CharField(max_length=20)
    tagline     = models.CharField(max_length=40)
    description = models.TextField()
    image_1     = models.ImageField()
    image_2     = models.ImageField()
    image_3     = models.ImageField()
