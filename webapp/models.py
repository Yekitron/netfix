from django.db import models


class Movies(models.Model):
    index = models.IntegerField(null=True, blank=True)
    budget = models.IntegerField(null=True, blank=True)
    homepage = models.CharField(max_length=100, null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    keywords = models.CharField(max_length=300, null=True, blank=True)
    original_title = models.CharField(max_length=200, null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    popularity = models.IntegerField(null=True, blank=True)
    production_companies = models.CharField(max_length=500, null=True, blank=True)
    production_countries = models.CharField(max_length=200,null=True, blank=True)
    release_date = models.CharField(max_length=100, null=True, blank=True)
    revenue = models.IntegerField(null=True, blank=True)
    runtime = models.IntegerField(null=True, blank=True)
    spoken_languages = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    tagline = models.TextField(null=True, blank=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    vote_average = models.CharField(max_length=100,null=True, blank=True)
    vote_count = models.IntegerField(null=True, blank=True)
    cast = models.TextField(null=True, blank=True)
    crew = models.TextField(null=True, blank=True)
    director = models.TextField(null=True, blank=True)


    def __str__(self):
        return (
            self.original_title, self.tagline,
            self.popularity, self.overview,
            self.id
            )






