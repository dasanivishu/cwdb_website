from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import UserRegistration, UserEditForm
from .forms import FormSubmissionForm

# Create your views here.

def index(request):
    return render(request,'authapp/index.html')

@login_required
def dashboard(request):
    context = {
        "welcome": "Welcome to your dashboard"
    }
    return render(request, 'authapp/dashboard.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/edit.html', context=context)


# from django.shortcuts import render, redirect

# change my complete views.py accordingly
# views.py
from django.shortcuts import render, redirect
from .models import FormSubmission
from .forms import FormSubmissionForm

@login_required
def form_submission_view(request):
    if request.method=='POST':
        form = FormSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('success_page')
    else:
        form = FormSubmissionForm()

    return render(request, 'authapp/form.html', {'form': form})

# @login_required
# def form_submission(request):
#     if request.method == 'POST':
#         uname = request.POST.get('uname')
#         name = request.POST.get('name')
#         dob = request.POST.get('dob')
#         mobile = request.POST.get('mobile')
#         gender = request.POST.get('gender')
#         nationality = request.POST.get('nationality')
#         # Continue to get other form field values
   
     
#       # Biodata and Photo Details
#         biodata = request.FILES.get('biodata')
#         photo = request.FILES.get('photo')

#     # Father/Spouse Details
#         father_spouse = request.POST.get('father_spouse')

#     # Expertise Area
#         expertise = request.POST.get('expertise')

#     # Personal Address Details
#         address1 = request.POST.get('address1')
#         address2 = request.POST.get('address2')
#         city = request.POST.get('city')
#         district = request.POST.get('district')
#         state = request.POST.get(' state')
#         pincode = request.POST.get('pincode')

#     # Institution Details
#         inst_state = request.POST.get('inst_state')
#         inst_district = request.POST.get(' inst_district')
#         institution = request.POST.get(' institution')
#         designation = request.POST.get(' designation')
#         department = request.POST.get('department')

#     # Qualifying Degree
#         QUALIFYING_DEGREE_CHOICES = (
#         ('M.S.', 'M.S.'),
#         ('M.D.', 'M.D.'),
#         ('PhD', 'PhD'),
#         )
#         qualifying_degree = request.POST.get('qualifying_degree')
#         degree_awarded = request.POST.get(' degree_awarded')
#         degree_date = request.POST.get(' degree_date')

#     # Thesis Title and Subject
#         thesis_title = request.POST.get('thesis_title')
#         subject = request.POST.get('subject')

#     # Research Supervisor/Guide and University/Institute
#         supervisor_guide = request.POST.get('supervisor_guide')
#         university_institute = request.POST.get('university_institute')

#     # Brief Details of Research Work
#         research_work_details = request.POST.get('research_work_details')

#     # Proposed Research Details
#         project_title = request.POST.get('project_title')
#         project_summary = request.POST.get('project_summary')
#         keywords = request.POST.get('keywords')
#         objectives = request.POST.get('objective')
#         result = request.POST.get('result')
#         methodology_work_plan = request.FILES.get('methodology_work_plan')

#     # Mentor Details
#         mentor_institute = request.POST.get('mentor_institute')
#         mentor_email = request.POST.get(' mentor_email')
#         mentor_name = request.POST.get('mentor_name')
#         registrar_email = request.POST.get('registrar_email')
#         phd_scholars_working = request.POST.get('phd_scholars_working')
#         postdoc_fellows_working = request.POST.get('postdoc_fellows_working')
    
#     # Upload
#         Undertaking = request.FILES.get('Undertaking')
#         Endorsement = request.FILES.get('Endorsement')
#         Birth = request.FILES.get('Birth')
#         CV= request.FILES.get('CV')
#         Plagiarism = request.FILES.get('Plagiarism')
#         Pub2 = request.FILES.get('Best Publication-2')
#         Caste = request.FILES.get('Caste')
#         Degree= request.FILES.get('Degree')
#         thesis = request.FILES.get('thesis')
#         Pub1 = request.FILES.get('Best Publication-1')
    
#     # Reference Details
#         reference1_name_address = request.POST.get('reference1_name_address')
#         reference1_email = request.POST.get('reference1_email')
#         reference1_contact = request.POST.get('reference1_contact')
#         reference2_name_address = request.POST.get('reference2_name_address')
#         reference2_email = request.POST.get('reference2_email')
#         reference2_contact = request.POST.get('reference2_contact')
    
#         form_submission = FormSubmission(
#             uname=uname,
#             name=name,
#             dob=dob,
#             mobile=mobile,
#             gender=gender,
#             nationality=nationality,biodata=biodata,
#             photo=photo,
#             father_spouse=father_spouse,expertise=expertise,
#             address1=address1,
#             address2=address2,
#             city=city,district=district,
#             state=state,pincode=pincode,
#             inst_state=inst_state,
#             inst_district=inst_district,
#             institution=institution,
#             designation=designation,
#             department= department,
#             qualifying_degree = qualifying_degree ,
#             degree_awarded=degree_awarded,
#             degree_date=degree_date,
#             thesis_title=thesis_title,
#             subject=subject,supervisor_guide=supervisor_guide,university_institute=university_institute,
#             research_work_details=research_work_details,project_title=project_title,
#             project_summary=project_summary,keywords=keywords,objectives=objectives,
#             result=result,methodology_work_plan=methodology_work_plan,
#             mentor_institute=mentor_institute,
#             mentor_name=mentor_name,
#             mentor_email=mentor_email,
#             registrar_email=registrar_email,
#             phd_scholars_working=phd_scholars_working,postdoc_fellows_working=postdoc_fellows_working,
#             Undertaking=Undertaking,
#             Endorsement=Endorsement,Birth=Birth,
#             CV=CV,Plagiarism=Plagiarism,Pub1=Pub1,Pub2=Pub2,Caste=Caste,Degree=Degree,
#             thesis=thesis,
#             reference1_name_address=reference1_name_address,
#             reference1_email=reference1_email,reference1_contact=reference1_contact,
#             reference2_name_address=reference2_name_address,reference2_email=reference2_email,
#             reference2_contact=reference2_contact



            
#             # Set other attributes here based on the form data
#         )
#         form_submission.save()
#         return redirect('authapp:dashboard')
#     return render(request, 'authapp/form.html')

# def success_page(request):
#     render(request, 'authapp/success.html')

# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FormSubmission
from django.utils.crypto import get_random_string

@login_required
def form_submission(request):
    if request.method == 'POST':
        # Process form submission and save the data
        uname = request.POST.get('uname')
        name = request.POST.get('name')
        dob = request.POST.get('dob')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        nationality = request.POST.get('nationality')
        father_spouse = request.POST.get('father_spouse')
        expertise = request.POST.get('expertise')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2')
        city = request.POST.get('city')
        district = request.POST.get('district')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        inst_state = request.POST.get('inst_state')
        inst_district = request.POST.get('inst_district')
        institution = request.POST.get('institution')
        designation = request.POST.get('designation')
        department = request.POST.get('department')
        qualifying_degree = request.POST.get('qualifying_degree')
        degree_awarded = request.POST.get('degree_awarded')
        degree_date = request.POST.get('degree_date')
        thesis_title = request.POST.get('thesis_title')
        subject = request.POST.get('subject')
        supervisor_guide = request.POST.get('supervisor_guide')
        university_institute = request.POST.get('university_institute')
        research_work_details = request.POST.get('research_work_details')
        project_title = request.POST.get('project_title')
        project_summary = request.POST.get('project_summary')
        keywords = request.POST.get('keywords')
        objectives = request.POST.get('objectives')
        result = request.POST.get('result')
        mentor_institute = request.POST.get('mentor_institute')
        mentor_email = request.POST.get('mentor_email')
        mentor_name = request.POST.get('mentor_name')
        registrar_email = request.POST.get('registrar_email')
        phd_scholars_working = request.POST.get('phd_scholars_working')
        postdoc_fellows_working = request.POST.get('postdoc_fellows_working')
        reference1_name_address = request.POST.get('reference1_name_address')
        reference1_email = request.POST.get('reference1_email')
        reference1_contact = request.POST.get('reference1_contact')
        reference2_name_address = request.POST.get('reference2_name_address')
        reference2_email = request.POST.get('reference2_email')
        reference2_contact = request.POST.get('reference2_contact')

        # Biodata and Photo Details
        biodata = request.FILES.get('biodata')
        photo = request.FILES.get('photo')

        # Upload
        Undertaking = request.FILES.get('Undertaking')
        Endorsement = request.FILES.get('Endorsement')
        Birth = request.FILES.get('Birth')
        CV = request.FILES.get('CV')
        Plagiarism = request.FILES.get('Plagiarism')
        Pub2 = request.FILES.get('Best Publication-2')
        Caste = request.FILES.get('Caste')
        Degree = request.FILES.get('Degree')
        thesis = request.FILES.get('thesis')
        Pub1 = request.FILES.get('Best Publication-1')

        # Generate a unique reference number
        reference_number = get_random_string(length=8)

        # Save the form data with the reference number and status
        form_submission = FormSubmission(
            uname=uname,
            name=name,
            dob=dob,
            mobile=mobile,
            gender=gender,
            nationality=nationality,
            father_spouse=father_spouse,
            expertise=expertise,
            address1=address1,
            address2=address2,
            city=city,
            district=district,
            state=state,
            pincode=pincode,
            inst_state=inst_state,
            inst_district=inst_district,
            institution=institution,
            designation=designation,
            department=department,
            qualifying_degree=qualifying_degree,
            degree_awarded=degree_awarded,
            degree_date=degree_date,
            thesis_title=thesis_title,
            subject=subject,
            supervisor_guide=supervisor_guide,
            university_institute=university_institute,
            research_work_details=research_work_details,
            project_title=project_title,
            project_summary=project_summary,
            keywords=keywords,
            objectives=objectives,
            result=result,
            mentor_institute=mentor_institute,
            mentor_email=mentor_email,
            mentor_name=mentor_name,
            registrar_email=registrar_email,
            phd_scholars_working=phd_scholars_working,
            postdoc_fellows_working=postdoc_fellows_working,
            reference1_name_address=reference1_name_address,
            reference1_email=reference1_email,
            reference1_contact=reference1_contact,
            reference2_name_address=reference2_name_address,
            reference2_email=reference2_email,
            reference2_contact=reference2_contact,
            reference_number=reference_number,
            status='Pending',
            biodata=biodata,
            photo=photo,
            Undertaking=Undertaking,
            Endorsement=Endorsement,
            Birth=Birth,
            CV=CV,
            Plagiarism=Plagiarism,
            Pub2=Pub2,
            Caste=Caste,
            Degree=Degree,
            thesis=thesis,
            Pub1=Pub1,
        )

        form_submission.save()

        return render(request, 'authapp/status.html', {'reference_number': reference_number})
    
    return render(request, 'authapp/form.html')

@login_required
def status_page(request):
    return render(request, 'authapp/status.html')

@login_required
def save_page(request):
    saved_forms = FormSubmission.objects.all()
    return render(request, 'authapp/save.html', {'saved_forms': saved_forms})

@login_required
def form_details(request, reference_number):
    try:
        form_submission = FormSubmission.objects.get(reference_number=reference_number)
        return render(request, 'authapp/form_details.html', {'form_submission': form_submission})
    except FormSubmission.DoesNotExist:
        return render(request, 'authapp/form_not_found.html')

@login_required
def success_page(request):
    return render(request, 'authapp/success.html')

@login_required
def proposal_inbox(request):
    proposals = FormSubmission.objects.all()
    return render(request, 'authapp/proposal_inbox.html', {'proposals': proposals})