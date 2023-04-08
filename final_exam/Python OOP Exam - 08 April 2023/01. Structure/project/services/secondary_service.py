from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name: str, capacity: int = 15):
        super().__init__(name, capacity)

    def details(self):
        if len(self.robots) == 0:
            result = f"{self.name} Secondary Service:" + "\n"
            result += "Robots: none"
            return result

        robots_name_list = [x.name for x in self.robots]
        result = f"{self.name} Secondary Service:" + "\n"
        result += f"Robots: {' '.join(robots_name_list)}"
        return result
