from django.contrib import admin
from school.models import Student, Course, Enrollment

class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'document', 'email', 'birth_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'level')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20

class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'course', 'date', 'period')
    list_display_links = ('id', 'student')
    search_fields = ('student__name',)
    list_per_page = 20

admin.site.register(Student, StudentAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)