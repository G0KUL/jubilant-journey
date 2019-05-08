import sys

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.views.decorators.csrf import csrf_exempt

from . import models

# Create your views here.


def login(request):
	request.session.flush()
	return render(request, 'login.html')


def home(request):
	if request.session.has_key('username'):
		role = request.session['role']

		if role == 'student':
			return render(request, 'student.html')
		elif role == 'faculty':
			return render(request, 'faculty.html')
		elif role == 'admin':
			return render(request, "admin.html")
		elif role == 'ta':
			return render(request, 'ta.html')
		else:
			return render(request, 'login.html')
	else:
		return render(request, 'login.html')

# def studenthome(request):
# 	return render(request, 'student.html')
#
#
# def facultyhome(requst):
# 	return render(requst, 'faculty.html')
#
#
# def adminhome(request):
# 	return render(request, 'admin.html')


def loginvalidate(requst):
	if requst.method == 'GET':
		return render(requst, 'login.html')

	if requst.method == 'POST':
		username = requst.POST['username']
		password = requst.POST['pass']
		# print('Username: ' + username + ", Password: " + password)
		try:
			# user = models.Login.objects.filter(username=username).filter(password=password)
			user = models.Login.objects.get(username=username)
			print(str(user.password) == password)
			if str(user.password) == password:
				print(user.role)
				requst.session['username'] = username
				requst.session['role'] = user.role
				requst.session['userId'] = user.userId
				return redirect('home')
			else:
				print('User not found')
				return redirect("/")
		except Exception as ex:
			print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
			return redirect("login")

	print('Global redirect..')
	return render(requst, 'login.html')


def handler404(request, exception, template_name="404.html"):
	response = render_to_response("404.html")
	response.status_code = 404
	return response


def createCourse(request):
	if request.session.is_empty():
		return redirect('login')

	if request.method == 'GET':
		return HttpResponse("invalid request")

	if request.method == 'POST':
		data = str(request.body).split("'")[1].split("&")
		courseID = data[0]
		courseName = data[1]
		courseDesc = data[2]
		courseInstr = data[3]

		# print(courseID+":"+courseName+":"+courseDesc+":"+courseInstr)
		# print(request.body)

		try:
			course = models.Course()
			course.courseID = courseID
			course.courseTitle = courseName
			course.courseDesc = courseDesc
			if courseInstr != 'None':
				faculty = models.Faculty.objects.get(facultyId=courseInstr)
				course.courseInstructor = faculty
			course.save()
			return HttpResponse("Course Created Successfully..")
		except Exception as ex:
			print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
			return HttpResponse("something went wrong.. Please try again")
	return HttpResponse("invalid request")


def createFaculty(request):
	if request.session.is_empty():
		return redirect('login')

	if request.method == 'GET':
		return HttpResponse("invalid request")

	if request.method == 'POST':
		data = str(request.body).split("'")[1].split("`")
		if len(data) != 7:
			return HttpResponse("Invalid Request")
		username = data[0]
		password = data[1]
		role = data[2]
		facultyId = data[3]
		facultyName = data[4]
		facultyDesig = data[5]
		areaOfInterest = data[6]
		print(data)
		faculty = models.Faculty()
		faculty.facultyId = facultyId
		faculty.facultyName = facultyName
		faculty.facultyDesignation = facultyDesig
		faculty.facultyAreaOfInterest = areaOfInterest

		login_ = models.Login()
		login_.username = username
		login_.password = password
		login_.role = role
		login_.userId = facultyId
		try:
			faculty.save()
			login_.save()
			return HttpResponse("Query Successful..")
		except Exception as ex:
			print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
			return HttpResponse("something went wrong.. Please try again")
	return HttpResponse("Invalid request..")


def createStudent(request):
	if request.session.is_empty():
		return redirect('login')

	if request.method == 'GET':
		return HttpResponse("invalid request")

	if request.method == 'POST':
		data = str(request.body).split("'")[1].split("`")
		if len(data) != 7:
			return HttpResponse("Invalid Request")
		username = data[0]
		password = data[1]
		role = data[2]
		studId = data[3]
		studentName = data[4]
		class_ = data[5]
		year = data[6]
		print(data)
		student = models.Student()
		student.studentRollNo = studId
		student.studentName = studentName
		student.studentClass = class_
		student.studentYear = year

		login_ = models.Login()
		login_.username = username
		login_.password = password
		login_.role = role
		login_.userId = studId
		try:
			student.save()
			login_.save()
			return HttpResponse("Query Successful..")
		except Exception as ex:
			print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
			return HttpResponse("something went wrong.. Please try again")
	return HttpResponse("Invalid request..")


def loadInstructor(request):
	if request.session.is_empty():
		redirect("login")
	qs = models.Faculty.objects.only("facultyId", "facultyName")
	data = ''
	for a in qs:
		data += a.facultyId + ":" + a.facultyName + ","
	print(data)
	return HttpResponse(data)


# Used by faculty ----------------------------------------------------------------
@csrf_exempt
def viewMyCourses(request):
	if request.session.is_empty():
		redirect("login")
	if request.session.has_key('userId'):
		try:
			courses = models.Course.objects.filter(courseInstructor=request.session['userId'])
			data = ''
			for course in courses:
				data += course.courseID + ":" + course.courseTitle + ","
			return HttpResponse(data)
		except Exception as ex:
			print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
			return HttpResponse("something went wrong.. Please try again")
	return HttpResponse("Invalid Request")


@csrf_exempt
def assignCourseToStudent(request):
	if request.session.is_empty():
		return redirect('login')

	if request.method == 'GET':
		return HttpResponse("Invalid Request")

	data = str(request.body).split("'")[1].split("`")
	try:
		print(data)
		student = models.Student.objects.get(studentRollNo=data[0])
		course = models.Course.objects.get(courseID=data[1])
		courseEnrollment = models.CourseEnrollment()
		courseEnrollment.courseId = course
		courseEnrollment.studentRollNo = student
		courseEnrollment.save()
		return HttpResponse("Details saved successfully..")
	except models.Student.DoesNotExist as ex:
		return HttpResponse("Student not found in the database")
	except Exception as ex:
		print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
		return HttpResponse("something went wrong.. Please try again")


@csrf_exempt
def assignTAToCourse(request):
	if request.session.is_empty():
		return redirect('login')

	if request.method == 'GET':
		return HttpResponse("Invalid Request")

	data = str(request.body).split("'")[1].split("`")
	try:
		print(data)
		student = models.Student.objects.get(studentRollNo=data[0])
		course = models.Course.objects.get(courseID=data[1])
		courseTA = models.CourseTA()
		courseTA.courseId = course
		courseTA.studentRollNo = student
		courseTA.save()
		login = models.Login.objects.get(userId=student.studentRollNo)
		login.role = 'ta'
		login.save()
		return HttpResponse("Details saved successfully..")
	except models.Student.DoesNotExist as ex:
		return HttpResponse("Student not found in the database")
	except Exception as ex:
		print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
		return HttpResponse("something went wrong.. Please try again")


@csrf_exempt
def viewStudents(request):
	if request.session.is_empty():
		return redirect('login')

	if request.method == 'GET':
		return HttpResponse("Invalid Request")

	# data = str(request.body).split("'")[1].split("`")
	try:
		students = models.Student.objects.all()
		data = ''
		for student in students:
			data += student.studentRollNo + ":" + student.studentName + ":"
			data += student.studentClass + ":" + str(student.studentYear) + ","
		print(data)
		return HttpResponse(data)
	except models.Student.DoesNotExist as ex:
		return HttpResponse("Student not found in the database")
	except Exception as ex:
		print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
		return HttpResponse("something went wrong.. Please try again")


@csrf_exempt
def viewFaculties(request):
	if request.session.is_empty():
		return redirect('login')

	if request.method == 'GET':
		return HttpResponse("Invalid Request")

	# data = str(request.body).split("'")[1].split("`")
	try:
		faculties = models.Faculty.objects.all()
		data = ''
		for faculty in faculties:
			data += faculty.facultyId + "`" + faculty.facultyName + "`"
			data += faculty.facultyDesignation + "`" + faculty.facultyAreaOfInterest + "~"
		print(data)
		return HttpResponse(data)
	except models.Student.DoesNotExist as ex:
		return HttpResponse("Student not found in the database")
	except Exception as ex:
		print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
		return HttpResponse("something went wrong.. Please try again")

@csrf_exempt
def viewAllCourses(request):
	if request.session.is_empty():
		redirect("login")
	if request.session.has_key('userId'):
		try:
			courses = models.Course.objects.all()
			data = ''
			for course in courses:
				data += course.courseID + "`" + course.courseTitle + "`"
				data += course.courseDesc + "`" + course.courseInstructor.facultyName + "~"

			return HttpResponse(data)
		except Exception as ex:
			print('Exception Occurred: ' + type(ex).__name__ + ":" + str(ex.args))
			return HttpResponse("something went wrong.. Please try again")
	return HttpResponse("Invalid Request")
