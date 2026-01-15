from django.db import models

class Profile(models.Model):
    full_name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField(unique=True)
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    problem_statement = models.TextField()
    solution = models.TextField()
    tech_stack = models.CharField(max_length=300)
    github_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # null if currently working
    responsibilities = models.TextField()

    def __str__(self):
        return f"{self.job_title} at {self.company_name}"
    

class Education(models.Model):
    institution_name = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    field_of_study = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} in {self.field_of_study} from {self.institution_name}"
    

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
