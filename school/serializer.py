from rest_framework import serializers
from school.models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'document', 'email', 'birth_date']

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'code', 'description', 'name', 'level']

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'student', 'course', 'date', 'period']

class ListEnrollmentSerializer(serializers.ModelSerializer):
    course =  serializers.ReadOnlyField(source='course.name')
    period = serializers.ReadOnlyField(source='get_period_display')
    class Meta:
        model = Enrollment
        fields = ['course', 'period']

class ListStudentsEnrolledInACourseSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source='student.name')
    period = serializers.ReadOnlyField(source='get_period_display')
    class Meta:
        model = Enrollment
        fields = ['student_name', 'period']