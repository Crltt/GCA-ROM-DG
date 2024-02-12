import numpy as np


def problem(argument):
    """
    problem(argument: int) -> Tuple[str, str, np.ndarray, np.ndarray]

    This function takes in an integer argument and returns a tuple containing the problem name (str), variable name (str), mu1 (np.ndarray) and mu2 (np.ndarray) for the specified case.

    The possible values of argument are:


    Returns:
    Tuple containing the problem name (str), variable name (str), mu1 (np.ndarray) and mu2 (np.ndarray) for the specified case.
    """

    match argument:
        case 14:
            problem_name = "maxwelldg"
            variable = 'TEz'
            mu1 = np.linspace(1, 130,130)
            mu_space = [mu1]
            n_param = 1
        case 15:
            problem_name = "maxwelldg0125"
            variable = 'TEz'
            mu1 = np.linspace(1, 335,335)
            mu_space = [mu1]
            n_param = 1
        case 16:
            problem_name = "maxwelldg0125"
            variable = 'THx'
            mu1 = np.linspace(1, 335,335)
            mu_space = [mu1]
            n_param = 1
        case 17:
            problem_name = "maxwelldg0125"
            variable = 'THy'
            mu1 = np.linspace(1, 335,335)
            mu_space = [mu1]
            n_param = 1    
        case 18:
            problem_name = "maxwelldg0125p2"
            variable = 'TEz'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1
        case 19:
            problem_name = "maxwelldg0125p2"
            variable = 'THx'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1
        case 20:
            problem_name = "maxwelldg0125p2"
            variable = 'THy'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1  
        case 21:
            problem_name = "maxwelldg0125p2hp"
            variable = 'TEz'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1
        case 22:
            problem_name = "maxwelldg0125p2hp"
            variable = 'THx'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1
        case 23:
            problem_name = "maxwelldg0125p2hp"
            variable = 'THy'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1  
        case 24:
            problem_name = "maxwelldg0125p1hp"
            variable = 'TEz'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1
        case 25:
            problem_name = "maxwelldg0125p1hp"
            variable = 'THx'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1
        case 26:
            problem_name = "maxwelldg0125p1hp"
            variable = 'THy'
            mu1 = np.linspace(1, 305,305)
            mu_space = [mu1]
            n_param = 1  
        case 27:
            problem_name = "maxwelldg00625p2hp"
            variable = 'TEz'
            mu1 = np.linspace(1, 130,130)
            mu_space = [mu1]
            n_param = 1
        case 28:
            problem_name = "maxwelldg00625p2hp"
            variable = 'THx'
            mu1 = np.linspace(1, 130,130)
            mu_space = [mu1]
            n_param = 1
        case 29:
            problem_name = "maxwelldg00625p2hp"
            variable = 'THy'
            mu1 = np.linspace(1, 130,130)
            mu_space = [mu1]
            n_param = 1  
    return problem_name, variable, mu_space, n_param
