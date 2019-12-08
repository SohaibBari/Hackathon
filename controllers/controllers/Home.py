from imports import *
from lib.firebase_admin import auth


# Bolt Reactor >> KompassEra >> Landing Handler Class
class LandingHandler(BaseHandler, Helpers):
    def get(self):
        template = self.jinja_environment.get_template("index.html")
        self.response.out.write(template.render({}))


class Help(BaseHandler):
    def get(self):
        template = self.jinja_environment.get_template("/help.html")
        self.response.out.write(template.render({}))


class Teach(BaseHandler):
    def get(self):
        template = self.jinja_environment.get_template("/teach.html")
        self.response.out.write(template.render({}))


class Dashboard(BaseHandler):
    @BaseHandler.checklogin
    def get(self):
        template = self.jinja_environment.get_template("/ke/dashboard/dashboard-home.html")
        self.response.out.write(template.render({}))


class ServeHandler(blobstore_handlers.BlobstoreDownloadHandler):
    def get(self, resource):
        resource = str(urllib.unquote(resource))
        blob_info = blobstore.BlobInfo.get(resource)
        self.send_blob(blob_info)


class DeleteAllFirebaseUsers(BaseHandler, Helpers):
    def get(self):
        all_users = Users.query()
        firebase_staging_environment_credentials, firebase_staging_environment_database_url = self.get_firebase_credentials(self.request)
        cred = credentials.Certificate(firebase_staging_environment_credentials)
        default_app = lib.firebase_admin.initialize_app(cred, firebase_staging_environment_database_url)

        for user in all_users:
            auth.delete_user(user.firebase_uid)


# Bolt Reactor >> KompassEra >> Usuability-Test Handler Classes
class NotFound(BaseHandler):
    def get(self):
        jinja_environment = self.jinja_environment
        template = jinja_environment.get_template("/ke/home/not-found.html")
        self.response.out.write(template.render({}))


class DeleteIndex(BaseHandler):
    def get(self):
        index = search.Index(name="listings")
        while True:
            # Use ids_only to get the list of document IDs in the index without
            # the overhead of getting the entire document.
            document_ids = [
                document.doc_id
                for document
                in index.get_range(ids_only=True)]

            # If no IDs were returned, we've deleted everything.
            if not document_ids:
                break

            # Delete the documents for the given IDs
            index.delete(document_ids)


class InProgress(BaseHandler, Helpers):
    def get(self):
        template = self.jinja_environment.get_template("ke/home/in-progress.html")
        self.response.out.write(template.render({}))
