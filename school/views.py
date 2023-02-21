from rest_framework import viewsets, generics
from school.models import Student, Course, Enrollment
from school.serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, ListEnrollmentSerializer, ListStudentsEnrolledInACourseSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows users to be viewed or edited."""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CourseViewSet(viewsets.ModelViewSet):
    """API endpoint that allows courses to be viewed or edited."""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class EnrollmentViewSet(viewsets.ModelViewSet):
    """API endpoint that allows enrollments to be viewed or edited."""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListEnrollmentViewSet(generics.ListAPIView):
    """API endpoint that lists enrollments from a student."""
    serializer_class = ListEnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(student_id=self.kwargs['pk'])

class ListStudentsEnrolledInACourseViewSet(generics.ListAPIView):
    """API endpoint that lists students enrolled in a course."""
    serializer_class = ListStudentsEnrolledInACourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Enrollment.objects.filter(course_id=self.kwargs['pk'])
