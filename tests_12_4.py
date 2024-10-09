import logging

import unittest



logging.basicConfig(level=logging.INFO, filename='runner_tests.log', encoding='utf-8',
                        filemode='w',format='%(asctime)s | %(levelname)s | %(message)s')

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers
class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            rnr = Runner('Kate', -5)
            for _ in range(10):
                rnr.walk()
            self.assertEqual(rnr.distance, 100)
            logging.info(f'test_walk выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner: %s', exc_info=True)


    def test_run(self):
        try:
            run_ = Runner(7)
            for _ in range(10):
                run_.run()
            self.assertEqual(run_.distance, 100)

            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning('Неверный тип данных для объекта Runner: %s',exc_info=True)




if __name__ == '__main__':
    unittest.main()

