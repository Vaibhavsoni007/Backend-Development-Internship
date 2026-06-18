import os
from werkzeug.utils import secure_filename


class StorageService:

    @staticmethod

    @staticmethod
    def get_storage_type(config):

        return config["STORAGE_TYPE"]
    
    def save_file(file, upload_folder):

        filename = secure_filename(file.filename)

        filepath = os.path.join(
            upload_folder,
            filename
        )

        file.save(filepath)

        return filename, filepath


    @staticmethod
    def delete_file(filepath):

        if os.path.exists(filepath):
            os.remove(filepath)
            return True

        return False


    @staticmethod
    def file_exists(filepath):

        return os.path.exists(filepath)
    
    