# Naruszona zasada ISP

from abc import ABC, abstractmethod

class IWorkable(ABC):
    @abstractmethod
    def work(self):
        pass

class IEatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class HumanWorker(IWorkable, IEatable):
    def work(self):
        print("Human worker working")

    def eat(self):
        print("Human worker eating")

class RobotWorker(IWorkable):
    def work(self):
        print("Robot worker working")

# Użycie
human = HumanWorker()
robot = RobotWorker()

human.eat()  # Działa
robot.work()  # Działa
# robot.eat()  # Teraz robot nawet nie ma tej metody, więc błąd nie wystąpi!