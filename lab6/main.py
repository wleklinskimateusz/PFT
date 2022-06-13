import os
from solver import Solver


def main():
    solver = Solver()
    if not os.path.exists('potential.npy'):
        solver.solve()
        solver.save_to_file()
    else:
        solver.load_from_file()
    

    


if __name__ == "__main__":
    main()