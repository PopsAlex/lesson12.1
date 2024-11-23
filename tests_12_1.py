import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name


class RunnerTest(unittest.TestCase):

    def test_walk(self):
        runner = Runner('Proisvol')
        for i in range(1, 11):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        runner = Runner('snova_Proizvol')
        for i in range(1, 11):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        runner = Runner('Proizvol1')
        walker = Runner('Proizvol2')
        for i in range(1, 11):
            runner.run()
            walker.walk()
        self.assertNotEqual(runner.distance, walker.distance)


runner_case = RunnerTest()