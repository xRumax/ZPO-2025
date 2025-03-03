class Robot:
    def operate(self) -> str:
        return 'Performing task'
    

class AI:
    def think(self) -> str:
        return 'Processing data'
    

class Android(Robot, AI):
    def self_learn(self)->str:
        return "Loading data"


def main():
    robot = Robot()
    ai = AI()
    android = Android()

    print(robot.operate())
    print(ai.think())
    print(android.self_learn())

if __name__ == '__main__':
    main()