from django.db import models
from django.conf import settings
# Create your models here.


class UserRegistrationModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


# testt/models.py
from django.db import models

class FormSubmission(models.Model):
    # Profile Details
    
    uname = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='', null=True)
    dob = models.DateField("Date", null=True,blank=True)
    mobile = models.CharField(max_length=15, default='', null=True)
    gender = models.CharField(max_length=10, default='', null=True)
    nationality = models.CharField(max_length=50, default='', null=True)

    # Biodata and Photo Details
    biodata = models.FileField(upload_to='uploads/', null=True, default=None)
    photo = models.ImageField(upload_to='uploads/', null=True, default=None)

    # Father/Spouse Details
    father_spouse = models.CharField(max_length=100, default='', null=True)

    # Expertise Area
    expertise = models.CharField(max_length=100, default='', null=True)

    # Personal Address Details
    address1 = models.CharField(max_length=100, default='', null=True)
    address2 = models.CharField(max_length=100, default='', null=True)
    city = models.CharField(max_length=50, default='', null=True)
    district = models.CharField(max_length=50, default='', null=True)
    state = models.CharField(max_length=50, default='', null=True)
    pincode = models.CharField(max_length=10, default='', null=True)

    # Institution Details
    inst_state = models.CharField(max_length=50, default='', null=True)
    inst_district = models.CharField(max_length=50, default='', null=True)
    institution = models.CharField(max_length=100, default='', null=True)
    created_date = models.DateTimeField(auto_now_add=True)

    designation = models.CharField(max_length=100, default='', null=True)
    department = models.CharField(max_length=100, default='', null=True)

    # Qualifying Degree
    QUALIFYING_DEGREE_CHOICES = (
        ('M.S.', 'M.S.'),
        ('M.D.', 'M.D.'),
        ('PhD', 'PhD'),
    )
    qualifying_degree = models.CharField(max_length=5, choices=QUALIFYING_DEGREE_CHOICES, default='M.S.')
    degree_awarded = models.CharField(max_length=3, choices=(('Yes', 'Yes'), ('No', 'No')), default='Yes', null=True)
    degree_date = models.DateField("Date", null=True,blank=True)

    # Thesis Title and Subject
    thesis_title = models.CharField(max_length=100, default='', null=True)
    subject = models.CharField(max_length=200, default='', null=True)

    # Research Supervisor/Guide and University/Institute
    supervisor_guide = models.CharField(max_length=200, default='', null=True)
    university_institute = models.CharField(max_length=200, default='', null=True)

    # Brief Details of Research Work
    research_work_details = models.TextField(max_length=6000, default='', null=True)

    # Proposed Research Details
    project_title = models.CharField(max_length=500, default='', null=True)
    project_summary = models.TextField(max_length=500, default='', null=True)
    keywords = models.CharField(max_length=180, default='', null=True)
    objectives = models.TextField(max_length=1500, default='', null=True)
    result = models.TextField(max_length=1500, default='', null=True)
    methodology_work_plan = models.FileField(upload_to='uploads/', null=True, default=None)

    # Mentor Details
    mentor_institute = models.CharField(max_length=100, default='', null=True)
    mentor_email = models.EmailField(default='', null=True)
    mentor_name = models.CharField(max_length=100, default='', null=True)
    registrar_email = models.EmailField(default='', null=True)
    phd_scholars_working = models.PositiveIntegerField(default=1, null=True)
    postdoc_fellows_working = models.PositiveIntegerField(default=1, null=True)

    # Upload
    Undertaking = models.FileField(upload_to='uploads/', default=None, null=True)
    Endorsement = models.FileField(upload_to='uploads/', default=None, null=True)
    Birth = models.FileField(upload_to='uploads/', default=None, null=True)
    CV = models.FileField(upload_to='uploads/', default=None, null=True)
    Plagiarism = models.FileField(upload_to='uploads/', default=None, null=True)
    Pub2 = models.FileField(upload_to='uploads/', default=None, null=True)
    Caste = models.FileField(upload_to='uploads/', default=None, null=True)
    Degree = models.FileField(upload_to='uploads/', default=None, null=True)
    thesis = models.FileField(upload_to='uploads/', default=None, null=True)
    Pub1 = models.FileField(upload_to='uploads/', default=None, null=True)

    # reference number and status
    reference_number = models.CharField(max_length=8, unique=True, default='')
    status = models.CharField(max_length=20, default='Pending')
    # Reference Details
    reference1_name_address = models.TextField(max_length=1000, default='', null=True)
    reference1_email = models.EmailField(default='', null=True)
    reference1_contact = models.CharField(max_length=50, default='', null=True)
    reference2_name_address = models.TextField(max_length=1000, default='', null=True)
    reference2_email = models.EmailField(default='', null=True)
    reference2_contact = models.CharField(max_length=50, default='', null=True)

    def __str__(self):
        return self.uname



