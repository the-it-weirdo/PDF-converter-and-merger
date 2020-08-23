import os, tempfile


class FileManager:

    def list_files(self, path: str, format: str):
        try:
            return {f: os.path.join(path, f) for f in os.listdir(path) if f.endswith(format)}
        except Exception as e:
            print(f"Error occurred: {e}")


    def is_path_writable(self, path:str):

        dirname = os.path.dirname(path) or os.getcwd()

        try:
            with tempfile.TemporaryFile(dir=dirname): pass
            return True

        except EnvironmentError:
            return False

    def is_path_exists(self, path):
        return os.path.exists(path)

    # def write(self, outpath):
    #     if not self.is_path_exists(outpath):
    #         pass