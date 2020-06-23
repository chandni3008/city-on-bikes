from django.db import models

class Register(models.Model):
      username = models.CharField(max_length=250, default='farzi username')
      contact = models.CharField(max_length=250, default='farzi contact')
      def __str__(self):
            return str(self.username)

class Bike(models.Model):
      pickup=models.CharField(max_length=70)
      dropat=models.CharField(max_length=70)
      kilo=models.FloatField(max_length=20)
      pickdate=models.DateField(max_length=20)
      picktime=models.TimeField(max_length=20)
      dropdate=models.DateField(max_length=20)
      droptime=models.TimeField(max_length=20)
      
      class Meta:
            get_latest_by = ['id']
      def __str__(self):
            return str(self.pickdate)

class Estimate(models.Model):
      username=models.CharField(max_length=50)
      contact=models.CharField(max_length=20)
      license_name=models.CharField(max_length=50)
      license_image=models.FileField(upload_to='images/')
      
      def __str__(self):
            return str(self.username)

class Bookride(models.Model):
      title = models.CharField(max_length=100,blank=True)
      description = models.TextField(blank=True)
      cost=models.IntegerField(blank=True,null=True)
      image = models.ImageField(upload_to='media/image',default='')
      
      def __str__(self):
            return str(self.title)

class Contact(models.Model):
      name = models.CharField(max_length=50)
      email = models.EmailField()
      subject = models.CharField(max_length=50)
      message = models.TextField(max_length=50)
      def __str__(self):
            return str(self.email)