from django.db import models

# Create your models for blog:
# title
# publish date
# image
# body
# add the blog app  to setting
# .make migrations
#migrate
# add app to admin



class Blog(models.Model):
    title=models.CharField(max_length=200)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='images/')
    body=models.TextField()

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e, %Y ')

    def __str__(self):
        return self.title