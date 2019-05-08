from django.db import models
from django.utils import timezone


class Student(models.Model):
    studentRollNo = models.CharField(max_length=10, primary_key=True)
    studentName = models.CharField(max_length=60)
    studentClass = models.CharField(max_length=10)
    studentYear = models.SmallIntegerField()
    studentSem = models.CharField(max_length=4)

    def __str__(self):
        return self.studentFName

    class Meta:
        db_table = 'student'


class Faculty(models.Model):
    facultyId = models.CharField(max_length=20, primary_key=True)
    facultyName = models.CharField(max_length=50)
    facultyDesignation = models.CharField(max_length=50)
    facultyAreaOfInterest = models.TextField(max_length=1000, null=True)

    class Meta:
        db_table = 'faculty'

    def __str__(self):
        return self.facultyId


class Login(models.Model):
    username = models.CharField(unique=True, max_length=30)
    password = models.CharField(max_length=40)
    role = models.CharField(max_length=10)
    userId = models.CharField(primary_key=True, max_length=30)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'login'

    def __str__(self):
        return self.role


class Course(models.Model):
    courseID = models.CharField(max_length=10, primary_key=True)
    courseTitle = models.CharField(max_length=200)
    courseDesc = models.TextField()
    createAt = models.DateTimeField(default=timezone.now, blank=True)
    courseInstructor = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.courseID + " : " + self.courseTitle

    class Meta:
        db_table = 'courses'


class CourseEnrollment(models.Model):
    studentRollNo = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    courseId = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'courseEnrollment'
        unique_together = (("studentRollNo", "courseId"),)


class Grades(models.Model):
    studentRollNo = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    courseId = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    labNumber = models.CharField(max_length=20)
    marksObtained = models.FloatField()
    maxMarks = models.FloatField()

    class Meta:
        unique_together = (("studentRollNo", "courseId", "labNumber"),)
        db_table = "grades"


class CourseTA(models.Model):
    studentRollNo = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    courseId = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = (("studentRollNo", "courseId"),)
        db_table = 'courseTA'
