import maze
import pytest

@pytest.mark.parametrize('file, goalF',
                         [('maze1.txt',(0, 5)),
                          ('maze2.txt',(8, 13)),
                          ('maze3.txt',(2, 1)),
                          ('labe1.txt',(1, 2)),
                          ('labe2.txt',(11, 24))
                          ])
def test_maze(file, goalF):
    m = maze.Maze(file)
    m.solve
    assert m.goal == goalF
