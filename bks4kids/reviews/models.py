from django.db import models
from django.contrib import auth
# Create your models here.
class Publisher(models.Model):
    """This is a company that publishes Children books"""
    # The backslash indicates that the following code is on the same line
    name = models.CharField \
        (max_length=50, \
         help_text = "The name of the publisher")
    city = models.CharField \
        (max_length = 25, \
         help_text = "The city where the publisher is located")
    website = models.URLField(help_text="The publisher's website")
    email = models.EmailField(help_text="The publisher's email address")
    def __str__(self):
        return self.name

class Creator(models.Model):
    """An author to a children's book"""
    first_names = models.CharField(max_length=50, \
                                   help_text="The author's first name or names")
    last_names = models.CharField(max_length=50, \
                                  help_text = "The author's last name or names")

# class Author(models.Model):
#     """An author to a children's book"""
#     first_names = models.CharField(max_length=50,\
#                                    help_text="The author's first name or names.")
#     last_names = models.CharField(max_length=50,\
#                                   help_text="The author's last name or names")
#     email = models.EmailField(help_text="The contact email for the author")
#     def __str__(self):
#         return self.first_names

class Book(models.Model):
    """A published children's book"""
    class AgeRange(models.TextChoices):
        SEVEN_PLUS = "SEVEN_PLUS" , "7+"
        EIGHT_PLUS = "EIGHT_PLUS" , "8+"
        NINE_PLUS = "NINE_PLUS" , "9+"
        TEN_PLUS = "TEN_PLUS" , "10+"
        ELEVEN_PLUS = "ELEVEN_PLUS" , "11+"
        TWELVE_PLUS = "TWELVE_PLUS" , "12+"
        ELEVEN_TWELVE = "ELEVEN_TWELVE" , "11-12"
        ELEVEN_FOURTEEN = "ELEVEN_FOURTEEN" , "11-14"
        THIRTEEN = "THIRTEEN" , "13"
        THIRTEEN_PLUS = "THIRTEEN_PLUS" , "13+"
        THIRTEEN_FIFTEEN = "THIRTEEN_FIFTEEN" , "13-15"
        THIRTEEN_EIGHTEEN = "THIRTEEN_EIGHTEEN" , "13-18"
        FOURTEEN_PLUS = "FOURTEEN_PLUS" , "14+"
    title = models.CharField \
        (max_length = 70, \
         help_text = "The title of the book.")
    isbn = models.CharField \
        (max_length = 20, \
         verbose_name = "ISBN number of the book")
    interest_age = models.CharField(verbose_name = "The interested readers' age", \
                        choices = AgeRange.choices, max_length = 20)
    reading_age = models.CharField(verbose_name = "The targeted readers' age", \
                        choices = AgeRange.choices, max_length = 20)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    creator = models.ManyToManyField('Creator', through="BookCreator")
    def __str__(self):
        return self.title

class BookCreator(models.Model):
    class CreatorRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        ILLUSTRATOR = "ILLUSTRATOR", "Illustrator"

    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this creator had in the book", \
                            choices=CreatorRole.choices, max_length=20)

class Review(models.Model):
    """Reviews for the different books"""
    content = models.TextField(help_text = "The Review text for the children book")
    rating = models.IntegerField(help_text = "The rating the reviewer has given.")
    date_created = models.DateTimeField(auto_now_add = True, \
                                        help_text = "The date and time the review was created")
    date_edited = models.DateTimeField(null=True,\
                                       help_text = "The date and time the review was last edited")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE,\
                             help_text = "The Children Book that this review is for")