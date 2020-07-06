from django.db import models

class Dictionary(models.Model):
    kind = models.CharField(max_length=10)  # 종 종류
    animal_name = models.CharField(max_length=50, help_text="이름을 작성해 주세요!")  # 동물 이름
    animal_en_name = models.CharField(max_length=50, help_text="영어 이름을 작성해 주세요!")  # 동물 영어 이름
    level = models.CharField(max_length=10, help_text="무슨과 인가요?")  # 과
    age = models.CharField(max_length=50, help_text="수명은?")  # 수명
    size = models.CharField(max_length=20, help_text="크기는?")  # 크기
    eat = models.CharField(max_length=20, help_text="뭘 먹나요?")  # 먹이
    live = models.CharField(max_length=20, help_text="어디 사나요?")  # 서식지
    description = models.TextField()  # 부연설명
    image_main = models.ImageField(blank=True, upload_to="dictionary/image_main/")  # 메인_이미지
    image = models.ImageField(blank=True, upload_to="dictionary/image/")  # 이미지

    def __str__(self):
        return "이름 : " + self.animal_name
