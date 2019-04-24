from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import DatabaseError
from .models import Dog
from django.views.decorators.csrf import csrf_exempt

import json

# Standard error messages that may be re-used many times. Shortens your code and
# makes them easy to update.
JSONDecodeFailMessage = "Error decoding JSON body. Please ensure your JSON file is valid."
BadRequestMessage = "Bad request."
DatabaseErrorMessage = "Error interacting with database."

@csrf_exempt # Exempt because it is not going through browser
def makeDog(request):
    if request.method == "POST":
        # Try to get the data from the POST body
        try: # Decode post body into JSON
            data = json.loads(request.body.decode("utf-8"))
        except json.JSONDecodeError: # If JSON failed to decode
            return HttpResponse(JSONDecodeFailMessage, status=400)
        # Handling other exceptions:
        # *****BAD:***** Gives too much info to the user, tells them too much about the system. Useful for debugging!
        # except Exception as e: # Any other exception
        #     return HttpResponse(str(e), status=400)
        # *****GOOD:*****
        except Exception: # Any other exception
            return HttpResponse(BadRequestMessage, status=400)
    else:
         return HttpResponse("Method not allowed.", status=405)

    try: # Add dog to DB
        newDoggo = Dog(name=data['name'], description=data['description'], breed=data['breed'])
        # Save the new row to the database
        newDoggo.save()
    except DatabaseError: # If database throws an error
        return HttpResponse(DatabaseErrorMessage, status=400)

    # JSON is all in dictionary format. By putting data into a dictionary,
    # django can easily encode it for you.
    # Notice how you can now access an ID!
    dogDict = { 'id': newDoggo.id, 'dogName': newDoggo.name, 'breed': newDoggo.breed}

    return JsonResponse(dogDict, safe=False, status=201)

    