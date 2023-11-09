from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        format = toml.loads(content)
        return Project(format['tool']['poetry']['name']
                       ,format['tool']['poetry']['description']
                       ,format['tool']['poetry']['license']
                       ,format['tool']['poetry']['authors']
                       ,format['tool']['poetry']['dependencies']
                       ,format['tool']['poetry']['group']['dev']['dependencies']
                    )
