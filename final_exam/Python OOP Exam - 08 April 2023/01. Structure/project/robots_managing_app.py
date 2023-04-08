from typing import List

from project.robots.base_robot import BaseRobot
from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.base_service import BaseService
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_SERVICE_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_ROBOT_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: List[BaseRobot] = []
        self.services: List[BaseService] = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_SERVICE_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.VALID_SERVICE_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_ROBOT_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.VALID_ROBOT_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        # Both robot and service with the given names will always exist.
        robot = next(filter(lambda x: x.name == robot_name, self.robots))
        service = next(filter(lambda x: x.name == service_name, self.services))

        if robot.__class__.__name__ == "MaleRobot":
            if service.__class__.__name__ != "MainService":
                return "Unsuitable service."

        elif robot.__class__.__name__ == "FemaleRobot":
            if service.__class__.__name__ != "SecondaryService":
                return "Unsuitable service."

        if robot.__class__.__name__ == "MaleRobot":
            if service.__class__.__name__ == "MainService":
                if service.capacity <= len(service.robots):
                    raise Exception("Not enough capacity for this robot!")
                else:
                    service.robots.append(robot)
                    self.robots.remove(robot)
                    return f"Successfully added {robot_name} to {service_name}."

        elif robot.__class__.__name__ == "FemaleRobot":
            if service.__class__.__name__ == "SecondaryService":
                if service.capacity <= len(service.robots):
                    raise Exception("Not enough capacity for this robot!")
                else:
                    service.robots.append(robot)
                    self.robots.remove(robot)
                    return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        # The service with the given name will always exist.
        service = next(filter(lambda x: x.name == service_name, self.services))

        robot_exist = False
        for robot in service.robots:
            if robot.name == robot_name:
                robot_exist = True
        if not robot_exist:
            raise Exception("No such robot in this service!")

        robot = next(filter(lambda x: x.name == robot_name, service.robots))

        self.robots.append(robot)
        service.robots.remove(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        # The service with the given name will always exist.
        service = next(filter(lambda x: x.name == service_name, self.services))

        for robot in service.robots:
            robot.eating()

        return f"Robots fed: {len(service.robots)}."

    def service_price(self, service_name: str):
        # The service with the given name will always exist.
        service = next(filter(lambda x: x.name == service_name, self.services))

        total_price = 0
        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ""
        for service in self.services:
            result += service.details() + "\n"
        return result[:-1]
