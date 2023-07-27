from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import QuestionSerializer

class QuestionAPI(APIView):
    def get(self, request):
        try:
            all_questions = Question.objects.all()
            questions = []

            if request.GET.get('filter'):
                filter = request.GET.get('filter')

                if filter == "read":
                    read_questions = ReadQuestion.objects.all()
                    [questions.append(ques) for ques in all_questions if ques not in read_questions]

                    # for ques in all_questions:
                    #     for q in read_questions:
                    #         if ques.id == q.question_id:
                    #             questions.append(ques)

                if filter == "unread":
                    read_questions = ReadQuestion.objects.all()
                    [questions.append(ques) for ques in all_questions if ques in read_questions]
                                       
                if filter == "favorite":
                    fav_questions = FavoriteQuestion.objects.all()
                    [questions.append(ques) for ques in all_questions if ques not in fav_questions]

                if filter == "unfavorite":
                    fav_questions = FavoriteQuestion.objects.all()
                    [questions.append(ques) for ques in all_questions if ques in fav_questions]
                    
            else:
                questions = all_questions
            serializer = QuestionSerializer(questions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({'msg': 'Something went wrong!', "error": e}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Question created successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
