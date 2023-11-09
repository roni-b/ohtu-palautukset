class Project:
    def __init__(self, name, description, licence, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.licence = licence
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_method(self, data):
        all = ""
        for a in data:
            all += f"\n- {str(a)}"
        return all + "\n"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicence: {self.licence}\n"
            f"\nAuthors: {self._stringify_method(self.authors)}"
            f"\nDependencies: {self._stringify_method(self.dependencies)}"
            f"\nDevelopment dependencies: {self._stringify_method(self.dev_dependencies)}"
        )
