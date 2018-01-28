from Recruiter.models.models import Question
import django_filters


class QuestionFilter(django_filters.FilterSet):
    #username = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Question
        fields = ['category_type', 'author']