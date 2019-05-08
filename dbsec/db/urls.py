from django.conf.urls import include, url
from . import views
from django.urls import path


urlpatterns = [
	path('home', views.home, name='home'),
	# path('student', views.studenthome),
	# path('faculty', views.facultyhome),
	# path('admin', views.adminhome),
	path('loginValidate', views.loginvalidate, name='loginValidate'),


	# Services:
	path('createCourse', views.createCourse, name='createCourse'),
	path('createStudent', views.createStudent, name='createStudent'),
	path('createFaculty', views.createFaculty, name='createFaculty'),
	path('loadInstructor', views.loadInstructor, name='loadInstructor'),
	path('viewMyCourses', views.viewMyCourses, name='viewMyCourses'),
	path('assignCourseToStudent', views.assignCourseToStudent, name='assignCourseToStudent'),
	path('assignTAToCourse', views.assignTAToCourse, name='assignTAToCourse'),
	path('viewStudents', views.viewStudents, name='viewStudents'),
	path('viewFaculties', views.viewFaculties, name='viewFaculties'),
	path('viewAllCourses', views.viewAllCourses, name='viewAllCourses'),

]
