from rest_framework.response import Response
from rest_framework import status, generics

class ResponseEntity():    
    #     추가 이유
    #     1) 추후에 Response에 공통적으로 변경할 사항이 있으면 이곳만 변경하면 됨
    #     2) 코드 작성 시 더 간략해게 작성 가능
    #     3) 제3자가 코드 분석 시 가독성 올라감    

    @classmethod
    def ok(cls, data, code=200):
        return Response(data, status=code)

    @classmethod
    def bad(cls, msg, code=400):
        return Response(msg, status=code, exception=True)

        