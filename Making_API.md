# How to make an API?

This documentation will show how to make an API for a database. I follow these steps, I suggest we all follow the procedure for the sake of uniformity and if you think something is wrong in this documentation, edit it accordingly.

## So the process contains 3 steps
   * Installing django rest framework - This will make things a bit easier
   * Making serializers.py
   * Making api.py
   * Final changes in the configuration

**1.) Installing DRF :**
   Go virtual environment where you have your Django project and open a terminal/cmd prompt (I mean whatever guys..)
   and type:
```
pip insall djangorestframework markdown django-filter
```
    this will install **DRF** in your environment. **Markdown** and **Django-filter** will used for markdown and filtering support.

**2.) Making Serializers.py :**
   * Go to the directory where you have your *models.py* and make new python file named **serializers.py**
   * Suppose our target model name is *Profile* and has fields:
        * id
        * user
        * first_name etc.
        then the content of *serializers.py* will look like:

```python
from models import Profile
from rest_framework import serializers

class profile_serializer(serializers.ModelSerializer):
class Meta:
    model = Profile
    # fields will be a group of variables we want to extract details of
    fields = (
    'id',
    'user',
    'first_name'
    )
```
         
That is it for the *serializers.py*.

**3.) Making api.py :**
   * In the same directory where you made the *serializers.py* make a new file **api.py**
   * So it will look something like:

```python
from models import Profile
from serializers import profile_serializer
# this one is optional
from django.http import Http404

from rest_framework import APIView
from rest_framework.response import Response

class profile_list(APIView):

  def get(self, request, format=None):
      """You can change the format to json here"""
      profiles = Profile.objects.all()
      serialized_profiles = profile_serializer(profiles, many=True)
      return Response(serialized_profiles.data)

""" this class can be a bit different depending on the task you wanna perform """
class profile_detail(APIView):

  def get_object(self, pk):
      try:
          return Profile.objects.get(pk=pk)
      except Profile.DoesNotExist:
          raise Http404


  def get(self, request, pk, format=None):
      """You can change the format to json here"""
      profile = self.get_object(pk)
      serialized_profile = profile_serializer(profile)
      return Response(serialized_profile.data)
```
    And we are done with the *api.py*

**4.) Final configurations :**
   * Go to *settings.py* and add ```rest_framework``` in ```INSTALLED_APPS```
   * Go to *urls.py* and add the two lines:

```python
from rest_framework.urlpatterns import format_suffix_patterns
# Here profile is the folder name
from profile import api

# Add the required urls
urlpatterns = (

# Previous urls ^

# API part
url(r'^api/profiles', api.profile_list.as_view()),
url(r'^api/profiles/(?P<pk>[0-9]+)/$', api.profile_detail.as_view()),
#                   (^^^^^^^^^^^^^^^)
# The weird part is just a regex to match for primary key (id in this case) values
# You can see more about regex at [re](https://docs.python.org/2/library/re.html)
)

urlpatterns = format_suffix_patterns(urlpatterns)
```


So that is what you need to do to create a *simple, sweet, your own* API
I'll add somethings furthur if required and if you find something erroeous, we shall discuss it.
