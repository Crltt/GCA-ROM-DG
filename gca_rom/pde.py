import numpy as np


def problem(argument):
    """
    problem(argument: int) -> Tuple[str, str, np.ndarray, np.ndarray]

    This function takes in an integer argument and returns a tuple containing the problem name (str), variable name (str), mu1 (np.ndarray) and mu2 (np.ndarray) for the specified case.

    The possible values of argument are:

    Poisson problem
    Advection problem
    Graetz problem
    Navier-Stokes problem (variable = VX)
    Navier-Stokes problem (variable = VY)
    Navier-Stokes problem (variable = P)
    Diffusion problem
    Poiseuille problem
    Linear elasticity problem
    Returns:
    Tuple containing the problem name (str), variable name (str), mu1 (np.ndarray) and mu2 (np.ndarray) for the specified case.
    """

    match argument:
        case 1:
            problem_name = "maxwell"
            variable = 'TEz'
            mu1 = np.linspace(0, 335,336)
            mu_space = [mu1]
            n_param = 1
        case 2:
            problem_name = "maxwell"
            variable = 'THx'
            mu1 = np.linspace(0, 335,336)
            mu_space = [mu1]
            n_param = 1
        case 3:
            problem_name = "maxwell"
            variable = 'THy'
            mu1 = np.linspace(0, 335,336)
            mu_space = [mu1]
            n_param = 1
        case 4:
            problem_name = "maxwellmodes"
            variable = 'TEz'
            mu1 = np.linspace(0, 335,336)
            mu_space = [mu1]
            n_param = 1
        case 5:
            problem_name = "maxwellmodes"
            variable = 'THx'
            mu1 = np.linspace(0, 335,336)
            mu_space = [mu1]
            n_param = 1
        case 6:
            problem_name = "maxwellmodes"
            variable = 'THy'
            mu1 = np.linspace(0, 335,336)
            mu_space = [mu1]
            n_param = 1
        case 7:
            problem_name = "maxwellhp"
            variable = 'TEz'
            mu1 = np.linspace(1, 269,269)
            mu_space = [mu1]
            n_param = 1
        case 8:
            problem_name = "maxwellhp"
            variable = 'THx'
            mu1 = np.linspace(1, 269,269)
            mu_space = [mu1]
            n_param = 1
        case 9:
            problem_name = "maxwellhp"
            variable = 'THy'
            mu1 = np.linspace(1, 269,269)
            mu_space = [mu1]
            n_param = 1
        case 30:
            problem_name = "maxwelldgparamAVG"
            variable = 'TEz'
            mu1 = np.linspace(1.25, 3.5,10)
            mu2 = np.linspace(12*0.0016, 610*0.0016,100)
            mu_space = [mu1, mu2]
            n_param = 2
        case 31:
            problem_name = "maxwelldgparamAVG"
            variable = 'THx'
            mu1 = np.linspace(1.25, 3.5,10)
            mu2 = np.linspace(12*0.0016, 610*0.0016,100)
            mu_space = [mu1, mu2]
            n_param = 2
        case 32:
            problem_name = "maxwelldgparamAVG"
            variable = 'THy'
            mu1 = np.linspace(1.25, 3.5,10)
            mu2 = np.linspace(12*0.0016, 610*0.0016,100)
            mu_space = [mu1, mu2]
            n_param = 2 
        case 34:
            problem_name = "maxwelldgparam1"
            variable = 'TEz'
            mu1 = np.linspace(2.25, 3.5,5)
            mu2 = np.linspace(12*0.0016, 610*0.0016,100)
            mu_space = [mu1, mu2]
            n_param = 2
        case 35:
            problem_name = "maxwelldgparam1"
            variable = 'THx'
            mu1 = np.linspace(2.25, 3.5,5)
            mu2 = np.linspace(12*0.0016, 610*0.0016,100)
            mu_space = [mu1, mu2]
            n_param = 2
        case 36:
            problem_name = "maxwelldgparam1"
            variable = 'THy'
            mu1 = np.linspace(2.25, 3.5,5)
            mu2 = np.linspace(12*0.0016, 610*0.0016,100)
            mu_space = [mu1, mu2]
            n_param = 2 
    return problem_name, variable, mu_space, n_param
