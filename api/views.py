from Users.models import *
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *


class Users(APIView):
    """
    API View for retrieving user information.

    Endpoint:
        GET api/users/: Retrieve a list of all users or a specific user by email or ID.

    Parameters:
        get_by (str): Optional. If provided, retrieves a specific user by email or ID.

    Returns:
        JSON Response: A serialized list of user information in the response body.
    """

    def get(self, request, get_by=None):
        """
        Handle GET requests for retrieving user information.

        Parameters:
            request (Request): The HTTP request object.
            get_by (str): Optional. If provided, retrieves a specific user by email or ID.

        Returns:
            Response: A JSON response containing serialized user information.
        """

        if get_by:
            users = CustomUser.objects.filter(Q(email__iexact=get_by) | Q(id__iexact=get_by))

        else:
            users = CustomUser.objects.all()

        serialized_user = UserSerializers(users, many=True)
        return Response(serialized_user.data)


class Exam(APIView):
    """
    API View for retrieving exam information.

    Endpoint:
        GET api/exams/: Retrieve a list of all exams or a specific exam by ID, Programme Name, or User Email.

    Parameters:
        get_by (str): Optional. If provided, retrieves a specific exam by ID, Programme Name, or User Email.

    Returns:
        JSON Response: A serialized list of exam information in the response body.
    """

    def get(self, request, get_by=None):
        """
        Handle GET requests for retrieving exam information.

        Parameters:
            request (Request): The HTTP request object.
            get_by (str): Optional. If provided, retrieves a specific exam by ID, Programme Name, or User Email.

        Returns:
            Response: A JSON response containing serialized exam information.
        """

        if get_by:
            exams = Exams.objects.filter(Q(ID__iexact=get_by) | Q(ProgrammeName__iexact=get_by) | Q(UserID__email__iexact=get_by))

        else:
            exams = Exams.objects.all()

        serialized_exams = ExamSerializers(exams, many=True)
        return Response(serialized_exams.data)


class Programmes(APIView):
    """
    API View for retrieving programme information.

    Endpoint:
        GET /programmes/: Retrieve a list of all programmes or a specific programme by ID or Name.

    Parameters:
        get_by (str): Optional. If provided, retrieves a specific programme by ID or Name.

    Returns:
        JSON Response: A serialized list of programme information in the response body.
    """

    def get(self, request, get_by=None):
        """
        Handle GET requests for retrieving programme information.

        Parameters:
            request (Request): The HTTP request object.
            get_by (str): Optional. If provided, retrieves a specific programme by ID or Name.

        Returns:
            Response: A JSON response containing serialized programme information.
        """

        if get_by:
            programmes = Programme.objects.filter(Q(ID__iexact=get_by) | Q(Name__iexact=get_by))

        else:
            programmes = Programme.objects.all()

        serialized_programmes = ProgrammeSerializers(programmes, many=True)
        return Response(serialized_programmes.data)


class Subjects(APIView):
    """
    API View for retrieving subject information.

    Endpoint:
        GET api/subjects/: Retrieve a list of all subjects or a specific subject by ID, Program Name, or Subject Name.

    Parameters:
        get_by (str): Optional. If provided, retrieves a specific subject by ID, Program Name, or Subject Name.

    Returns:
        JSON Response: A serialized list of subject information in the response body.
    """

    def get(self, request, get_by=None):
        """
        Handle GET requests for retrieving subject information.

        Parameters:
            request (Request): The HTTP request object.
            get_by (str): Optional. If provided, retrieves a specific subject by ID, Program Name, or Subject Name.

        Returns:
            Response: A JSON response containing serialized subject information.
        """

        if get_by:
            subjects = Subject.objects.filter(Q(ID__iexact=get_by) | Q(ProgrammeID__Name__iexact=get_by) | Q(Name__iexact=get_by))

        else:
            subjects = Subject.objects.all()

        serialized_subjects = SubjectSerializers(subjects, many=True)
        return Response(serialized_subjects.data)


class Question(APIView):
    """
    API View for retrieving question information.

    Endpoint:
        GET api/questions/: Retrieve a list of all questions or specific questions by ID, SubjectID, Subject Name, or Title.

    Parameters:
        get_by (str): Optional. If provided, retrieves specific questions by ID, SubjectID, Subject Name, or Title.

    Returns:
        JSON Response: A serialized list of question information in the response body.
    """

    def get(self, request, get_by=None):
        """
        Handle GET requests for retrieving question information.

        Parameters:
        - request (Request): The HTTP request object.
        - get_by (str): Optional. If provided, retrieves specific questions by ID, SubjectID, Subject Name, or Title.

        Returns:
        - Response: A JSON response containing serialized question information.
        """

        if get_by:
            questions = Questions.objects.filter(Q(ID__iexact=get_by) | Q(SubjectID__Name__iexact=get_by) | Q(SubjectID__ProgrammeID__Name__iexact=get_by) | Q(Title__iexact=get_by))

        else:
            questions = Questions.objects.all()

        serialized_questions = QuestionSerializers(questions, many=True)
        return Response(serialized_questions.data)


class Reports(APIView):
    """
    API View for retrieving reports information.

    Endpoint:
        GET api/reports/: Retrieve a list of all reports or a specific report by ID.

    Parameters:
        get_by (str): Optional. If provided, retrieves a specific report by ID.

    Returns:
        JSON Response: A serialized list of report information in the response body.
    """

    def get(self, request, get_by=None):
        """
        Handle GET requests for retrieving report information.

        Parameters:
            request (Request): The HTTP request object.
            get_by (str): Optional. If provided, retrieves a specific report by ID.

        Returns:
            Response: A JSON response containing serialized report information.
        """

        if get_by:
            reports = ReportQuestion.objects.filter(Q(ID__iexact=get_by) | Q(UserID__email__iexact=get_by) | Q(QuestionID__ID__iexact=get_by) | Q(QuestionID__Title__iexact=get_by))

        else:
            reports = ReportQuestion.objects.all()

        serialized_reports = ReportSerializers(reports, many=True)
        return Response(serialized_reports.data)


class Feedbacks(APIView):
    """
    API View for retrieving feedback information.

    Endpoint:
        GET api/feedbacks/: Retrieve a list of all feedbacks.

    Parameters:
        request (Request): The HTTP request object.

    Returns:
        JSON Response: A serialized list of feedback information in the response body.
    """

    def get(self, request):
        """
        Handle GET requests for retrieving feedback information.

        Parameters:
            request (Request): The HTTP request object.

        Returns:
            Response: A JSON response containing serialized feedback information.
        """

        feedbacks = FeedBack.objects.all()

        serialized_feedbacks = FeedbackSerializers(feedbacks, many=True)
        return Response(serialized_feedbacks.data)


class Histories(APIView):
    """
    API View for retrieving history information.

    Endpoint:
    - GET api/histories/: Retrieve history information based on the specified criteria.

    Parameters:
        request (Request): The HTTP request object.
        get_by (str): The criteria for retrieving history information.

    Returns:
        Response: A JSON response containing serialized history information.
    """

    def get(self, request, get_by):
        """
        Handle GET requests for retrieving history information.

        Parameters:
            request (Request): The HTTP request object.
            get_by (str): The criteria for retrieving history information.

        Returns:
            Response: A JSON response containing serialized history information.
        """

        histories = Exams.objects.filter(Q(UserID__id__iexact=get_by) | Q(UserID__email__iexact=get_by))

        serialized_histories = HistorySerializers(histories, many=True)

        return Response(serialized_histories.data)
