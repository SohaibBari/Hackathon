from imports import *
from models.Pictures import Image
from models.Users import Users
from google.appengine.ext import ndb
from google.appengine.api import images
import jinja2
from datetime import date
from lib import pytz
from lib.pytz import timezone

PICTURE_PARENT_KEY = ndb.Key("Entity", "pictures_root")


class Helpers():
    CLASSROOM_STUDENT_KEY = ndb.Key("Entity", "classroom_student_key")

    def __init__(self):
        pass

    @staticmethod
    def string_to_boolean(string_value):
        if string_value == 'on' or string_value == 'true':
            return True
        else:
            return False

    def get_firebase_credentials(self, request):
        firebase_staging_environment_credentials = {
            "type": "service_account",
            "project_id": "kompassera-191815",
            "private_key_id": "7cbde704674ba6a47834d6184eb3e294c0a01efc",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQCvLv2vdgykoS5f\n4NKMmNVdXMpspqQfcArf1FKL0wJ31XriT882aiVaWbiW6x9YJX4Ync3T6UY/DBu0\nLY55bczYXqlkbJgXyXRgtrx4DedcYhkMbhn/ttUeSNNIjrZENqzshaZXppKASrAJ\nGDTRu+XvT3plc8MMkyvZhduBc2lBJPHSAy5NEdtbVC1oZl/QRXbz/7o1Yn9CDJNL\ngN0+WPPVxtWMc76Y1rThlC6GaH3ahjoqf27Nu5m5K42Z1IqosEhaUyeQ4hXqnazl\nyDsQh3cy69ur1dQ+hrwtt3KR90ZctAKYLTAxEV/kYmJza6RDM305g2ehBrfgHcUo\n0dbPk82ZAgMBAAECggEACPVuvMPdNqgVfoq5Sb5hHvKpWXAWMZNhwvuRMxxZ4nX0\n4FDziFVaTqoK8hDZHAFi1vBu/7jMwlmkqwyvXg9a6++/WubgykqfnHiL39naLJPJ\nsySISNb5RCC2SV4e/RMMudXF4XKfyFbJdNWbkeQ5iIj4eeq3HVQDaI7bYF3eEpoy\nzXlBumh12sdtSXp/vZEbqD31tr1XlFzLF+wn8GlIdyPCNkD6U6zFL79pZiFW6bPa\n+v5zVi6zOFZ6w9xvDY864sGbpZuHuG7L5cp3yQR9DwAY8bU2DWhw3R+WoncwU18d\nJ5j/T/GOGWXB+zSsIFuP2Azy6Xh+eH+B3fkPYxtIwQKBgQDp1pEWsbNCUOYxnpOZ\nycho+BV6xdPDS/oOcsQpXIxc9RODwjNOFtikKJgUxeY/L/YT7eGU61q2+WjrJFY3\nkKmnYU4bjP2v1bgz5U6411yvgwaPoQqcZV388W82kxn4ZNLqIuYVkvWpHpRsvYJk\n1Za5DaeCYc9tKz3JKF+6B8mHyQKBgQC/yVVbRTG9knKPwDcgABV2EXwHi70msRuJ\nG43Gg7c2GwCXy3WYrIffQ0Ucuk2wg1HOaDLjf5yMgktahIaeaKCVl7UUoU40DZm2\nhbK22lDZ+1nTGnqTRT4dGyxpNemUgQflfnhqolHKVJ1jl2JUKf+XZuGWxNF6EKbS\nTDlU8qqfUQKBgQCYZsCO8ufrC8DLjBeUvp9AUpflOXPHsAfcTM4uSuQsXYoHcJVx\nipBNhSuBNm3WttKBsKM6JJ4t7KWFw1vxwPXhYhi++ggJBpiUMho5fBsrRJENIR9C\nSQqVpWEfR4ZAjq2r7WzZmLtFKun/aQ/H2jDukMigwFCpTOpq5UZmf1bIiQKBgQCX\nDdpe0rcEmu4Ebt58I9TDc63+u381lFUdvkgCTQfmY4oqBKQQpgM2Q+ORZuN93VB3\ng/Zg3MfOm2kCWFM3PS0N5blIEGxp7zRcYB2Mi5MWvTPYY4ibqfPsNNTb4QyiXKZ9\niQkK4+ILvG1iXX+izplzBCM1/rsGq0rZZBPb5m2goQKBgC+H66Mx3l36ecmupS/h\nCVsQYj/ZaXQIQQeFBIOW+SH+piyrYILK+NHdpjovNVxdLxghwJw/Tw+uqoT+Btuy\nwlJIv2ouXZolvxs9yv5JmmYpYC7mVsui2fVaAdWqNUfKcvc5hf4FQcQXkkr41sFR\nlMYET8NC9sqgzA8nDw7bwfhg\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-70oiz@kompassera-191815.iam.gserviceaccount.com",
            "client_id": "112130120507812013246",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-70oiz%40kompassera-191815.iam.gserviceaccount.com"
        }
        firebase_dev_environment_credentials = {
            "type": "service_account",
            "project_id": "kompassera-dev-6e1af",
            "private_key_id": "ff94fb9a5cc335b77e9b86000f5df3fe86395e3c",
            "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCfvF23kG+baAz0\ndZn0/xo8CR4W3NopLIAnRzu4bgqX97Ov+uxwygWigtLu8nAoqMoWjGn1QLlTsfsp\nRINW+1imk621pSSxy0piVBGOnxrXNWamJnQgLCsyAETZbqworTNoIVgamxTDjy0x\nNJ3BFnIZuXz9VqNTmujfaslgSslti+WeALIg96E2ikuIecqBIp64ekiogAZPAR+S\nCW+FI4ePzhP7/Z+BHfYZ207rgncIF5tEFcE94U+ZXdaVmLjhdPMoe/TjOVaGeam3\nOEVGTQp3X4OwkcKJUoasrnzJYqJEqqwVQdoBjPzCS8B3NNnxs3g7/TI6z0l+fzqa\nPTGkKzbDAgMBAAECggEAD9eq6qFSVTUsXI4ekmKlhsD98UhYzmhoLD0cfbRTeNk4\ndfw3hhCehXMsAEa4SNGqYjK6V/iVSOlBxUjsk9LPt8AbpISrNbafyBr/0Meth4NE\nc1C+B+pv8E1MugBUswYWlddn+XknEow5POrNUjceyVFdxaYmaPM+V6ZFY1D98E82\n+zOUALtxakya342waRI4G4oBrqZtYRdxQEgBe+IdTLp1cHZfo2vSmxUrOf7dkbet\n1bg4za1V6mWaCSQkrxZ8ysuYoKxd/+9XBZe2rRGsAiSbGzRPdzHtN9VTOIiRPZEQ\nBu/O3517j+li/x5kXVUIjIjylKGaGGBOYxK0zJ/loQKBgQDZ/MoSN7Q/NLhRP1pR\n2L8M8YWbIvxuRI4Ya7PimDR/nnwKnqkJsB0JcvJHU8BKRO+JPvdrSZkhZgVOsjOq\nD+wNnlR5qPJ9As5h2GMkfRUe2IVpypY2I7r0oSHFt6VdYwjrPtd4qgQGIgAqs9Xa\nOBr4ANlsREmAgZSNl/lzOZcoIwKBgQC7lyfvDSs95KSSUHEzdaHNiLj+G/4m1Mk+\nk1yvPQUKR8vZNRoSEK/ma8lC3HBSak83nP1Xg5BYpxIb11HwdoxS7cmYDg0hthen\nomL6p2eCrI+3XzSqgrS4Dq/dQkMsBiZS/P705tT9VGnsUeINzOD4b5rcnT+xskcY\nPWfeeIJQ4QKBgAGo5hT7bZjpmtmrhNGIt/OuRxkmTAu+4+IVt9nq1MN//mvKR3k2\naRIwWN3oKlembLh7zUB43/ycHUA7JR+PXXnBEd2XRrli8xVVo3OcrDN+7I0gqMIi\nxYKlU2+A9XZfkarQ4K0fhkZRrfSlR+SQdswanY0we+rJkcr+ND0HXDpHAoGACmBF\nBDL9RlIkTDeI22jRR1YdrWiM+UbhzsVF5ieA5N2tx9jpFUC5CgzCOCGLUPOyaAgV\n90Y+sLilBsc1MBDOmDOw5+k3DrtMuagAw46I6jBzTphEiH3sUxX04k8s+f1pF0QJ\nMjCmbVDC/yBUWaEQfI1nynYkNMcAqbWTzjlqM+ECgYBnWcrMgWvhfv/G2foRt0av\nkUAmm4YcdVLpys+mUGzfBGwySo43OVG7tr+D/sQa9rAHte0/IZ6DvY2Crv8M1Q7q\n7iGGzuHjQi+akSDX5w/9ZK9rxJh2Dr+9sF1WJS5PGld47Uktp/0P+CkbMOqyhGDR\nW7vx6WntEHM5yNYVZnPK0Q==\n-----END PRIVATE KEY-----\n",
            "client_email": "firebase-adminsdk-2xvm6@kompassera-dev-6e1af.iam.gserviceaccount.com",
            "client_id": "108895032232450823320",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-2xvm6%40kompassera-dev-6e1af.iam.gserviceaccount.com"
        }

        firebase_staging_environment_database_url = {
            'databaseURL': 'https://kompassera-191815.firebaseio.com'
        }
        firebase_dev_environment_database_url = {
            'databaseURL': 'https://kompassera-dev-6e1af.firebaseio.com'
        }
        if request.host == "127.0.0.1:8080" or request.host == "localhost:8080":
            return firebase_dev_environment_credentials, firebase_dev_environment_database_url
        else:
            return firebase_staging_environment_credentials, firebase_staging_environment_database_url

    def get_firebase_js_credentials(self):
        firebase_staging_environment_credentials_js = {
            "apiKey": "AIzaSyCRAbwWGexRXsplcW4nX8RPqmVpBigJXkA",
            "authDomain": "kompassera-191815.firebaseapp.com",
            "databaseURL": "https://kompassera-191815.firebaseio.com",
            "projectId": "kompassera-191815",
            "storageBucket": "kompassera-191815.appspot.com",
            "messagingSenderId": "595460395838"
        }
        firebase_dev_environment_credentials_js = {
            "apiKey": "AIzaSyB0KBt9quXMxRU2PHEaLrbpIM-0qBDkl6I",
            "authDomain": "kompassera-dev-6e1af.firebaseapp.com",
            "databaseURL": "https://kompassera-dev-6e1af.firebaseio.com",
            "projectId": "kompassera-dev-6e1af",
            "storageBucket": "kompassera-dev-6e1af.appspot.com",
            "messagingSenderId": "711127520472"
        }
        if self.request.host == "127.0.0.1:8080" or self.request.host == "localhost:8080":
            return firebase_dev_environment_credentials_js
        else:
            return firebase_staging_environment_credentials_js

    def hash_password(self, password):
        salt = uuid.uuid4().hex
        return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt

    def check_user(self, email, Users):
        check = Users.query(Users.email == email).get()
        return check

    def get_user_profile_main_image(self, user_id, image_size='', default_image=None):
        user_image = Image.query(Image.reference_key == user_id).order(-Image.image_creation_date).get()
        if user_image:
            print user_image
            user_image.serving_url = images.get_serving_url(user_image.image_key)
            return user_image.serving_url + image_size
        else:
            return default_image

    def getProfilePictures(self, id):
        main_image = None
        image = None
        image = Image.query(ndb.AND(Image.reference_key == id, Image.active == True)).order(-Image.image_creation_date)
        image.fetch(limit=6)
        if image:
            for a in image:
                a.serving_url = images.get_serving_url(a.image_key) + "=s800-c"
                main_image = []
            for a in image:
                main_image.append(images.get_serving_url(a.image_key) + "=s800-c")
                main_image.append(a.image_key)
                break

        return image, main_image

    def get_main_picture(self, id):
        main_image = Image.query(ndb.AND(Image.reference_key == id,
                                         Image.active == True),
                                 ancestor=PICTURE_PARENT_KEY).get()
        if main_image:
            main_image = images.get_serving_url(main_image.image_key) + "=s150-c"

        return main_image

    def generate_slug(self, name, model):
        slug = re.sub('[^a-zA-Z0-9 \n\.]', '', name)
        slug = slug.replace(" ", "-").lower()
        # if model == "Users":
        count = 0
        slug_check = slug
        while model.query(model.slug == slug_check).get():
            count += 1
            print count
            # slug_check = slug
            slug_check = slug + str(count)
        # slug_check = model.query(model.slug == slug).get()
        # if model == "Listing":
        #     slug_check = Listing.query(Listing.slug == slug).get()

        # if slug_check:
        #     slug = slug + "1"
        return slug_check

    @staticmethod
    def get_user_object_from_user_id(user_id):
        return json.dumps(Users.query(Users.key == ndb.Key(urlsafe=user_id)).get(projection=[Users.slug,
                                                                                             Users.last_name,
                                                                                             Users.first_name,
                                                                                             Users.firebase_uid,
                                                                                             Users.email
                                                                                             ]).to_dict(), default=str)
        # user = Users.query(Users.key.urlsafe() == user_id).get()
        # user = Users.get_by_id(ndb.Key(urlsafe=user_id).id())
        # return ndb.Key(urlsafe=user_id).get().slug

    @staticmethod
    def check_dictionary(dictionary):
        if isinstance(dictionary, list):
            return True
        return False

    def set_timezone(self):
        if self.request.host == "127.0.0.1:8080" or self.request.host == "localhost:8080":
            timezone = "Asia/Karachi"
            return timezone
        else:
            county_code = self.request.headers['X-AppEngine-Country']
            timezone = pytz.country_timezones(county_code)
            return str(timezone[0])

    def get_timezone(self, date_time, user_timezone):
        user_tz = timezone(user_timezone)
        current = date_time.replace(tzinfo=pytz.utc).astimezone(user_tz)
        return current.strftime('%m/%d/%Y, %H:%M')
