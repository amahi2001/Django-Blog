from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    #lets us only preview the text
    def summary(self):
        if len(self.body) > 100:
            return self.body[:100]+'...'
        return self.body

    #lets us display the date in a better format
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y') #prints out the month, day and year published