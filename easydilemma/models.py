from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class DilemmaModel(models.Model):
#     dilemma_part_one = models.CharField(max_length=500)
#     dilemma_part_two = models.CharField(max_length=500)
    
class DilemmaPartOne(models.Model):
    dilemma_part_one = models.CharField(max_length=500)

    def __str__(self):
        return self.dilemma_part_one[:50]

class ReasonPartOne(models.Model):
    # Asscccoiate a reason to a dilemma
    dilemma = models.ForeignKey(DilemmaPartOne, default=None, related_name="reason_part_one", on_delete=models.CASCADE)

    reason = models.TextField()

    selected_option = models.CharField(max_length=50)

    def __str__(self):
        return self.reason[:50]


class DilemmaPartTwo(models.Model):
    dilemma_part_two = models.CharField(max_length=500)

    def __str__(self):
        return self.dilemma_part_two[:50]

class ReasonPartTwo(models.Model):
    # Asscccoiate a reason to a dilemma
    dilemma = models.ForeignKey(DilemmaPartTwo, default=None, related_name="reason_part_two" , on_delete=models.CASCADE)
    
    reason = models.TextField()

    selected_option = models.CharField(max_length=50)

    def __str__(self):
        return self.reason[:50]



class Dilemma(models.Model):
    dilemma_part_one = models.ForeignKey(DilemmaPartOne, on_delete=models.CASCADE)
    dilemma_part_two = models.ForeignKey(DilemmaPartTwo, on_delete=models.CASCADE)
    result = models.TextField()
    user = models.ForeignKey(User, null=True, blank=True, default = None, on_delete=models.CASCADE)
    should_post = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.dilemma_part_two}... Or {self.dilemma_part_two}..."
    
    # def get_part_one(self):
    #     return dilemma_part_one.dilemma_part_one

# class Reason(models.Model):
#     dilemma = models.ForeignKey(Dilemma, default=None, on_delete=models.CASCADE)
#     reason = models.TextField()

#     selected_option = models.CharField(max_length=50)

#     def __str__(self):
#         return self.reason[:50]
