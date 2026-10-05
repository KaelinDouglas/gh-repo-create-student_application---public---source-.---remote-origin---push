from django.shortcuts import render, redirect


DEGREE_MAJORS = ['Computer Science', 'Software Engineering', 'Data Science', 'Information Systems', 'Cybersecurity']
YEAR_STANDINGS = ['Freshman', 'Sophomore', 'Junior', 'Senior']
CODING_LANGUAGES = ['Python', 'Java', 'C++', 'JavaScript', 'SQL', 'HTML/CSS']

def entry_form_view(request):
    """Processes the form submission and validates required fields."""
    validation_error = None

    if request.method == 'POST':
    
        full_name = request.POST.get('student_name', '').strip()
        student_id = request.POST.get('student_id', '').strip()
        chosen_major = request.POST.get('major')
        academic_standing = request.POST.get('class_standing')
        selected_languages = request.POST.getlist('languages_known')
        grad_year = request.POST.get('expected_grad')
        user_comments = request.POST.get('comments')

        
        if not full_name:
            validation_error = "Student Name cannot be blank."
        elif not student_id:
            validation_error = "Student ID cannot be blank."

        if validation_error:
            
            return render(request, 'portal/form.html', {
                'error_msg': validation_error,
                'major_options': DEGREE_MAJORS,
                'standing_options': YEAR_STANDINGS,
                'language_options': CODING_LANGUAGES,
                'submitted_data': request.POST,
                'selected_langs': selected_languages,
            })

        
        request.session['record_payload'] = {
            'student_name': full_name,
            'student_id': student_id,
            'major': chosen_major,
            'class_standing': academic_standing,
            'languages': ', '.join(selected_languages) if selected_languages else 'None',
            'expected_grad': grad_year,
            'comments': user_comments,
        }
        return redirect('registration_summary')

    
    return render(request, 'portal/form.html', {
        'major_options': DEGREE_MAJORS,
        'standing_options': YEAR_STANDINGS,
        'language_options': CODING_LANGUAGES,
    })

def summary_view(request):
    """Displays the registration summary results."""
    registration_record = request.session.get('record_payload', {})
    return render(request, 'portal/results.html', {'record': registration_record})